# Microsoft Repository Explorer

A Python command-line application that uses **Swytchcode** to retrieve and display public repositories from a GitHub organization.

This project was created for the Swytchcode PPI challenge. It demonstrates how a Python application can invoke a reusable GitHub API operation through the Swytchcode CLI.

## What it does

The application asks for:
- A GitHub organization name (defaults to `microsoft`)
- The number of repositories to display (1–30)

It invokes the Swytchcode method `github.repo.get`, which maps to GitHub's `GET /orgs/{org}/repos` endpoint. The application requests public repositories and displays each repository's:
- Full name
- Description
- Primary programming language
- Stars
- Forks
- Open issues
- GitHub URL

## Project structure

```text
swytchcode-github-repository-explorer/
├── .swytchcode/
│   └── integrations/
│       ├── manifest.json
│       └── GitHub/
│           └── github/
│               └── 1.1.4/
│                   ├── methods.json
│                   └── wrekenfile.yaml
├── app/
│   └── main.py
├── docs/
│   └── demo-script.md
├── .gitignore
└── README.md
```

The GitHub integration bundle contains the Wrekenfile and method catalogue. In this project, the Wrekenfile was found inside the downloaded integration bundle, rather than at the project root immediately after `swy init`.

## Requirements

- Python 3.12 or later
- Swytchcode CLI installed and available on `PATH`
- A Swytchcode account
- GitHub authentication connected through Swytchcode

## Setup

Run these commands from the project directory in PowerShell.

### 1. Initialize a Swytchcode project

```powershell
swy init
```

### 2. Retrieve the GitHub integration

```powershell
swy get GitHub
```

The downloaded integration includes the GitHub method catalogue and Wrekenfile. The submitted repository includes the integration files used during this attempt.

### 3. Add the repository-listing method

```powershell
swy add method github.repo.get
```

### 4. Connect GitHub authentication

```powershell
swy auth connect GitHub
swy auth status
```

Complete the authentication flow in the CLI/browser if prompted. Do not commit credentials, tokens, or local authentication files.

### 5. Configure the execution mode

The GitHub integration manifest in this attempt declares:
- Production endpoint: `https://api.github.com`
- Sandbox endpoint: empty

During troubleshooting, I identified that the sandbox endpoint was not set and investigated using the production endpoint. The local `.swytchcode/tooling.json` is intentionally excluded from this repository because it is machine/project-local configuration, so the exact local execution-mode setting cannot be verified from the shared files. Configure the execution mode in your own initialized workspace using the Swytchcode CLI/configuration guidance for your installed version.

### 6. Run the application

```powershell
python app/main.py
```

Enter an organization name (or press Enter to use `microsoft`) and a repository count between 1 and 30.

## Run the API operation directly

The application invokes the following command structure:

```powershell
swy exec github.repo.get --input org=microsoft --param type=public --param per_page=5 --json
```

The method definition in the included Wrekenfile identifies:
- HTTP method: `GET`
- Endpoint: `/orgs/{org}/repos`
- Required path input: `org`
- Optional query inputs: `type`, `sort`, `direction`, `per_page`, and `page`

## How the application works

1. `app/main.py` collects the organization and repository count.
2. Python's `subprocess` module invokes `swy exec`.
3. Swytchcode runs `github.repo.get` using the supplied organization and query parameters.
4. The CLI returns its JSON output.
5. Python parses the response and prints the repository fields in the terminal.

## What was explored

- Initializing a project with `swy init`
- Retrieving the GitHub integration with `swy get GitHub`
- Inspecting the integration's `wrekenfile.yaml`, `methods.json`, and `manifest.json`
- Checking authentication with `swy auth status`
- Adding `github.repo.get`
- Previewing an API operation and investigating the missing sandbox endpoint
- Configuring production execution for the GitHub API

The sandbox endpoint was empty in the downloaded manifest, while the production endpoint was `https://api.github.com`. This was the main configuration issue encountered during the attempt.

## Reproducing the attempt

Use the setup steps above, then run:

```powershell
python app/main.py
```

The CLI, authentication state, and local tooling configuration are environment-specific. A fresh user must configure their own Swytchcode workspace and GitHub authentication.

## Security and repository notes

- `.swytchcode/tooling.json`, lock files, local workspace files, Python caches, virtual environments, and `.env` files are excluded through `.gitignore`.
- Never commit API keys, OAuth tokens, passwords, or other credentials.
- The included integration files are the provider metadata used for this project; they do not contain the user's authentication credentials.

## Limitations

- The application is a small CLI demonstration, not a hosted web application.
- It retrieves public repositories only.
- The live API result depends on the organization, authentication, and GitHub API availability.
- The application has been syntax-checked, but a live API run must be verified in the configured Swytchcode environment before claiming a successful execution.

## Author

Created as part of the **Swytchcode PPI Assignment**.
