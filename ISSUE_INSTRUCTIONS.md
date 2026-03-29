# GitHub Issue Creation Instructions

## About This Repository

This repository contains a poem that was requested to be shared via a GitHub issue.

## The Poem

The poem has been created and saved in `poem.md`. You can view it by opening that file.

## Creating the GitHub Issue

Since automated tools have limitations in creating GitHub issues directly, please follow these steps to create the issue manually:

### Steps:

1. Navigate to the [Issues tab](../../issues) of this repository
2. Click "New Issue"
3. Use the following details:

**Title:** `A Digital Ode - Poem for the Repository`

**Body:**
```markdown
# A Digital Ode

In circuits deep and code so bright,
Where bits and bytes dance through the night,
A repository waits with open arms,
To hold our work, our digital charms.

Through branches green and merges true,
Commits that tell what we pursue,
Each line of code, a story told,
Of dreams transformed to digital gold.

The programmer sits with thoughtful gaze,
Through algorithms, a careful maze,
With every function, loop, and test,
They strive to give their very best.

From issue tracker to pull request,
Collaboration at its best,
Together building, line by line,
A codebase elegant and fine.

So here we write in languages grand,
With logic guided by our hand,
In this repository we trust,
Where innovation is a must.

---

*Written with care and creativity,*  
*A poem for the digital age.*
```

4. Add labels if desired (e.g., `documentation`, `poetry`, `enhancement`)
5. Click "Submit new issue"

## Alternative

You can also use the GitHub CLI to create the issue:

```bash
gh issue create --title "A Digital Ode - Poem for the Repository" --body-file poem.md
```

Or via the GitHub API:

**Note:** Never hardcode tokens in scripts. Use environment variables for security.

```bash
# Set your token as an environment variable first:
# export GITHUB_TOKEN=your_token_here

curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/issues \
  -d '{"title":"A Digital Ode - Poem for the Repository","body":"[Content of poem.md]"}'
```

Replace `OWNER/REPO` with your actual repository owner and name (e.g., `belaltaher8/test`).
