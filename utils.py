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
