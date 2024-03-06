import os
from pathlib import Path

from github import Auth, Github

token_path = Path(__file__).parent / "../token"
# token = token_path.open().read()
token = os.getenv("TOKEN", "")
auth = Auth.Token(token)

g = Github(auth=auth)

repo = g.get_repo("ntu-grade-viewer/test-actions-repo")
pull = repo.get_pull(4)
pull.edit(body="Updated")
pull.update()
commit = pull.get_commits()[0]
print(commit.commit.message)

g.close()
