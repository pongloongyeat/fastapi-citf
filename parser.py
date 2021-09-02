import pandas

try:
    from commit_utils import CommitUtils
except ImportError:
    from .commit_utils import CommitUtils


class CITFGitHubCSVParser:
    BASE_REPO_URL = 'https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main'

    def __init__(self, path_to_csv: str) -> None:
        self.path_to_csv = path_to_csv

        # Get commit history to see if path is valid
        latest_commit = CommitUtils.get_latest_file_commit(self.path_to_csv)

        if latest_commit == None:
            raise ValueError(f'csv file does not exist at path: {path_to_csv}')

        self.__data = pandas.read_csv(f'{self.BASE_REPO_URL}/{self.path_to_csv}')

    def csv(self):
        """Returns the CSV file as a pandas DataFrame."""
        return self.__data


if __name__ == '__main__':
    parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_malaysia.csv')
    print(parser.csv())
