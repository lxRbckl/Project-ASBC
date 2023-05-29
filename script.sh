#! /bin/bash


sleep 60


# locate where executable is (which poetry) #
POETRY='/Library/Frameworks/Python.framework/Versions/3.8/bin/poetry'


# using path to executable execute the following #
$POETRY run python3 -c 'from frontend.layout import run; run()' &
$POETRY run python3 -c 'from backend.bot import run; run()'
