import json
import os
import pandas
from datetime import date, datetime

try:
    from commit_utils import CommitUtils
    from utils import save_metadata
except ImportError:
    from .commit_utils import CommitUtils
    from .utils import save_metadata


class CITFGitHubCSVParser:
    BASE_REPO_URL = 'https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main'

    def __init__(self, path_to_csv: str) -> None:
        self.path_to_csv = path_to_csv

        # Create cache path
        if not os.path.exists('cache'):
            os.mkdir('cache')

        self.__update_data()

    def __update_data(self):
        filename = self.path_to_csv.split('/')[-1]

        if os.path.exists(f'cache/{filename}') and os.path.exists(f'cache/{filename}.metadata'):
            print(f'Using cached file at cache/{filename}...')

            # Check metadata and ensure its updated
            with open(f'cache/{filename}.metadata', 'r') as f:
                metadata = json.load(f)

            last_updated = metadata['last_updated']

            # Update every hour
            if (datetime.now() - datetime.strptime(last_updated, "%Y-%m-%d %H:%M:%S.%f")).seconds > 3600:
                print('Updating cache...')

                # Re-update
                latest_commit = CommitUtils.get_latest_file_commit(self.path_to_csv)

                self.__data = pandas.read_csv(f'{self.BASE_REPO_URL}/{self.path_to_csv}')
                self.__data.to_csv(f'cache/{filename}')

                # Cache the CSV file so GitHub API doesn't ban us
                save_metadata(filepath=self.path_to_csv, metadata={
                    'latest_commit': latest_commit.sha,
                    'last_updated': str(datetime.now())
                })
            else:
                # Use cached file
                self.__data = pandas.read_csv(f'cache/{filename}')
        else:
            print('Fetching file from GitHub...')

            # Get commit history to see if path is valid
            latest_commit = CommitUtils.get_latest_file_commit(self.path_to_csv)

            if latest_commit == None:
                raise ValueError(f'csv file does not exist at path: {self.path_to_csv}')

            self.__data = pandas.read_csv(f'{self.BASE_REPO_URL}/{self.path_to_csv}')
            self.__data.to_csv(f'cache/{filename}')

            # Cache the CSV file so GitHub API doesn't ban us
            save_metadata(filepath=self.path_to_csv, metadata={
                'latest_commit': latest_commit.sha,
                'last_updated': str(datetime.now())
            })

    def csv(self):
        """Returns the CSV file as a pandas DataFrame."""
        self.__update_data()
        return self.__data


if __name__ == '__main__':
    parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_malaysia.csv')
    print(parser.csv())
