#! /bin/bash


poetry run python3 -c 'from frontend.layout import run; run()' &
poetry run python3 -c 'from backend.bot import run; run()'
