import requests
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}

home_url = "https://instagram.com"
url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"


def check_username(username: str) -> bool:
    """
    Function check the username
    Available in Instagram or
    not

    >>> check_username("google")
    True
    >>> check_username("jdhfvisofh")
    False
    >>> check_username("github")
    True
    """

    with requests.session() as s:
        response = s.get(home_url)
        token = response.cookies["csrftoken"]
        headers["x-csrftoken"] = token
        data = requests.post(url, data={"username": username}, headers=headers).json()

        if "username" in data["errors"]:
            return True

        return False


def check_email(email_id: str) -> bool:
    """
    Function check the email id
    Available in Instagram or
    not

    """

    with requests.session() as s:
        response = s.get(home_url)
        token = response.cookies["csrftoken"]
        headers["x-csrftoken"] = token
        data = requests.post(url, data={"email": email_id}, headers=headers).json()
        if "email" in data["errors"]:
            return True

        return False


def suggest_username(query: str) -> list:
    """
    Function suggest the username for the
    Instagram Accounts by Instagram
    """

    with requests.session() as s:
        response = s.get(home_url)
        token = response.cookies["csrftoken"]
        headers["x-csrftoken"] = token
        data = requests.post(url, data={"email": query}, headers=headers).json()

        return data["username_suggestions"]
