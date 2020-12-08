# Instagramy

[![PyPI](https://img.shields.io/pypi/v/instagramy.svg)](https://pypi.org/project/instagramy/) [![Downloads](https://pepy.tech/badge/instagramy)](https://pepy.tech/project/instagramy)
[![GitHub license](https://img.shields.io/github/license/yogeshwaran01/instagramy?style=plastic)](https://github.com/yogeshwaran01/instagramy/blob/master/LICENSE.txt)
[![Code style](https://img.shields.io/badge/codestyle-Black-blue)](https://github.com/psf/black)
![GitHub Repo size](https://img.shields.io/github/repo-size/yogeshwaran01/instagramy)

<hr>

Scrape Instagram Users Informations, Posts Details, and Hashtags details. This Package scrapes the user's recent posts with some information like likes, comment, caption and etc. No login required.


## Download

### Windows

`> pip install instagramy`

### Linux

`$ pip3 install instagramy`

## Usage

### Instagram User details
Class `InstagramUser` scrape some of the information related to the user of the Instagram

#### Properties
- biography
- email
- fullname
- is_private
- is_verified
- number_of_followers
- number_of_followings
-  number_of_posts
- other_info
- posts
-  posts_display_urls
- profile_picture_url
- username
- website

![user](https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/user.png)

### Instagram Hashtag details
Class `InstagramHashTag`  scrape some of the information related to the hash-tag of the Instagram

#### Properties
- number_of_posts
- posts_display_urls
- profile_pic_url
- tagname
- top_posts

![hashtag](https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/hashtag.png)

### Instagram Post details
Class `InstagramPost`  scrape some of the information related to the particular post of Instagram. It takes the post id as the parameter. You can get the post id from the URL of the Instagram posts from the property of `InstagramUser.posts`. or `InstagramHagTag.top_posts`

#### Properties

- author
- caption
- description
- number_of_comments
- number_of_likes
- post_detail

![Post](https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/post.png)

### Check Username is in Instagram
Function `check_username` checks the user is on Instagram or not

![check](https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/check.png)

### Suggest Username for Instagram
Function `suggest_username` suggests username for the  Instagram

![suggest](https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/suggest.png)

### Check E-Mail is in Instagram
Function `check_email` checks the email is on Instagram or not.

## Note
- This Package does not work in Remote PC or any Online python Interpreter
-  This Package not scrap all the posts from a certain account, limit of the posts only 12 ( For non-private account)
- This Package not scrap all the posts of certain hash-tags it only scrap the top 60 - 70 posts in certain hash-tags.

### Sample-Scripts

Some sample scripts based on this package

- [👦 Download Instagram DP](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instadp.py)

- [📊 Analysis Instagram Accounts with Matplotlib](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instalysis.py)

- [#️⃣ Bulk Instagram Hashtag Posts Download](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instagram_hastags_post.py)

