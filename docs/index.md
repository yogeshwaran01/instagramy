<!-- headings -->

<h1 align="center"> Instagramy </h1>

<p align="center">Python Package for Instagram Without Any external dependencies</p>

<!-- Badges -->

<p align="center">
    <a href="https://pypi.org/project/instagramy/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/instagramy.svg"/>
    </a>
    <a href="https://pepy.tech/project/instagramy">
    <img alt="Downloads" src="https://pepy.tech/badge/instagramy"/>
    </a>
    <a href="https://github.com/yogeshwaran01/instagramy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/yogeshwaran01/instagramy"></a>
    <a href="https://github.com/yogeshwaran01/instagramy/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/yogeshwaran01/instagramy"></a>
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
Scrape Instagram Users Information, Posts Details, and Hashtags details. This Package scrapes the user's recent posts with some information like likes, comments, captions and etc. No external dependencies.
</p>

<!-- Features -->

## Features

- It scrapes most of the data of the Instagram user, Hashtags and Posts
- You can use this package with login or without login
- Download Instagram post and User profile picture
- Have some plugins for Data analysis
- No External dependencies
- Lightweight
- Easy to Use

<!-- Downloading Guides -->

## Download

### Installation

```bash

pip install instagramy

```

### Upgrade

```bash

pip install instagramy --upgrade

```

<!-- Usage -->

## Sample Usage

### Getting Session Id of Instrgram

For Login into Instagram via instagramy session id is required. No username or password is Needed. You must be login into Instagram via Browser to get session id

1. Login into Instagram in default webbrowser
2. Move to Developer option
3. Copy the sessionid
   - Move to storage and then to cookies and copy the sessionid (Firefox)
   - Move to Application and then to storage and then to cookies and copy the sessionid (Chrome)

**Note:** Check for session id frequently, It may be changed by Instagram

<img src="https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/sessionid.gif" alt="demo" width=100% height=100%>

### Instagram User details

Class `InstagramUser` scrape some of the information related to the user of the Instagram

```python
>>> from instagramy import InstagramUser

>>> session_id = "38566737751%3Ah7JpgePGAoLxJe%334"

>>> user = InstagramUser('google', sessionid=session_id)

>>> user.is_verified
True

>>> user.biography
'Google unfiltered—sometimes with filters.'

>>> user.user_data # More data about user as dict
```

<details><summary>Show all Properties</summary>
<p>

- biography
- connected_fb_page
- followed_by_viewer
- follows_viewer
- fullname
- has_blocked_viewer
- has_country_block
- has_requested_viewer
- is_blocked_by_viewer
- is_joined_recently
- is_private
- is_verified
- no_of_mutual_follower
- number_of_followers
- number_of_followings
- number_of_posts
- other_info
- posts
- posts_display_urls
- profile_picture_url
- requested_by_viewer
- restricted_by_viewer
- username
- website

</p>
</details>

`InstagramUser.user_data` has more data other than defined as `Properties`

### Instagram Hashtag details

Class `InstagramHashTag` scrape some of the information related to the hash-tag of the Instagram

you can also set your sessionid as env variable

```bash
$ export SESSION_ID="38566737751%3Ah7JpgePGAoLxJe%er40q"
```

```python
>>> import os

>>> from instagramy import InstagramHashTag

>>> session_id = os.environ.get("SESSION_ID")

>>> tag = InstagramHashtag('google', sessionid=session_id)

>>> tag.number_of_posts
9556876

>>> tag.tag_data # More data about hashtag as dict
```

<details><summary>Show all Properties</summary>
<p>

- number_of_posts
- posts_display_urls
- profile_pic_url
- tagname
- top_posts

</p>
</details>

`InstagramHashTag.tag_data` has more data other than defined as `Properties`

### Instagram Post details

Class `InstagramPost` scrape some of the information related to the particular post of Instagram. It takes the post id as the parameter. You can get the post id from the URL of the Instagram posts from the property of `InstagramUser.posts`. or `InstagramHagTag.top_posts`

```python
>>> from instagramy import InstagramPost

>>> session_id = "38566737751%3Ah7JpgePGAoLxJe%334"

>>> post = InstagramPost('CLGkNCoJkcM', sessionid=session_id)

>>> post.author
'ipadpograffiti'

>>> post.number_of_likes
1439

>>> post.post_data # More data about post as dict

```

<details><summary>Show all Properties</summary>
<p>

- author
- caption
- display_url
- get_json
- number_of_comments
- number_of_likes
- post_source
- type_of_post
- upload_time

</p>
</details>

`InstagramPost.post_data` has more data other than defined as `Properties`

### Plugins

Instagramy has some plugins for ease

#### Plugins for Data Analyzing

- analyze_users_popularity
- analyze_hashtags
- analyze_user_recent_posts

