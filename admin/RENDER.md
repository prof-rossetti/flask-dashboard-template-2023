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

Finally, click to "Create" the web service.

## Render Deploys

Whenever you push new code to the desingated branch in your GitHub repository, it will trigger a new deployment to update your hosted site.

You can also trigger builds manually.
