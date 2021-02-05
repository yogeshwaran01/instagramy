<h1 align="center"> Instagramy </h1>

<p align="center">Python Package for Instagram Without Any external dependencies</p>

<ul>
</ul>

<p align="center">
    <a href="https://pypi.org/project/instagramy/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/instagramy.svg"/>
    </a>
    <a href="https://pepy.tech/project/instagramy">
    <img alt="Downloads" src="https://pepy.tech/badge/instagramy"/>
    </a>
    <a href="https://github.com/yogeshwaran01/instagramy/blob/master/LICENSE.txt">
    <img alt="GitHub license" src="https://img.shields.io/github/license/yogeshwaran01/instagramy?color=blue"/>
    </a>
    <a href="https://github.com/psf/black">
    <img alt="Code style" src="https://img.shields.io/badge/codestyle-Black-blue"/>
    </a>
    <img alt="GitHub Repo size" src="https://img.shields.io/github/repo-size/yogeshwaran01/instagramy"/>
    <img alt="Actions" src="https://github.com/yogeshwaran01/instagramy/workflows/Python%20package/badge.svg"/>
    <img alt="Actions" src="https://github.com/yogeshwaran01/instagramy/workflows/Upload%20Python%20Package/badge.svg"/>
</p>

</hr>

<p align="center">
Scrape Instagram Users Informations, Posts Details, and Hashtags details. This Package scrapes the user's recent posts with some information like likes, comments, captions and etc. No login required and any dependencies.
</p>

## Download

### Installation

```bash

pip install instagramy

```

### Upgrade

```bash

pip install --upgrade instagramy

```
## Usage

### Instagram User details

Class `InstagramUser` scrape some of the information related to the user of the Instagram

#### Properties

- biography
- fullname
- is_private
- is_verified
- number_of_followers
- number_of_followings
- number_of_posts
- other_info
- posts
- posts_display_urls
- profile_picture_url
- username
- website

<img src="https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/user.png" width=100% height=100%>

### Instagram Hashtag details

Class `InstagramHashTag`  scrape some of the information related to the hash-tag of the Instagram

#### Properties

- number_of_posts
- posts_display_urls
- profile_pic_url
- tagname
- top_posts

<img src="https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/hashtag.png" width=100% height=100%>

### Instagram Post details

Class `InstagramPost`  scrape some of the information related to the particular post of Instagram. It takes the post id as the parameter. You can get the post id from the URL of the Instagram posts from the property of `InstagramUser.posts`. or `InstagramHagTag.top_posts`

#### Properties

- author
- caption
- description
- number_of_comments
- number_of_likes
- post_detail
- uploaded_date

<img src="https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/post.png" width=100% height=100%>

## Caching

From version 4.1 it does some caching process for avoid some errors. Due to caching the package may return old data of users or hashtags.
To avoid this just use agrument `from_cache=False` or delete the hidden folder `.instagramy_cache`

```python

from instagramy import InstagramUser

user = InstagramUser('github', from_cache=False)

```

## ⚠️ Note


- Don't send multiple requests, the Instagram redirects to the login page, If you send multiple requests, reboot your pc or change the IP or try after sometimes.
- This Package does not work in Remote PC or any Online python Interpreter.
- This Package does not scrap all the posts from an account, the limit of the post only 12 (For non-private account)
- This Package not scrap all the posts of given hash-tags it only scrapes the top 60 - 70 posts .


### Sample-Scripts

Some sample scripts based on this package

- [👦 Download Instagram DP](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instadp.py)

- [📊 Analysis Instagram Accounts with Matplotlib](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instalysis.py)

- [#️⃣ Bulk Instagram Hashtag Posts Download](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instagram_hastags_post.py)

<h3 align="center"> Made with Python ❤️ </h3>
