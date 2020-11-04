#!/bin/bash
echo "run capstone"
. ~/workspace/venv/capstone/Scripts/activate

echo "install dependencies"
cd ~/workspace/CapstoneProject/
pip install -r requirements.txt

echo "export env vairable"
export AUTH0_DOMAIN='fullstackiam.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='movies'

echo "start app"
cd ~/workspace/CapstoneProject
python test_flask.py
