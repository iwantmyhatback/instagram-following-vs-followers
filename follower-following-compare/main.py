import time
import os
from instabot import Bot
from getpass import getpass

# Formatting console output (colors)


class bcolors:
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

# Uncomment to reset cookie that causes username issues
#import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])


# Get user input for credentials
print("Enter Instagram Username, and then hit Enter: ")
userName = input()
print("Enter Instagram Password and then hit Enter: ")
userPass = getpass()

# Access instagram and get a list of followers and following
bot = Bot()
bot.login(username=userName, password=userPass)
time.sleep(1)
following = bot.following
time.sleep(1)
followers = bot.followers
time.sleep(1)

# Determine what users are in following list but not followers list
traitorNums = []
for i in following:
    if i not in followers:
        traitorNums.append(i)

# Translate user numbers into user names
traitorNames = []
for i in traitorNums:
    traitorNames.append(bot.get_username_from_user_id(i))

# Output the results
print(f"{bcolors.YELLOW}The following is a list of accounts that do not follow you back... {bcolors.ENDC}")
print(traitorNames)
