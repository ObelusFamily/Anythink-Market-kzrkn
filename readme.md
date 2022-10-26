# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

Open up a terminal. If you're on a mac, make sure docker.app is run. In general in terminal type ```docker -v ``` to check.

``` 
# git clone the repo
# cd to repo root folder
docker-compose up
```

Check the backend is running via: http://localhost:3000/api/ping. 

Check the frontend is working via: http://localhost:3001/register

Make an account, and if everything works, it works!

**[TODO 05/01/2018 @vanessa-cooper]:** _It's been a while since anyone ran a fresh copy of this repo. I think it's worth documenting the steps needed to install and run the repo on a new machine?_
