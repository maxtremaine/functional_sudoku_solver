#!bin/sh
echo Running mypy:
python3 -m mypy .
echo Running unittest:
python3 -m unittest