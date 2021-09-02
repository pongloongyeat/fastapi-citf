from typing import Dict, Union
from fastapi import FastAPI, HTTPException

# This try block serves no purpose
# other than to enable type hinting/
# suggestions for VSCode lol
try:
    from parser import CITFGitHubCSVParser
except ImportError:
    from .parser import CITFGitHubCSVParser


app = FastAPI()

# vax_registration_malaysia_parser = CITFGitHubCSVParser(path_to_csv='registration/vaxreg_malaysia.csv')
# vax_registration_state_parser = CITFGitHubCSVParser(path_to_csv='registration/vaxreg_state.csv')
# vax_malaysia_parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_malaysia.csv')
# vax_state_parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_state.csv')


@app.get('/')
@app.get('/help')
async def help() -> Dict:
    """Shows this help message."""

    return {
        '/': help.__doc__,
        '/help': help.__doc__,
        '/registration/malaysia': get_latest_registration_data_malaysia.__doc__,
        '/registration/malaysia/latest': get_latest_registration_data_malaysia.__doc__,
        '/registration/malaysia/{date}': get_registration_data_malaysia.__doc__,
        '/vaccination/malaysia': get_latest_vax_data_malaysia.__doc__,
        '/vaccination/malaysia/latest': get_latest_vax_data_malaysia.__doc__,
        '/vaccination/malaysia/{date}': get_vax_data_malaysia.__doc__,
        '/registration/state': get_latest_registration_data_state.__doc__,
        '/registration/state/all/latest': get_latest_registration_data_state.__doc__,
        '/registration/state/all/{date}': get_registration_data_all_state.__doc__,
        '/registration/state/{state}/latest': get_latest_registration_data_for_state.__doc__,
        '/registration/state/{state}/{date}': get_registration_data_state.__doc__,
        '/vaccination/state': get_latest_vax_data_state.__doc__,
        '/vaccination/state/all/latest': get_latest_vax_data_state.__doc__,
        '/vaccination/state/all/{date}': get_vax_data_all_state.__doc__,
        '/vaccination/state/{state}/latest': get_latest_vax_data_for_state.__doc__,
        '/vaccination/state/{state}/{date}': get_vax_data_state.__doc__,
    }

#region Malaysia
#region Vaccination registration statistics
@app.get('/registration/malaysia')
@app.get('/registration/malaysia/latest')
async def get_latest_registration_data_malaysia() -> Union[Dict, None]:
    """Returns the latest registration statistics for Malaysia."""

    return vax_registration_malaysia_parser.csv().tail(1).to_dict('records')[0]

@app.get('/registration/malaysia/{date}')
async def get_registration_data_malaysia(date: str) -> Union[Dict, None]:
    """Returns the registration statistics for Malaysia during a certain date with format YYYY-MM-DD."""

    dataframe = vax_registration_malaysia_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching[0]
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for date {date}')
#endregion

#region Vaccination statistics
@app.get('/vaccination/malaysia')
@app.get('/vaccination/malaysia/latest')
async def get_latest_vax_data_malaysia() -> Dict:
    """Returns the latest vaccination statistics for Malaysia."""

    return vax_malaysia_parser.csv().tail(1).to_dict('records')[0]

@app.get('/vaccination/malaysia/{date}')
async def get_vax_data_malaysia(date: str) -> Union[Dict, None]:
    """Returns the vaccination statistics for Malaysia during a certain date with format YYYY-MM-DD."""

    dataframe = vax_malaysia_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching[0]
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for date {date}')
#endregion
#endregion

#region State
#region Vaccination registration statistics
@app.get('/registration/state')
@app.get('/registration/state/all/latest')
async def get_latest_registration_data_state() -> Dict:
    """Returns the latest registration statistics for all states."""

    return vax_registration_state_parser.csv().tail(16).to_dict('records')

@app.get('/registration/state/all/{date}')
async def get_registration_data_all_state(date: str) -> Union[Dict, None]:
    """Returns the registration statistics for all states during a certain date with format YYYY-MM-DD."""

    dataframe = vax_registration_state_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for date {date}')

@app.get('/registration/state/{state}/latest')
async def get_latest_registration_data_for_state(state: str) -> Union[Dict, None]:
    """Returns the latest registration statistics for a specific state. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv)."""

    dataframe = vax_registration_state_parser.csv().tail(16)
    matching = dataframe[dataframe['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for state {state}')

@app.get('/registration/state/{state}/{date}')
async def get_registration_data_state(state: str, date: str) -> Union[Dict, None]:
    """Returns the registration statistics for a certain state during a certain date with format YYYY-MM-DD. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv)."""

    dataframe = vax_registration_state_parser.csv()
    matching = dataframe[dataframe['date'] == date]
    matching = matching[matching['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for state {state} and date {date}')
#endregion

#region Vaccination statistics
@app.get('/vaccination/state')
@app.get('/vaccination/state/all/latest')
async def get_latest_vax_data_state() -> Dict:
    """Returns the latest vaccination statistics for all states."""

    return vax_state_parser.csv().tail(16).to_dict('records')

@app.get('/vaccination/state/all/{date}')
async def get_vax_data_all_state(date: str) -> Union[Dict, None]:
    """Returns the vaccination statistics for all states during a certain date with format YYYY-MM-DD."""

    dataframe = vax_state_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for date {date}')

@app.get('/vaccination/state/{state}/latest')
async def get_latest_vax_data_for_state(state: str) -> Union[Dict, None]:
    """Returns the latest vaccination statistics for a specific state. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv)."""

    dataframe = vax_state_parser.csv().tail(16)
    matching = dataframe[dataframe['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for state {state}')

@app.get('/vaccination/state/{state}/{date}')
async def get_vax_data_state(state: str, date: str) -> Union[Dict, None]:
    """Returns the vaccination statistics for a certain state during a certain date with format YYYY-MM-DD. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv)."""

    dataframe = vax_state_parser.csv()
    matching = dataframe[dataframe['date'] == date]
    matching = matching[matching['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        raise HTTPException(status_code=404, detail=f'Record not found for state {state} and date {date}')
#endregion
#endregion
