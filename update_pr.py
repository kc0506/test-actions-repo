import os
from pathlib import Path

from github import Auth, Github

token_path = Path(__file__).parent / ".github/token"
token = os.getenv("TOKEN")
if not token:
    token = token_path.open().read()
pr_number = int(os.getenv("PR", "5"))
action = os.getenv("ACTION", "")
version = os.getenv("VERSION", "")

auth = Auth.Token(token)
g = Github(auth=auth)
# print(g.get_user().name)

repo = g.get_repo("kc0506/test-actions-repo")
pr = repo.get_pull(4)
print(pr.mergeable_state)
exit(0)


def section(title: str, body: list[str]):
    return f"\n## {title}\n" + "\n".join(["- " + s for s in body])


match action:
    case "title":
        pr.edit(title=f"v{version} release")
        pr.update()
        print(version)
    case "body":
        body = (pr.body or "") + section(
            "Commit messages (auto-generated)",
            [commit.commit.message for commit in pr.get_commits()],
        )

        pr.edit(body=body)
        pr.update()

g.close()