```python
>>> import pandas as pd
>>> from instagramy.plugins.analysis import analyze_users_popularity

>>> session_id = "38566737751%3Ah7JpgePGAoLxJe%334"

>>> teams = ["chennaiipl", "mumbaiindians",
        "royalchallengersbangalore", "kkriders",
        "delhicapitals", "sunrisershyd",
        "kxipofficial"]
>>> data = analyze_users_popularity(teams, session_id)
>>> pd.Dataframe(data)

                   Usernames  Followers  Following  Posts
0                 chennaiipl    6189292        194   5646
1              mumbaiindians    6244961        124  12117
2  royalchallengersbangalore    5430018         59   8252
3                   kkriders    2204739         68   7991
4              delhicapitals    2097515         75   9522
5               sunrisershyd    2053824         70   6227
6               kxipofficial    1884241         67   7496
```

#### Plugins for Downloading Posts

- download_hashtags_posts
- download_post
- download_profile_pic

```python
>>> import os

>>> from instagramy.plugins.download import *

>>> session_id = os.environ.get('SESSION_ID')

>>> download_profile_pic(username='google', sessionid=session_id, filepath='google.png')

>>> download_post(id="ipadpograffiti", sessionid=session_id, filepath='post.mp4')

>>> download_hashtags_posts(tag="tamil", session_id=session_id, count=2)
```

### Use Without Login

You can use this package without login. Sessionid is not required but it may rise `RedirectionError` error after four to five requests.

```python
>>> from instagramy import *

>>> user = InstagramUser('google')
>>> user.fullname
'Google'
>>> tag = InstagramHashTag('python')
>>> tag.tag_data
```

## Sample Scripts

### 1) All Instagram data into Json File

This Script dump all data of the Instagram User, Tag and Post data in Json file

```python
import json
from instagramy import *

user = InstagramUser('github', sessionid="your_session%here")
tag = InstagramTag('python', sessionid="check_your_session_id_often")
post = InstagramPost("post_id_from_post_url", sessionid="os.getenv('SID')")

user_data = user.user_data
tag_data = tag.tag_data
post_data = post.post_data

# Dumping all data into respective files as Json

with open('github_user.json', 'w') as file:
    json.dump(user_data, file, indent=4)

with open('python_tag.json', 'w') as file:
    json.dump(user_data, file, indent=4)

with open('some_post.json', 'w') as file:
    json.dump(user_data, file, indent=4)

```

### 2) Visualization of Instagram User data

This Script analyze and visualize the Instagram users popularity.

Before running the script lets create the text file `accounts.txt` python required Instagram Users

```text
im_surya_jass__
sarv._.sa
_velu_shree_
__perumal__
...
```

Store this source as `instagram_viz.py`

```python
import sys

import matplotlib.pyplot as plt
import numpy as np
from instagramy import InstagramUser

try:
    filename = sys.argv[1]
except (IndexError, KeyError):
    print("List of username as textfile in arguement")

usernames = []
file = open(filename, "r")
for line in file:
    if line != "\n":
        usernames.append(str(line).strip())
followers = []
following = []
posts = []

for username in usernames:
    user = InstagramUser(username)
    followers.append(user.number_of_followers)
    following.append(user.number_of_followings)
    posts.append(user.number_of_posts)

x = np.arange(len(usernames))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + 0.2, followers, width, label="Followers")
rects2 = ax.bar(x, following, width, label="Following")
rects3 = ax.bar(x - 0.2, posts, width, label="Posts")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Popularity")
ax.yaxis.set_visible(False)
ax.set_title("Username")
ax.set_xticks(x)
ax.set_xticklabels(usernames)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            "{}".format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()
plt.show()
```

Lets run the script,

```bash
python3 instagram_viz.py accounts.txt
```

And here this the output

<img src="https://fun-web-projects.herokuapp.com/image/X-m5IfDbsys" alt="demo" width=100% height=100%>

You can do more stuff with this Package

<!-- Conclution -->

## ✏️ Important Notes

- You can use this package without sessionid (Login). But it may `RedirectionError` after four to five requests.
- class `Viewer` provide the data about currently logged in user.
- Check for session id frequently, It may be changed by Instagram
- If code execution is never gets completed, check and change your session id and try again.
- Don't provide the wrong session_id.
- `InstagramUser.user_data`, `InstagramPost.post_data` and `InstagramHashtag.tag_data` which is python `dict` has more and more data other than defined as `Properties`.
- This Package does not scrap all the posts from an account, the limit of the post only 12 (For non-private account)
- This Package not scrap all the posts of given hash-tag it only scrapes the top 60 - 72 posts.

## License

[MIT License](https://github.com/yogeshwaran01/instagramy/blob/master/LICENSE.txt)

## Contributions

Contributions are Welcome. Feel free to report bugs in [issue](https://github.com/yogeshwaran01/instagramy/issues) and fix some bugs by creating [pull requests](https://github.com/yogeshwaran01/instagramy/pulls). Comments, Suggestions, Improvements and Enhancements are always welcome. Let disscuss about it [Here](https://github.com/yogeshwaran01/instagramy/discussions/9).

<h3 align="center"> Made with Python ❤️ </h3>
