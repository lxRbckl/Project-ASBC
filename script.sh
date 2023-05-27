#! /bin/bash


nohup poetry run python3 -c 'from frontend.frontend import run; run()' &
nohup poetry run python3 -c 'from backend.bot import run; run()' &