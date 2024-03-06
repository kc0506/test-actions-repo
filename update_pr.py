import os
from pathlib import Path

from github import Auth, Github

token_path = Path(__file__).parent / ".github/token"
token = os.getenv("TOKEN")
if not token:
    token = token_path.open().read()
pr_number = int(os.getenv("PR", "5"))

auth = Auth.Token(token)
g = Github(auth=auth)
repo = g.get_repo("ntu-grade-viewer/test-actions-repo")
pr = repo.get_pull(pr_number)


def section(title: str, body: list[str]):
    return f"\n## {title}\n" + "\n".join(["- " + s for s in body])


body = (pr.body or "") + section(
    "Commit messages (auto-generated)", [commit.commit.message for commit in pr.get_commits()]
)

pr.edit(body=body)
pr.update()

g.close()
