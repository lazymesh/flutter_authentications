# flutter_authentications
trying out flutter authentications

# frontends
## flutter
Sigin and Signup pages 

# backends
## express
start express server by `node index.js`

you need to create .env file with the following environmental variables
`MONGODB_USER=
MONGODB_PASSWORD=
MONGODB_URI=
MONGODB_CLUSTER=
MONGODB_DATABASE=`

## fastapi
create virtual environment to install the dependecies listed in libraries.txt file
`python3 -m venv .venv`
`source .venv/bin/activate`
`pip install -r libraries.txt`

uvicorn run is used in code so just run `python main.py` to run the fastapi server

you need to create .env file with the following environmental variables
`MONGODB_USER=
MONGODB_PASSWORD=
MONGODB_URI=
MONGODB_CLUSTER=
MONGODB_DATABASE=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=`
