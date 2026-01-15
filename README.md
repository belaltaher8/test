# Test Repository

[![GitHub Actions](https://github.com/belaltaher8/test/workflows/go-linter/badge.svg)](https://github.com/belaltaher8/test/actions)

A test repository for experimenting with GitHub features, workflows, and automation.

## 📖 Overview

This repository serves as a testing ground for various GitHub capabilities including:
- GitHub Actions workflows
- Custom GitHub Copilot agents
- Continuous Integration/Continuous Deployment (CI/CD) pipelines
- Repository automation

## 🚀 Features

### GitHub Actions Workflow

The repository includes a basic GitHub Actions workflow (`go-linter`) that:
- Triggers on pull requests, merge groups, and manual workflow dispatch
- Runs on Ubuntu latest
- Executes a simple test step that echoes "hi"

### Custom Agents

The repository contains several custom GitHub Copilot agents in the `.github/agents/` directory:
- **default.agent.md** - Default agent configuration
- **longDescription.md** - Agent with extended documentation
- **my-agent.md** - Custom agent for testing
- **not-the-right.agent.md** - Alternative agent configuration

## 📋 Prerequisites

No special prerequisites are required to use this repository. It's designed as a lightweight testing environment.

## 🛠️ Usage

### Running Workflows

Workflows can be triggered in several ways:

1. **Automatically**: Open a pull request to trigger the workflow
2. **Manually**: Use the GitHub Actions UI to trigger via workflow_dispatch
3. **Merge Groups**: Workflows run when commits are added to merge queues

### Testing Locally

Clone the repository:

```bash
git clone https://github.com/belaltaher8/test.git
cd test
```

## 📁 Repository Structure

```
.
├── .github/
│   ├── agents/           # Custom GitHub Copilot agents
│   └── workflows/        # GitHub Actions workflows
│       └── my-action.yaml
└── README.md            # This file
```

## 🤝 Contributing

This is a test repository, but contributions are welcome for:
- Improving workflow examples
- Adding new test scenarios
- Enhancing documentation
- Adding new agent configurations

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This is a test repository and is provided as-is for experimental purposes.

## 🔗 Links

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---

**Note**: This is a test repository created for experimentation and learning purposes.
