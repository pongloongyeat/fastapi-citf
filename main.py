from typing import Dict
from fastapi import FastAPI
from parser import CITFGitHubCSVParser


app = FastAPI()

vax_registration_malaysia_parser = CITFGitHubCSVParser(path_to_csv='registration/vaxreg_malaysia.csv')
vax_registration_state_parser = CITFGitHubCSVParser(path_to_csv='registration/vaxreg_state.csv')
vax_malaysia_parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_malaysia.csv')
vax_state_parser = CITFGitHubCSVParser(path_to_csv='vaccination/vax_state.csv')


@app.get('/')
@app.get('/help')
async def help() -> Dict:
    return {"message": "Hello World"}

#region Malaysia
#region Vaccination registration statistics
@app.get('/registration/malaysia')
@app.get('/registration/malaysia/latest')
async def get_latest_registration_data_malaysia() -> Dict:
    return vax_registration_malaysia_parser.csv().tail(1).to_dict('records')[0]

@app.get('/registration/malaysia/{date}')
async def get_registration_data_malaysia(date: str) -> Dict:
    dataframe = vax_registration_malaysia_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching[0]
    else:
        return {}
#endregion

#region Vaccination statistics
@app.get('/vaccination/malaysia')
@app.get('/vaccination/malaysia/latest')
async def get_latest_vax_data_malaysia() -> Dict:
    return vax_malaysia_parser.csv().tail(1).to_dict('records')[0]

@app.get('/vaccination/malaysia/{date}')
async def get_vax_data_malaysia(date: str) -> Dict:
    dataframe = vax_malaysia_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching[0]
    else:
        return {}
#endregion
#endregion

#region State
#region Vaccination registration statistics
@app.get('/registration/state')
@app.get('/registration/state/all/latest')
async def get_latest_registration_data_state() -> Dict:
    return vax_registration_state_parser.csv().tail(16).to_dict('records')

@app.get('/registration/state/{state}/latest')
async def get_latest_registration_data_for_state(state: str) -> Dict:
    dataframe = vax_registration_state_parser.csv().tail(16)
    matching = dataframe[dataframe['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}

@app.get('/registration/state/all/{date}')
async def get_registration_data_state(date: str) -> Dict:
    dataframe = vax_registration_state_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}

@app.get('/registration/state/{state}/{date}')
async def get_registration_data_state(state: str, date: str) -> Dict:
    dataframe = vax_registration_state_parser.csv()
    matching = dataframe[dataframe['date'] == date]
    matching = matching[matching['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}
#endregion

#region Vaccination statistics
@app.get('/vaccination/state')
@app.get('/vaccination/state/all/latest')
async def get_latest_vax_data_state() -> Dict:
    return vax_state_parser.csv().tail(16).to_dict('records')

@app.get('/vaccination/state/{state}/latest')
async def get_latest_vax_data_for_state(state: str) -> Dict:
    dataframe = vax_state_parser.csv().tail(16)
    matching = dataframe[dataframe['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}

@app.get('/vaccination/state/all/{date}')
async def get_vax_data_state(date: str) -> Dict:
    dataframe = vax_state_parser.csv()
    matching = dataframe[dataframe['date'] == date].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}

@app.get('/vaccination/state/{state}/{date}')
async def get_vax_data_state(state: str, date: str) -> Dict:
    dataframe = vax_state_parser.csv()
    matching = dataframe[dataframe['date'] == date]
    matching = matching[matching['state'] == state].to_dict('records')

    if len(matching):
        return matching
    else:
        return {}
#endregion
#endregion
