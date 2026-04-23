# Test Repository

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/belaltaher8/test/my-action.yaml?branch=main)](https://github.com/belaltaher8/test/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 About

This is a test repository for experimenting with GitHub features, workflows, and automation. It serves as a playground for testing various GitHub Actions, workflows, and custom agents.

## 🚀 Features

- **GitHub Actions Workflows**: Automated CI/CD pipelines
- **Custom Agents**: GitHub agents for specialized tasks
- **Test Workflow**: Simple greeting workflow for testing

## 📁 Repository Structure

```
.
├── .github/
│   ├── agents/           # Custom GitHub agents
│   │   ├── default.agent.md
│   │   ├── longDescription.md
│   │   ├── my-agent.md
│   │   └── not-the-right.agent.md
│   └── workflows/        # GitHub Actions workflows
│       └── my-action.yaml
└── README.md            # This file
```

## 🔧 GitHub Workflows

### My Action Workflow

The repository includes a GitHub Actions workflow (`my-action.yaml`) that:
- Triggers on pull requests, merge groups, and manual dispatch
- Runs on Ubuntu latest
- Includes a simple greeting step

**Workflow triggers:**
- Pull requests
- Merge groups
- Manual workflow dispatch

## 🤖 Custom Agents

This repository contains several custom GitHub agents in the `.github/agents/` directory:
- `default.agent.md` - Default agent configuration
- `longDescription.md` - Agent with extended description
- `my-agent.md` - Custom agent for testing
- `not-the-right.agent.md` - Alternative agent configuration

## 🛠️ Usage

This repository is primarily used for testing and experimentation. You can:

1. **Fork the repository** to create your own testing environment
2. **Modify workflows** to test different GitHub Actions configurations
3. **Add custom agents** to experiment with automation
4. **Test CI/CD pipelines** before implementing in production

## 📝 Development

### Prerequisites

- Git
- GitHub account
- Basic understanding of GitHub Actions

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/belaltaher8/test.git
   cd test
   ```

2. Make your changes

3. Push to your fork or create a pull request

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/belaltaher8/test/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**belaltaher8**

- GitHub: [@belaltaher8](https://github.com/belaltaher8)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

<p align="center">Made with ❤️ for testing and learning</p>
