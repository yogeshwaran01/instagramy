<!-- headings -->

<h1 align="center"> Instagramy </h1>
<p align="center"> <img alt="Instagramy Logo" src="https://fun-web-projects.herokuapp.com/image/_q5ukAE4Vww"/> </p>

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
    <a href="https://github.com/yogeshwaran01/instagramy/actions/workflows/python-publish.yml"><img alt="GitHub Actions" src="https://github.com/yogeshwaran01/instagramy/workflows/Upload%20Python%20Package/badge.svg"></a>
    <a href="https://github.com/yogeshwaran01/instagramy/actions/workflows/python-package.yml"><img alt="GitHub Actions" src="https://github.com/yogeshwaran01/instagramy/workflows/Python%20package/badge.svg"></a>

</p>

</hr>

<p align="center">
Scrape Instagram Users Information, Posts data, Hashtags and Locations data. This Package scrapes the user's recent posts with some information like likes, comments, captions and etc. No external dependencies.
</p>

<!-- Features -->

## Features

- It scrapes most of the data of [Instagram user](#Instagram-User-details), [hastags](#Instagram-Hashtag-details), [Posts](#Instagram-Post-details) and [Location](#Instagram-Location-details)
- You can use this package [with login](#Sample-Usage) or [without login](#Use-Without-Login)
- Download [Instagram post](#Plugins-for-Downloading-Posts) and [User profile picture](#Plugins-for-Downloading-Posts)
- Have some [plugins](#Plugins) for Data analysis
- No External dependencies
- Having [caching Function](#Caching-Feature)
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

<img src="https://raw.githubusercontent.com/yogeshwaran01/instagramy/master/samples/sessionid.gif" width=100% height=100%>

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

If you get the data of the user onetime, instagramy store the data as cache file for avoid the error. you can get the data from cache also. Don't provide the sessionid.

```python
>>> from instagramy import InstagramUser

>>> user = InstagramUser('google', from_cache=True)

>>> user.is_verified
True
```

It is opt of all classes `InstagramUser`, `InstagramHashTag` and `InstagramPost`.

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
- text
- type_of_post
- upload_time

</p>
</details>

`InstagramPost.post_data` has more data other than defined as `Properties`

### Instagram Location details

Class `InstagramLocation` scrape some of the information and posts related to the given Location . It takes the location id and slug as the parameter. You can get the location id and slug from the URL of the Instagram Location or from the property of `InstagramPost.location.id` and `InstagramPost.location.slug`.

```python
>>> from instagramy import InstagramPost

>>> session_id = "38566737751%3Ah7JpgePGAoLxJe%334"

>>> post = InstagramPost('CLGkNCoJkcM', sessionid=session_id)

>>> location_id, slug = post.location.id, post.location.slug

>>> from Instagramy import InstagramLocation

>>> location = InstagramLocation(location_id, slug, session_id)

>>> location.latitude
28.6139

>>> location.longitude
77.2089

>>> location.address
{'street_address': 'T2, Indira Gandhi International Airport', 'zip_code': '', 'city_name': 'New Delhi', 'region_name': '', 'country_code': 'IN', 'exact_city_match': False, 'exact_region_match': False, 'exact_country_match': False}
```

you can also get the location id and slug from the instagram url

```url
https://www.instagram.com/explore/locations/977862530/mrc-nagar
https://www.instagram.com/explore/locations/<location_id>/<slug>
```

<details><summary>Show all Properties</summary>
<p>

- address
- id
- latitude
- location_data
- longitude
- name
- number_of_posts
- phone
- profile_pic_url
- sessionid
- slug
- top_posts
- url
- viewer
- website

</p>
</details>

`InstagramLocation.location_data` has more data other than defined as `Properties`

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

### Caching Feature

from version `4.3`, Added the new feature that is caching the required data. If you get the data of the user onetime, instagramy store the data as cache json file for avoid the error. you can get the data from cache also. Don't need to provide the sessionid. Instead of sessionid add the optional parameter `from_cache=True`.

```python
>>> from instagramy import InstagramUser

>>> user = InstagramUser('google', from_cache=True)

>>> user.is_verified
True
```

It is opt of all classes `InstagramUser`, `InstagramHashTag`, `InstagramPost` and `InstagramLocation`.

Clear all Caches created by instagramy in current dir by

```python
>>> from instagramy.core.cache import clear_caches

>>> clear_caches() # clear all caches of instagramy

```

List of all Cache files created by instagramy in current dir

```python
>>> from instagramy import list_caches

>>> list_caches() # list all caches of instagramy
```

## Sample Scripts

You can get some Sample scripts [Here](https://yogeshwaran01.herokuapp.com/post/Instagramy-Python-Package-for-Instagram)

## ✏️ Important Notes

- Don't send huge request to Instagram with sessionid, Instagram may ban you.
- You can use this package without sessionid (Login). But it may `RedirectionError` after four to five requests.
- class `Viewer` provide the data about currently logged in user.
- Check for session id frequently, It may be changed by Instagram
- If code execution is never gets completed, check and change your session id and try again.
- Don't provide the wrong session_id.
- `InstagramUser.user_data`, `InstagramPost.post_data`, `InstagramHashtag.tag_data` and `InstagramLocation.location_data` which is python `dict` has more and more data other than defined as `Properties`.
- This Package does not scrap all the posts from an account, the limit of the post only 12 (For non-private account)
- This Package not scrap all the posts of given hash-tag and location it only scrapes the top 60 - 72 posts.

<!-- Conclution -->

## Disclaimer

If you send the huge request to the Instagram with session id Instagram may ban you. I am not responsible for any misuse or damage caused by this program.

## License

[MIT License](https://github.com/yogeshwaran01/instagramy/blob/master/LICENSE.txt)

## Contributions

Contributions are Welcome. Feel free to report bugs in [issue](https://github.com/yogeshwaran01/instagramy/issues) and fix some bugs by creating [pull requests](https://github.com/yogeshwaran01/instagramy/pulls). Comments, Suggestions, Improvements and Enhancements are always welcome. Let disscuss about it [Here](https://github.com/yogeshwaran01/instagramy/discussions/9).

<h3 align="center"> Made with Python ❤️ </h3>
