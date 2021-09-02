import os
import json


def add_params_to_url(base_url: str, params: dict):
    first = True
    url = base_url

    for key, val in params.items():
        if first:
            url += f'?{key}={val}'
            first = False
        else:
            url += f'&{key}={val}'

    return url

def save_metadata(filepath: str, metadata: dict):
    if not os.path.exists('cache'):
        os.mkdir('cache')

    filename = filepath.split('/')[-1]

    with open(f'cache/{filename}.metadata', 'w') as f:
        f.write(json.dumps(metadata))
