# flask-dashboard-template

## Setup

### Repository Setup

Create new virtual environment:

```sh
conda create -n dashboard-env python=3.10
```

Activate the virtual environment:

```sh
conda activate dashboard-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

### AlphaVantage API Key

Obtain and AlphaVantage API Key and set it as the `ALPHAVANTAGE_API_KEY` environment variable (see configuration section below).


## Configuration

Create a new file called ".env" in the root directory of this local repository, and place inside contents like the following:


```sh
# this is the ".env" file...

# telling flask where our app is defined:
FLASK_APP="web_app"

# for interfacing with the AlphaVantage API:
ALPHAVANTAGE_API_KEY="________"
```

## Usage

Test the data fetching process:

```sh
python -m web_app.services.alpha
```

Run the web application (then view in the browser at localhost:5000):

```sh
flask run
```

## Testing

Running tests:

```sh
pytest
```
