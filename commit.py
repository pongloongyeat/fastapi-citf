class Commit:
    def __init__(self, sha: str, node_id: str, *args, **kwargs) -> None:
        self.sha = sha
        self.node_id = node_id

    def __str__(self) -> str:
        return f'Commit {self.sha[:6]}'
