# Test Repository

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/belaltaher8/test/my-action.yaml?label=go-linter)
![GitHub](https://img.shields.io/github/license/belaltaher8/test)
![GitHub last commit](https://img.shields.io/github/last-commit/belaltaher8/test)

A test repository demonstrating GitHub Actions workflows and custom agent configurations.

## 📋 Overview

This repository serves as a testing ground for:
- **GitHub Actions Workflows**: Automated CI/CD pipelines
- **Custom Agents**: Specialized agent configurations for various tasks
- **Development Best Practices**: Template for GitHub repository structure

## 🚀 Features

### GitHub Actions Workflow

The repository includes a `go-linter` workflow that:
- Triggers on pull requests, merge groups, and manual workflow dispatch
- Runs on Ubuntu latest
- Executes basic validation steps

**Workflow Configuration**: [`.github/workflows/my-action.yaml`](.github/workflows/my-action.yaml)

### Custom Agents

This repository includes several custom agent configurations located in `.github/agents/`:

- **default.agent.md** - Default agent configuration
- **longDescription.md** - Agent with extended documentation
- **my-agent.md** - Custom agent for testing
- **not-the-right.agent.md** - Alternative agent configuration

## 📁 Repository Structure

```
.
├── .github/
│   ├── agents/          # Custom agent configurations
│   └── workflows/       # GitHub Actions workflows
└── README.md           # This file
```

## 🛠️ Getting Started

### Prerequisites

- Git installed on your local machine
- GitHub account with access to this repository

### Clone the Repository

```bash
git clone https://github.com/belaltaher8/test.git
cd test
```

## 📖 Usage

This repository can be used as:

1. **Testing Ground**: Experiment with GitHub Actions and workflows
2. **Template**: Base structure for new repositories
3. **Learning Resource**: Understanding CI/CD pipelines and custom agents

## 🔧 Workflow Details

The `go-linter` workflow is configured with:

- **Triggers**: Pull requests, merge groups, workflow dispatch
- **Permissions**: 
  - `id-token: write`
  - `contents: read`
- **Environment**: `HUSKY: 0`

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is available as open source. Please check the repository settings for license details.

## 📬 Contact

For questions or feedback, please open an issue in this repository.

---

**Note**: This is a test repository for experimentation and learning purposes.
