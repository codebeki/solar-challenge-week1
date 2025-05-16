Solar Challenge Week 1
Project Overview
This repository, solar-challenge-week1, serves as a foundational setup for the project, including environment configuration, GitHub Actions for CI/CD, and essential development practices.

1. Environment Setup
To reproduce the development environment:

Clone the Repository
bash
git clone <repository-url>
cd solar-challenge-week1

Create a Virtual Environment

Using venv
python -m venv .venv
source .venv/Scripts/activate  # (Git Bash/Windows)
source .venv/bin/activate      # (Mac/Linux)
Using Conda (Alternative)

conda create --name my_env python=3.9
conda activate my_env

Install Dependencies
pip install -r requirements.txt

2. Git Workflow
Branching & Commits

Create a new branch for setup tasks
git checkout -b setup-task

Make at least 3 commits
git add .gitignore
git commit -m "init: add .gitignore"
git add requirements.txt
git commit -m "chore: venv setup"

git add .github/workflows/ci.yml
git commit -m "ci: add GitHub Actions workflow"
Push Changes
git push origin setup-task
Merge the Branch
Create a Pull Request in GitHub.

Title: "Setup task"

Description: "This PR adds the.gitignore,requirements.txt, and GitHub Actions workflow configuration."

Merge setup-task into main.

3. Continuous Integration (CI)
GitHub Actions Workflow (.github/workflows/ci.yml)
This workflow ensures dependencies are installed and Python version is verified.

yaml
name: Basic CI

on:
  push:
    branches:
      - main
      - setup-task
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

       - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9' //This is different from each other based on the use of python

      - name: Verify Python version
        run: python --version

      - name: Install dependencies
        run: pip install -r requirements.txt
4. Project Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
5. Key Performance Indicators (KPIs)
Development Environment Setup: Ensures smooth installation and execution of dependencies.

Version Control & CI/CD: Maintains structured commits and automated testing with GitHub Actions.
