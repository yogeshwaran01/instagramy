""" Random Headers for webscraping """

import random


# User-Agents for Web-Scraping
user_agents = [
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Googlebot/2.1 (+http://www.googlebot.com/bot.html)",
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
]

headers = {"User-Agent": f"user-agent: {random.choice(user_agents)}"}
