#!/bin/bash
echo "run capstone"
. ~/workspace/venv/capstone/Scripts/activate

echo "install dependencies"
cd ~/workspace/CapstoneProject/
pip install -r requirements.txt

echo "start app"
cd ~/workspace/CapstoneProject
export FLASK_APP=api.py
export FLASK_ENV=development
flask run --reload
