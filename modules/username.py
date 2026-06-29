import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def check_github(username):
    url = f"https://github.com/{username}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return "FOUND"
    elif response.status_code == 404:
        return "NOT FOUND"
    else:
        return f"ERROR ({response.status_code})"


def check_reddit(username):
    url = f"https://www.reddit.com/user/{username}"

    response = requests.get(url, headers=HEADERS)

    # Reddit often returns 200 even for missing users
    if "Sorry, nobody on Reddit goes by that name." in response.text:
        return "NOT FOUND"
    elif response.status_code == 200:
        return "FOUND"
    else:
        return f"ERROR ({response.status_code})"


def check_gitlab(username):
    url = f"https://gitlab.com/{username}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return "FOUND"
    elif response.status_code == 404:
        return "NOT FOUND"
    else:
        return f"ERROR ({response.status_code})"


def check_hackerone(username):
    url = f"https://hackerone.com/{username}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return "FOUND"
    elif response.status_code == 404:
        return "NOT FOUND"
    else:
        return f"ERROR ({response.status_code})"