# Deploying to Render

Follow this guide if you would like to deploy your host your application on a free server provided by the Render platform.

References:
  + https://render.com/docs/deploy-flask

## Render Setup

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service". Choose your own repository by specifying its public URL.

Specify start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Under the "Advanced" options, set the following environment variable (specifying your own API Key value):

```sh
ALPHAVANTAGE_API_KEY="________"
```
