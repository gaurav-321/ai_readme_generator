import base64
import logging
from datetime import datetime, timedelta

import httpx
import requests

from config import *

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def find_all_repo(OWNER="gaurav-321"):
    url = f"https://api.github.com/users/{OWNER}/repos"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    repo_names = []
    page = 1

    logging.info(f"Fetching repositories for user: {OWNER}")

    while True:
        response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        if response.status_code != 200:
            logging.error(f"GitHub API error: {response.status_code} – {response.text}")
            raise Exception(f"GitHub API error: {response.status_code}, {response.text}")

        repos = response.json()
        if not repos:
            break  # Exit loop if no more repositories

        repo_names.extend([repo["name"] for repo in repos])
        page += 1

    for name in repo_names:
        logging.info(f"Found repo: {name}")

    return repo_names


def get_all_files(OWNER, REPO):
    logging.info(f"Fetching file list from repo: {OWNER}/{REPO}")
    logging.info(f"URL: https://github.com/{OWNER}/{REPO}")

    repo_info_url = f"https://api.github.com/repos/{OWNER}/{REPO}"
    repo_info = requests.get(repo_info_url, headers=headers).json()
    default_branch = repo_info.get("default_branch", "main")

    branch_url = f"https://api.github.com/repos/{OWNER}/{REPO}/branches/{default_branch}"
    branch_info = requests.get(branch_url, headers=headers).json()
    tree_sha = branch_info["commit"]["commit"]["tree"]["sha"]

    tree_url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{tree_sha}?recursive=1"
    tree_data = requests.get(tree_url, headers=headers).json()

    files = [item["path"] for item in tree_data["tree"] if item["type"] == "blob"][:20]

    for f in files:
        logging.debug(f"File: {f}")

    return files


def get_file_data(OWNER, REPO, BRANCH, FILE_PATH):
    raw_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{FILE_PATH}"
    logging.info(f"Fetching file content: {OWNER}/{REPO}/{FILE_PATH}")

    response = requests.get(raw_url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        logging.error(f"Failed to fetch file '{FILE_PATH}' from repo '{REPO}' "
                      f"(Status: {response.status_code})")
        logging.debug(response.text)
        return None


def upload_file_to_github(OWNER, REPO, filepath, content, commit_message):
    """
    Create or update a file in your GitHub repo via GitHub’s REST API.
    `filepath` is where the file will live in the repo, e.g. 'README.md'.
    """
    if debug:
        logging.warning("Debug mode ON — skipping actual upload.")
        return

    logging.info(f"Uploading file to GitHub: {OWNER}/{REPO}/{filepath}")

    api_url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{filepath}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    with httpx.Client() as client:
        # 1. Check if file already exists
        resp = client.get(api_url, headers=headers)
        sha = resp.json().get("sha") if resp.status_code == 200 else None

        # 2. Encode file content in base64
        encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")

        data = {
            "message": commit_message,
            "content": encoded_content,
            "sha": sha  # include SHA if updating
        }

        # 3. PUT request to create or update the file
        put_resp = client.put(api_url, json=data, headers=headers)
        if put_resp.status_code in [200, 201]:
            logging.info(f"✅ File '{filepath}' successfully uploaded to '{REPO}'.")
        else:
            logging.error(
                f"❌ Failed to upload '{filepath}' to '{REPO}'. "
                f"Status: {put_resp.status_code}, Response: {put_resp.text}"
            )
            raise RuntimeError(
                f"GitHub upload failed – {put_resp.status_code}: {put_resp.text}"
            )
