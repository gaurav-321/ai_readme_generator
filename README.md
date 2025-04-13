# GitHub README Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/gag3301v/ai_readme_generator)](LICENSE)

 自动生成和增强GitHub仓库README文件的Python程序。

## ✨ Description

`ai_readme_generator` 是一个用于自动化生成和改进GitHub仓库README文件的工具。它可以根据项目文件内容自动生成新的README.md，增强现有的README.md，或总结整个仓库的内容并写入本地文件。该工具利用了GitHub API和OpenAI API来实现这些功能。

## 🚀 Features

- 自动生成README文件
- 增强现有README文件
- 总结仓库内容并写入本地文件
- 使用GitHub API获取仓库信息
- 使用OpenAI API生成文本摘要

## ⛠️ Installation

1. 克隆仓库：
   ```bash
   git clone https://github.com/gag3301v/ai_readme_generator.git
   cd ai_readme_generator
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Usage

### 生成README文件

```python
from main import add_readme

repo = "gaurav-321/my_repo"
add_readme(repo)
```

### 增强README文件

```python
from main import enhance_readme

repo = "gaurav-321/my_repo"
enhance_readme(repo)
```

### 总结仓库内容

```python
from main import summarize_repo

repo = "gaurav-321/my_repo"
summarize_repo(repo)
```

## 🔧 Configuration

在项目根目录下创建一个 `.env` 文件，并添加以下环境变量：

```plaintext
GITHUB_TOKEN=your_github_token_here
```

## 🧪 Tests

运行测试：

```bash
pytest
```

## 📁 Project Structure

```
ai_readme_generator/
├── config.py
├── github_api.py
├── main.py
├── prompts.py
├── requirements.txt
└── utils.py
```

## 👥 Contributing

欢迎贡献！请阅读 [CONTRIBUTING.md](https://github.com/gag3301v/ai_readme_generator/blob/master/CONTRIBUTING.md) 了解如何参与。

## 📄 License

本项目采用 [MIT 许可证](LICENSE)。