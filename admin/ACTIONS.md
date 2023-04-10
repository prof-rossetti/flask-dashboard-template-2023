
# Continuous Integration

This guide describes the process of configuring your repository to work with GitHub actions for Continuous Integration purposes.

## GitHub Actions Setup

The GitHub Actions CI build process is defined by the steps in the["python-app.yml" file](/.github/workflows/python-app.yml). The steps include checking code syntax and running automated tests, to determine if the app is working as desired.

Some of the tests make requests for stock data, in which case they need an AlphaVantage API Key. We'll set this credential in a secure encrypted way via the GitHub repository's secrets menu.

From the GitHub repository settings, under "Actions" menu, click to "Create new repository secret", then specify `ALPHAVANTAGE_API_KEY` as the "name" and your own key value (without quotes, like `abc123` ) as the "secret" value.
