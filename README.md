##instagram-following-vs-followers
---
Small Python3 CLI tool to compare a users followed accounts to the accounts who follow them. 
Takes in the Instagram Username and Passwork and returns a list of the accounts who do not follow back.
**The tool will not work if your account had 2FA (Two Factor Authentication) enabled**
---
###To run:
1. `cd` into the repository
2. run `python3 -m pip install --user pipenv` (if pipenv has not been previously installed)
3. run `pipenv install` to install dependencies
4. run `pipenv shell` to enter the virtual environment
5. run `pipenv run python3 follower-following-compare/main.py`
6. follow on screen instructions
