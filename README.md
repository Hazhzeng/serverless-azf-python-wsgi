### Azure Functions

Refer to [Serverless docs](https://serverless.com/framework/docs/providers/azure/guide/intro/) for more information.

### How to start

1. Create a virtual environment
    - Windows: `py -m venv env ; env\Scripts\Activate.ps1 ; pip install -r requirements.txt`
    - Linux: `python3 -m venv env && source env\bin\activate && pip install -r requirements.txt`
1. Get the serverless framework [here](https://serverless.com/framework/docs/getting-started/)
2. Run `npm install` to resolve packages
3. Run `sls offline` to start debugging server on your local devbox
4. Make a GET request to http://localhost:7071/

### How to deploy

1. Change **service** field in **serverless.yml** to change the destination function app name
2. Set an environment variable **AZURE_SUBSCRIPTION_ID**, (e.g. AZURE_SUBSCRIPTION_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee")
3. Run `sls deploy` to deploy your local function app onto azure
4. Now we can use GET requests to access the Flask app on Azure Functions http://appname.azurewebsites.net
