# CITF FastAPI server

A REST API server written with FastAPI to parse vaccination data obtained from CITF Malaysia's [public repository](https://github.com/CITF-Malaysia/citf-public) to JSON-formatted data.

## Setting up

```bash
# Get the same Python version
pyenv install 3.9.0
pyenv global 3.9.0
git clone https://github.com/pongloongyeat/fastapi-vax-my.git && cd fastapi-vax-my

# Setup venv
pipenv shell
pipenv install

# Run server
uvicorn main:app
```

## Available APIs

| Route | Documentation |
|---|---|
| /<br>/help | Shows this help message. |
| /registration/malaysia<br>/registration/malaysia/latest | Returns the latest registration statistics for Malaysia. |
| /registration/malaysia/{date} | Returns the registration statistics for Malaysia during a certain date with format YYYY-MM-DD. |
| /vaccination/malaysia<br>/vaccination/malaysia/latest | Returns the latest vaccination statistics for Malaysia. |
| /vaccination/malaysia/{date} | Returns the vaccination statistics for Malaysia during a certain date with format YYYY-MM-DD. |
| /registration/state<br>/registration/state/all/latest | Returns the latest registration statistics for all states. |
| /registration/state/all/{date} | Returns the registration statistics for all states during a certain date with format YYYY-MM-DD. |
| /registration/state/{state}/latest | Returns the latest registration statistics for a specific state. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv). |
| /registration/state/{state}/{date} | Returns the registration statistics for a certain state during a certain date with format YYYY-MM-DD. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/registration/vaxreg_state.csv). |
| /vaccination/state<br>/vaccination/state/all/latest | Returns the latest vaccination statistics for all states. |
| /vaccination/state/all/{date} | Returns the vaccination statistics for all states during a certain date with format YYYY-MM-DD. |
| /vaccination/state/{state}/latest | Returns the latest vaccination statistics for a specific state. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/vaccination/vax_state.csv). |
| /vaccination/state/{state}/{date} | Returns the vaccination statistics for a certain state during a certain date with format YYYY-MM-DD. Note that this should follow the same naming scheme as that specified in the CITF repository (see https://github.com/CITF-Malaysia/citf-public/blob/main/vaccination/vax_state.csv). |
