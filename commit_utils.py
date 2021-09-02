import json
import requests
from typing import Union
from requests.models import HTTPError

from commit import Commit


BASE_URL = 'https://api.github.com/repos/CITF-Malaysia/citf-public/commits'

class CommitUtils:
    def get_commit_history(per_page: int) -> Union[None, Commit]:
        endpoint_url = f'{BASE_URL}?per_page={per_page}'

        try:
            response = requests.get(endpoint_url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(http_err)
            return
        except Exception as err:
            print(err)
            return
        else:
            return [Commit(**x) for x in response.json()]

    def get_latest_commit() -> Union[None, Commit]:
        return CommitUtils.get_commit_history(per_page=1)[0]


if __name__ == '__main__':
    print(CommitUtils.get_latest_commit())
