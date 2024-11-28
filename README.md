# Python GitHub Actions Example

This project demonstrates the use of GitHub Actions for CI/CD with Python.

## Features
- **Automatic Workflow**: Runs linting and tests automatically on pull requests.
- **Manual Workflow**: Can be triggered manually for additional tasks.

## How to Use
1. Clone this repository.
2. Create a pull request to see the automatic workflow in action.
3. Trigger the manual workflow from the "Actions" tab in GitHub.

## Run Locally
```bash
pip install -r requirements.txt
flake8 app tests
python -m unittest discover -s tests
```

---

### **How to Test**

1. Push the project to a new GitHub repository.
2. Create a pull request to see the automatic workflow run.
3. Trigger the manual workflow from the "Actions" tab.

This simple setup demonstrates how to integrate and test automatic and manual workflows in GitHub Actions.