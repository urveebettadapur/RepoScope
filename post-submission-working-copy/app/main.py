import subprocess
import json

def get_repositories(org, count):
    command = [
        "swy", "exec", "github.repo.get",
        "--input", f"org={org}",
        "--param", "type=public",
        "--param", f"per_page={count}",
        "--json"
    ]

    try:
        result = subprocess.run(
            command,
    	    capture_output=True,
    	    text=True,
            encoding="utf-8",
            errors="replace",
            check=True
        )

        # Extract the JSON response from CLI output
        output = result.stdout
        start = output.find('{"data"')

        if start == -1:
            print("Could not find repository data.")
            print(output)
            return

        response = json.loads(output[start:])
        repositories = response.get("data", [])

        print(f"\nPublic repositories for: {org}")
        print("=" * 65)

        for repo in repositories:
            print(f"\nName: {repo.get('full_name', 'N/A')}")
            print(f"Description: {repo.get('description') or 'No description'}")
            print(f"Language: {repo.get('language') or 'Not specified'}")
            print(f"Stars: {repo.get('stargazers_count', 0)}")
            print(f"Forks: {repo.get('forks_count', 0)}")
            print(f"Open issues: {repo.get('open_issues_count', 0)}")
            print(f"URL: {repo.get('html_url', 'N/A')}")
            print("-" * 65)

    except subprocess.CalledProcessError as error:
        print("Swytchcode execution failed.")
        print(error.stderr)
    except json.JSONDecodeError:
        print("Could not parse the API response.")
    except FileNotFoundError:
        print("Swytchcode CLI was not found. Check your PATH.")


if __name__ == "__main__":
    print("MICROSOFT REPOSITORY EXPLORER")
    print("=" * 35)

    organization = input("Enter GitHub organization (default: microsoft): ").strip()
    if not organization:
        organization = "microsoft"

    try:
        count = int(input("Number of repositories to display (1-30): "))
        if not 1 <= count <= 30:
            raise ValueError
    except ValueError:
        print("Please enter a number between 1 and 30.")
        raise SystemExit

    get_repositories(organization, count)
