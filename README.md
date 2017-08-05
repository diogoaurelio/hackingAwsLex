# Local Setup

### Local Requirements

- python3.6
- conda
- Setup permissions: setup secrets file so you can store passwords (without being commited in the source code of this repo) to authenticate to different services
- Run locally: test API on your local machine before deploying into AWS
- Deploy in AWS serverless fashion (aka Lambda + Gateway)

### Setup 2 virtual environments

We are using 2 virtual environments (to separate dependencies for web dev and backend), one for zappa deployment of web application (AWS lambda plus API Gateway) and another for bot application (AWS Lambda integrating with AWS Lex)

1) Create a virtual environment for the web application:
Usage:

```
cd <this-repo-root-directory>/web_app

virtualenv -p /usr/bin/python3.6 web_app_hacking_aws_lex
source web_app_hacking_aws_lex/bin/activate
pip install -r requirements.txt
```

This will create a new directory with packages in your current location (no problem if you are inside the repo directory IF you copy paste the commands, as it is gitignored).

We need to create a new virtual env now for the Flask App, so we need to "jump" outside of this virtual env.
To deactivate a this virtual environment, just do:
```
deactivate
```
Note: this does NOT remove it; just disables it from the current terminal environment. No worries :)

2) Create a virtual environment for the bot application:

```
cd <this-repo-root-directory>/web_app

virtualenv -p /usr/bin/python3.6 bot_app_hacking_aws_lex
source bot_app_hacking_aws_lex/bin/activate
pip install -r requirements.txt
```

#### To switch between different


 
 
Next time you open again a terminal window, you need to load this virtual environtment again - in other words, to activate it again:
```
>cd <this-repo-root-directory>
>source hacking_aws_lex/bin/activate
(hacking_aws_lex)>
```

In your terminal you should see now that the prompt has changed, pointing to the terminal session env:
```
(hacking_aws_lex)>
```
 

To completely remove this venv:
 
```
rm virtualenv hacking_aws_lex
```



### Django setup

The django app was initially started using [this page](https://edgarroman.github.io/zappa-django-guide/walk_core/)
You do NOT need to run this command anymore, we just write it for reference:
```
cd web_service
django-admin startproject app .
```

```
python manage.py runserver
```


### Setup Permissions



Change in secrets/secrets.py add the following:

```

```

### run locally

Note: make sure you have the virtualenv activated before running the following command.

To run the server, run the following line in the terminal:
```
python manage.py runserver
```
You can access the API in: localhost:8000

In case you want to change the port where the server runs, say for example to 5000:

```
python manage.py runserver 5000
```


#### Test via API launching an EMR cluster
##### Launch new EMR cluster

Via GET request:
```
```

Via POST request:
```
curl -X POST http://127.0.0.1:5000/
```



### Deploy on AWS serverless

This project uses [zappa](https://github.com/Miserlou/zappa) to setup/deploy server-less environment. 

Note: make sure you configure your ~/.aws/config file with the required credentials as described [here](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/).

To deploy on dev environment for the first time:
```
zappa deploy dev
```

To update dev environment:
```
zappa update dev
```


### FAQ

I try tu run locally the server, with: 

```
python manage.py runserver 5000
```

...but I get a:

```
    from slackclient import SlackClient
ImportError: No module named 'slackclient'
```

Make sure you dont forget to load the python virtual env, via this command:

```
>source hacking_aws_lex/bin/activate
```