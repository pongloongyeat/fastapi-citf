import requests
from typing import List, Union
from requests.models import HTTPError

from commit import Commit
from utils import add_params_to_url


BASE_URL = 'https://api.github.com/repos/CITF-Malaysia/citf-public/commits'

class CommitUtils:
    def get_commit_history_with_params(params: dict) -> Union[None, List[Commit]]:
        try:
            response = requests.get(add_params_to_url(base_url=BASE_URL, params=params))
            response.raise_for_status()
        except HTTPError as http_err:
            print(http_err)
            return
        except Exception as err:
            print(err)
            return
        else:
            return [Commit(**x) for x in response.json()]

    def get_file_commit_history(repo_filepath: str, per_page: int) -> Union[None, List[Commit]]:
        return CommitUtils.get_commit_history_with_params(params={
            'path': repo_filepath,
            'per_page': per_page
        })

    def get_latest_file_commit(repo_filepath: str) -> Union[None, Commit]:
        return CommitUtils.get_file_commit_history(repo_filepath=repo_filepath, per_page=1)[0]

    def get_commit_history(per_page: int) -> Union[None, List[Commit]]:
        return CommitUtils.get_commit_history_with_params(params={
            'per_page': per_page
        })

    def get_latest_commit() -> Union[None, Commit]:
        return CommitUtils.get_commit_history(per_page=1)[0]


if __name__ == '__main__':
    print(CommitUtils.get_latest_commit())
