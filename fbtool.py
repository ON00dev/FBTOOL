import os
import sys
import time
import hashlib
import json
import requests
from getpass import getpass

def tool_main_function():
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mLogin Facebook \033[1;97m")
    print(50 * "-")
    print("\033[1;97m[☆] \033[1;92m1. Login")
    print("\033[1;97m[☆] \033[1;92m2. Settings")
    print("\033[1;97m[☆] \033[1;92m0. Exit")
    print(50 * "-")
    choice = input("\033[1;97m[☆] \033[1;92mChoose : \033[1;97m")
    if choice == "1":
        login()
    elif choice == "2":
        setting()
    elif choice == "0":
        sys.exit()
    else:
        tool_main_function()

def login():
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mLogin Facebook \033[1;97m")
    print(50 * "-")
    id = input("\033[1;97m[☆] \033[1;92mEmail/ID \033[1;91m: \033[1;97m")
    pwd = getpass("\033[1;97m[☆] \033[1;92mPassword \033[1;91m: \033[1;97m")
    try:
        os.mkdir('login')
    except OSError:
        pass
    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    q = json.loads(data.text)
    if 'access_token' in q:
        s = open('login.txt', 'w')
        s.write(q['access_token'])
        s.close()
        bot()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print("\033[1;91m[!] Login Failed. Account might be checkpointed.")
            time.sleep(1)
            tool_main_function()
        else:
            print("\033[1;91m[!] Login Failed. Email/ID or password may be wrong.")
            time.sleep(1)
            tool_main_function()

def bot():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92m1. Auto Comment")
    print("\033[1;97m[☆] \033[1;92m2. Auto Reaction")
    print("\033[1;97m[☆] \033[1;92m3. Comment on Group Post")
    print("\033[1;97m[☆] \033[1;92m4. React on Group Post")
    print("\033[1;97m[☆] \033[1;92m5. Accept Friend Requests")
    print("\033[1;97m[☆] \033[1;92m6. Comment on Group Post (Alt)")
    print("\033[1;97m[☆] \033[1;92m7. React on Group Post (Alt)")
    print("\033[1;97m[☆] \033[1;92m8. Group Friend Requests")
    print("\033[1;97m[☆] \033[1;92m0. Back")
    print(50 * "-")
    choice = input("\033[1;97m[☆] \033[1;92mChoose : \033[1;97m")
    if choice == "1":
        auto_comment()
    elif choice == "2":
        auto_reaction()
    elif choice == "3":
        ac_group()
    elif choice == "4":
        ar_group()
    elif choice == "5":
        auto_accept()
    elif choice == "6":
        auto_comment_group_post()
    elif choice == "7":
        auto_reaction_group_post()
    elif choice == "8":
        auto_group_friend_requests()
    elif choice == "0":
        tool_main_function()
    else:
        bot()

def auto_comment():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mAuto Comment")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    comment = input("\033[1;97m[☆] \033[1;92mYour Comment \033[1;91m: \033[1;97m")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idpost = i['id']
        requests.post('https://graph.facebook.com/' + idpost + '/comments?message=' + comment + '&access_token=' + toket)
        print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def auto_reaction():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mAuto Reaction")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print("\033[1;97m[☆] \033[1;92mReaction Type \033[1;97m")
    print("\033[1;97m[☆] \033[1;92m1. \033[1;97mLike")
    print("\033[1;97m[☆] \033[1;92m2. \033[1;97mLove")
    print("\033[1;97m[☆] \033[1;92m3. \033[1;97mWow")
    print("\033[1;97m[☆] \033[1;92m4. \033[1;97mHaha")
    print("\033[1;97m[☆] \033[1;92m5. \033[1;97mSad")
    print("\033[1;97m[☆] \033[1;92m6. \033[1;97mAngry")
    print(50 * "-")
    reaction_type = input("\033[1;97m[☆] \033[1;92mChoose \033[1;91m:\033[1;97m ")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idpost = i['id']
        if reaction_type == "1":
            reaction = "LIKE"
        elif reaction_type == "2":
            reaction = "LOVE"
        elif reaction_type == "3":
            reaction = "WOW"
        elif reaction_type == "4":
            reaction = "HAHA"
        elif reaction_type == "5":
            reaction = "SAD"
        elif reaction_type == "6":
            reaction = "ANGRY"
        requests.post('https://graph.facebook.com/' + idpost + '/reactions?type=' + reaction + '&access_token=' + toket)
        print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def ac_group():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mComment on Group Post")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    comment = input("\033[1;97m[☆] \033[1;92mYour Comment \033[1;91m:\033[1;97m ")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idg = i['id']
        r = requests.get('https://graph.facebook.com/v3.0/' + idg + '?fields=feed&access_token=' + toket)
        z = json.loads(r.text)
        for a in z['feed']['data']:
            idpost = a['id']
            requests.post('https://graph.facebook.com/' + idpost + '/comments?message=' + comment + '&access_token=' + toket)
            print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def ar_group():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mReact on Group Post")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print("\033[1;97m[☆] \033[1;92mReaction Type \033[1;97m")
    print("\033[1;97m[☆] \033[1;92m1. \033[1;97mLike")
    print("\033[1;97m[☆] \033[1;92m2. \033[1;97mLove")
    print("\033[1;97m[☆] \033[1;92m3. \033[1;97mWow")
    print("\033[1;97m[☆] \033[1;92m4. \033[1;97mHaha")
    print("\033[1;97m[☆] \033[1;92m5. \033[1;97mSad")
    print("\033[1;97m[☆] \033[1;92m6. \033[1;97mAngry")
    print(50 * "-")
    reaction_type = input("\033[1;97m[☆] \033[1;92mChoose \033[1;91m:\033[1;97m ")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idg = i['id']
        r = requests.get('https://graph.facebook.com/v3.0/' + idg + '?fields=feed&access_token=' + toket)
        z = json.loads(r.text)
        for a in z['feed']['data']:
            idpost = a['id']
            if reaction_type == "1":
                reaction = "LIKE"
            elif reaction_type == "2":
                reaction = "LOVE"
            elif reaction_type == "3":
                reaction = "WOW"
            elif reaction_type == "4":
                reaction = "HAHA"
            elif reaction_type == "5":
                reaction = "SAD"
            elif reaction_type == "6":
                reaction = "ANGRY"
            requests.post('https://graph.facebook.com/' + idpost + '/reactions?type=' + reaction + '&access_token=' + toket)
            print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def auto_accept():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mAuto Accept Friend Requests")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/friendrequests?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['from']['id']
        requests.post('https://graph.facebook.com/me/friends/' + uid + '?access_token=' + toket)
        print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + uid)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def auto_comment_group_post():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mAuto Comment on Group Posts")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    comment = input("\033[1;97m[☆] \033[1;92mYour Comment \033[1;91m: \033[1;97m")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idg = i['id']
        r = requests.get('https://graph.facebook.com/v3.0/' + idg + '?fields=feed&access_token=' + toket)
        z = json.loads(r.text)
        for a in z['feed']['data']:
            idpost = a['id']
            requests.post('https://graph.facebook.com/' + idpost + '/comments?message=' + comment + '&access_token=' + toket)
            print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def auto_reaction_group_post():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mAuto React on Group Posts")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print("\033[1;97m[☆] \033[1;92mReaction Type \033[1;97m")
    print("\033[1;97m[☆] \033[1;92m1. \033[1;97mLike")
    print("\033[1;97m[☆] \033[1;92m2. \033[1;97mLove")
    print("\033[1;97m[☆] \033[1;92m3. \033[1;97mWow")
    print("\033[1;97m[☆] \033[1;92m4. \033[1;97mHaha")
    print("\033[1;97m[☆] \033[1;92m5. \033[1;97mSad")
    print("\033[1;97m[☆] \033[1;92m6. \033[1;97mAngry")
    print(50 * "-")
    reaction_type = input("\033[1;97m[☆] \033[1;92mChoose \033[1;91m:\033[1;97m ")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idg = i['id']
        r = requests.get('https://graph.facebook.com/v3.0/' + idg + '?fields=feed&access_token=' + toket)
        z = json.loads(r.text)
        for a in z['feed']['data']:
            idpost = a['id']
            if reaction_type == "1":
                reaction = "LIKE"
            elif reaction_type == "2":
                reaction = "LOVE"
            elif reaction_type == "3":
                reaction = "WOW"
            elif reaction_type == "4":
                reaction = "HAHA"
            elif reaction_type == "5":
                reaction = "SAD"
            elif reaction_type == "6":
                reaction = "ANGRY"
            requests.post('https://graph.facebook.com/' + idpost + '/reactions?type=' + reaction + '&access_token=' + toket)
            print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + idpost)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def auto_group_friend_requests():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print("\033[1;91m[!] Token invalid")
        os.system('rm -rf login.txt')
        time.sleep(1)
        tool_main_function()
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mGroup Friend Requests")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print('\033[1;97m[☆] \033[1;92mStart...')
    print(50 * "-")
    r = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        idg = i['id']
        r = requests.get('https://graph.facebook.com/v3.0/' + idg + '?fields=members&access_token=' + toket)
        z = json.loads(r.text)
        for a in z['members']['data']:
            uid = a['id']
            requests.post('https://graph.facebook.com/me/friends/' + uid + '?access_token=' + toket)
            print('\033[1;97m[\033[1;92m✓\033[1;97m] ' + uid)
    print(50 * "-")
    input('\n\033[1;97m[Press Enter To Go Back]')
    bot()

def setting():
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mSettings")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    print("\033[1;97m[☆] \033[1;92m1. Set user-agent")
    print("\033[1;97m[☆] \033[1;92m2. Set account name")
    print("\033[1;97m[☆] \033[1;92m0. Back")
    print(50 * "-")
    choice = input("\033[1;97m[☆] \033[1;92mChoose : \033[1;91m: \033[1;97m")
    if choice == "1":
        user_agent()
    elif choice == "2":
        account_name()
    elif choice == "0":
        tool_main_function()
    else:
        setting()

def user_agent():
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mSet User-Agent")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    agent = input("\033[1;97m[☆] \033[1;92mUser-Agent \033[1;91m: \033[1;97m")
    if not os.path.exists('user-agent.txt'):
        with open('user-agent.txt', 'w') as f:
            f.write(agent)
    else:
        with open('user-agent.txt', 'w') as f:
            f.write(agent)
    print("\033[1;92m[✓] User-Agent set successfully!")
    time.sleep(1)
    setting()

def account_name():
    os.system('clear')
    print(logo)
    print("\033[1;97m[☆] \033[1;92mSet Account Name")
    print("\033[1;97m[☆] \033[1;91mPress Enter To Back")
    print(50 * "-")
    name = input("\033[1;97m[☆] \033[1;92mAccount Name \033[1;91m: \033[1;97m")
    if not os.path.exists('account-name.txt'):
        with open('account-name.txt', 'w') as f:
            f.write(name)
    else:
        with open('account-name.txt', 'w') as f:
            f.write(name)
    print("\033[1;92m[✓] Account name set successfully!")
    time.sleep(1)
    setting()

if __name__ == '__main__':
    logo = """
\n
\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m
│   ▄▄▄▄▄▄                      █                    █        │\033[1;91m
│   █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄    │\033[1;91m
│   █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀     │\033[1;91m
│   █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█      │\033[1;91m
│   █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄    │\033[1;91m
│                                                             │\033[1;91m
└─────────────────────────────────────────────────────────────┘\033[1;91m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mTeam    \033[1;91m: \033[1;96mAnonySphinx Philippines \033[1;97m                         ║
\033[1;97m║\033[1;93m* \033[1;97mRecode  \033[1;91m: \033[1;96mVictor O. Nascimento \033[1;97m                            ║
\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/VictorON00/FBTOOL\033[1;97m             ║
\033[1;97m║\033[1;93m* \033[1;97mCredits \033[1;91m: \033[1;96m[AQUI É O BRASIL] [Jair Messias Bolsonaro] \033[1;97m      ║
\033[1;97m║\033[1;93m* \033[1;97mNotice \033[1;91m : \033[1;96mThis is not my own work, i just recoded it. \033[1;97m     ║
\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4m1.1.0 (Adapted to Python3)\033[0m               \033[1;97m        ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""

    tool_main_function()
