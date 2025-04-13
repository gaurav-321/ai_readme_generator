# GitHub Repository Automation and Summarization

## Description
The GitHub Repository Automation and Summarization project is designed to automate various tasks related to managing and enhancing GitHub repositories. This includes fetching repository information, listing files, uploading new files, generating summaries, and updating READMEs based on the content of the repository.

## 🚀 Features
- **Fetch Repositories**: Retrieve all repositories for a specified GitHub user.
- **List Files**: Get file paths of all files in a specific repository.
- **Upload Files**: Upload or update files in a GitHub repository.
- **Generate Summaries**: Create high-level summaries of Python files using natural language processing (NLP) prompts.
- **Update READMEs**: Automatically enhance and generate new README.md files based on summarized content.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gag3301v/ai_readme_generator.git
   ```
2. Change to the project directory:
   ```bash
   cd ai_readme_generator
   ```
3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Usage
### config.py
This file configures the environment for interacting with the GitHub API.

```python
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {GITHUB_TOKEN}'}
owner = 'gaurav-321'
debug = False
logging.basicConfig(level='DEBUG' if debug else 'INFO')
```

### github_api.py
This script interacts with the GitHub API to fetch repository information and manage files.

```python
import httpx
from config import headers, owner

def find_all_repo(OWNER="gaurav-321"):
    # Fetch all repositories for a given GitHub user
    pass

def get_all_files(OWNER, REPO):
    # Retrieve file paths of all files in a specified repository
    pass

def get_file_data(OWNER, REPO, BRANCH, FILE_PATH):
    # Fetch the content of a specific file from a repository
    pass

def upload_file_to_github(OWNER, REPO, filepath, content, commit_message):
    # Upload or update files in a GitHub repository
    pass
```

### utils.py
This script uses the OpenAI API to generate summaries of text prompts.

```python
import openai

client = openai.Client(api_key='your_openai_api_key')

def summarize_file(prompt, model="qwen2.5-coder:7b"):
    # Generate a summary of the input text prompt using the OpenAI API
    pass
```

## 📖 Documentation
For more detailed documentation and examples, refer to the [GitHub Repository Automation and Summarization Wiki](https://github.com/gag3301v/ai_readme_generator/wiki).

## Contributing
Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.