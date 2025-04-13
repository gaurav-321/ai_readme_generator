from config import *
from github_api import find_all_repo, get_all_files, get_file_data, upload_file_to_github
from prompts import *
from utils import summarize_file

# Configure basic logging


# Valid file types to include in README summarization
valid_files = [".py", ".txt", ".md"]


def add_readme(repo):
    """Generates and uploads a new README.md based on the summarized content of project files."""
    try:
        file_content = get_file_data(owner, repo, "master", "README.md")
        if file_content:
            logging.warning(f"README.md already exist: {repo}")
            return
        files_paths = get_all_files(owner, REPO=repo)
        files_paths = [x for x in files_paths if x.lower().endswith(tuple(valid_files))]
        prompt_temp = prompt_readme + f"\nUrl for this repo is https://github.com/gag3301v/{repo}"

        if not files_paths:
            logging.warning(f"No valid files found in repo: {repo}")
            return None

        for file in files_paths:
            try:
                file_content = get_file_data(owner, repo, "master", file)
                prompt_summarizer_temp = prompt_summarizer + "\n" + file + "\n" + file_content
                prompt_temp += f"\nFile Path : {file}\n"
                prompt_temp += f"File Summarizer : {summarize_file(prompt_summarizer_temp)}\n"
                prompt_temp += "-" * 60
            except Exception as e:
                logging.error(f"Error summarizing file {file}: {e}")
                continue

        logging.info(f"Total prompt length: {len(prompt_temp)} characters")

        output = summarize_file(prompt_temp)

        # Write the new README locally
        with open(f"temp/README_{repo}.md", "w", encoding="utf-8", errors="ignore") as f:
            f.write(output)

        logging.info(f"Generated README.md for repo: {repo}")
        upload_file_to_github(owner, repo, "README.md", output, "Better UI")

    except Exception as e:
        logging.exception("Error during README generation")


def summarize_repo(repo):
    """Generates a high-level analysis of the entire repository and writes it to a summary file."""
    try:
        files_paths = get_all_files(owner, REPO=repo)
        files_paths = [x for x in files_paths if x.lower().endswith(tuple(valid_files))]
        prompt_temp = prompt_repo_analysis + f"\nUrl for this repo is https://github.com/gag3301v/{repo}"

        if not files_paths:
            logging.warning(f"No valid files found in repo: {repo}")
            return None

        for file in files_paths:
            try:
                file_content = get_file_data(owner, repo, "master", file)
                prompt_summarizer_temp = prompt_summarizer + "\n" + file + "\n" + file_content
                prompt_temp += f"\nFile Path : {file}\n"
                prompt_temp += f"File Summarizer : {summarize_file(prompt_summarizer_temp)}\n"
                prompt_temp += "-" * 60
            except Exception as e:
                logging.error(f"Error summarizing file {file}: {e}")
                continue

        logging.info(f"Total prompt length: {len(prompt_temp)} characters")

        output = summarize_file(prompt_temp)

        # Write the summary to a local file
        with open(f"temp/SUMMARY_{repo}.txt", "w", encoding="utf-8", errors="ignore") as f:
            f.write(output)

    except Exception as e:
        logging.exception("Error during repository summarization")


def enhance_readme(repo):
    """Improves the existing README.md file by reformatting and rewriting its content."""
    try:
        logging.info(f"Enhancing README.md for repo: {repo}")
        prompt_temp = prompt_readme_single + "\n"
        file_content = get_file_data(owner, repo, "master", "README.md")
        if not file_content:
            logging.warning(f"README.md not found in repo: {repo}")
            return

        prompt_temp += f"\nFile Path : README.md\n"
        prompt_temp += f"File Data : {file_content}\n"

        output = summarize_file(prompt_temp)

        # Save the enhanced README
        with open(f"temp/README_{repo}.md", "w", encoding="utf-8", errors="ignore") as f:
            f.write(output)
        logging.info(f"README enhanced for repo: {repo}:temp/README_{repo}.md")
        upload_file_to_github(owner, repo, "README.md", output, "Enhanced Readme")

    except Exception as e:
        logging.exception("Error enhancing README")


if __name__ == "__main__":
    owner = "gaurav-321"
    repos = find_all_repo(owner)

    # Print available repos with index
    print("\n📦 Repositories found:")
    for i, repo in enumerate(repos):
        print(f"[{i}] {repo}")

    print("\n💡 Choose an option:")
    print("1. Enhance existing README.md")
    print("2. Add new README.md if missing")
    print("3. Summarize repository")

    action_input = input("Enter action number (1/2/3): ").strip()
    action_map = {"1": "enhance", "2": "add", "3": "summarize"}
    action = action_map.get(action_input)

    if not action:
        print("❌ Invalid action. Exiting.")
        exit(1)

    index_input = input("Enter repo number (or press Enter for all): ").strip()

    # Determine which repos to run on
    if index_input == "":
        selected_repos = repos
    else:
        try:
            idx = int(index_input)
            selected_repos = [repos[idx]]
        except (ValueError, IndexError):
            print("❌ Invalid repo index. Exiting.")
            exit(1)

    # Run the chosen action on selected repos
    for repo_name in selected_repos:
        print(f"\n🚀 Running '{action}' on: {repo_name}")
        try:
            if action == "enhance":
                enhance_readme(repo_name)
            elif action == "add":
                add_readme(repo_name)
            elif action == "summarize":
                summarize_repo(repo_name)
        except Exception as e:
            logging.error(f"Failed to process {repo_name}: {e}")