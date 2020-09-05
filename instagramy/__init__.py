import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def html_1(soup):
    scripts = soup.find_all('script')
    main_scripts = scripts[4]
    data = main_scripts.contents[0]
    info_object = data[data.find('{"config"'): -1]
    info = json.loads(info_object)
    info = info['entry_data']['ProfilePage'][0]['graphql']['user']
    return info


def html_2(soup):
    scripts = soup.find_all('script')
    main_scripts = scripts[3]
    data = main_scripts.contents[0]
    info_object = data[data.find('{"config"'): -1]
    info = json.loads(info_object)
    info = info['entry_data']['ProfilePage'][0]['graphql']['user']
    return info


class Instagram(object):

    def __init__(self, username):
        self.username = username
        self.url = "https://www.instagram.com/{}/".format(username)

    def soup(self):
        html = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup

    def data(self):
        try:
            info = html_1(self.soup())
            return info
        except:
            info = html_2(self.soup())
            return info

    def get_followers(self):
        info = self.data()
        followers = info['edge_followed_by']['count']
        return followers

    def get_followings(self):
        info = self.data()
        following = info['edge_follow']['count']
        return following

    def get_posts(self):
        info = self.data()
        posts = info['edge_owner_to_timeline_media']['count']
        return posts

    def get_biography(self):
        info = self.data()
        bio = info['biography']
        return bio

    def get_fullname(self):
        info = self.data()
        fullname = info['full_name']
        return fullname

    def get_username(self):
        info = self.data()
        username = info['username']
        return username

    def get_profile_pic(self):
        info = self.data()
        pic = info['profile_pic_url_hd']
        return pic

    def get_posts_details(self):
        final_lists = []
        info = self.data()
        posts_details = info["edge_owner_to_timeline_media"]["edges"]
        for i in posts_details:
            data = {}
            try:
                data["url"] = i['node']["display_url"]
            except:
                data["url"] = None
            try:
                data["likes"] = i['node']["edge_liked_by"]["count"]
            except:
                data["likes"] = None
            try:
                data["comment"] = i['node']["edge_media_to_comment"]["count"]
            except:
                data["comment"] = None
            try:
                data["caption"] = i['node']['accessibility_caption']
            except:
                data["caption"] = None
            try:
                data["is_video"] = i['node']["is_video"]
            except:
                data["is_video"] = None
            try:
                data["timestamp"] = i['node']["taken_at_timestamp"]
            except:
                data["timestamp"] = None
            try:
                data["location"] = i['node']["location"]
            except:
                data["location"] = None
            final_lists.append(data)
        return final_lists

    def get_posts_links(self):
        post_links = []
        a = self.get_posts_details()
        for i in a:
            post_links.append(i["url"])
        return post_links

    def popularity(self):
        final = {"followers": self.get_followers(),
                 "following": self.get_followings(),
                 "posts": self.get_posts()}
        return final

