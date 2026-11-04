# Demo video script — Microsoft Repository Explorer

**Target length:** 2–3 minutes

## 0:00–0:20 — Introduction

"Hi, this is my Swytchcode PPI project: Microsoft Repository Explorer. It is a small Python command-line application that retrieves public repositories from a GitHub organization through Swytchcode."

## 0:20–0:50 — Project and integration files

"Here is the project structure. The application is in `app/main.py`. The GitHub integration bundle includes `manifest.json`, `methods.json`, and `wrekenfile.yaml`. The Wrekenfile describes the available API methods, including `github.repo.get`."

Show the Wrekenfile entry for `github.repo.get`, including `GET /orgs/{org}/repos`.

## 0:50–1:25 — CLI workflow

"To set up the project, I used `swy init`, retrieved the provider with `swy get GitHub`, checked authentication with `swy auth status`, and added the method using `swy add method github.repo.get`."

Show the commands in the terminal. Do not show tokens, secrets, or private account information.

## 1:25–2:10 — Application and API operation

"The application asks for an organization and a repository count. It invokes `swy exec github.repo.get` with the organization as a path input and `type=public` and `per_page` as query parameters."

Run the application and show the real output only if the API call succeeds. If it does not, show the exact error and explain the blocker honestly. Do not present sample output as a real API response.

## 2:10–2:40 — Learning and conclusion

"One thing I learned was how a provider integration packages reusable API methods and configuration, and how the execution mode and endpoint configuration affect API calls. The main friction I encountered was that the GitHub sandbox endpoint was not configured, so I had to investigate the manifest and use the production endpoint."

## Recording checklist

- Keep the video under 3 minutes.
- Show the actual project files and relevant Wrekenfile entry.
- Show the CLI commands and actual API result or blocker.
- Hide credentials, OAuth tokens, email addresses if private, and other sensitive information.
- Do not claim a successful HTTP response unless it is visible in the recording.
