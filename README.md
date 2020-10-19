# instagramy

[![PyPI](https://img.shields.io/pypi/v/instagramy.svg)](https://pypi.org/project/instagramy/)
</br>
Get Instagram users informations, posts details
and hash tag details

## Download

### Windows

`pip install instagramy`

### Linux

`pip3 install instagramy`

## Usage

### Instagram User details

    >>> from instagramy import InstagramUser

    >>> user = InstagramUser("github")
    >>> user.is_verified
    True
    >>> user.biography
    'Built for developers.'
    >>> user.number_of_followers
    121113
    >>> user.number_of_posts
    158

### Instagram Hashtag details

    >>> from instagramy import InstagramHashTag

    >>> hashtag = InstagramHashTag("python")
    >>> hashtag.number_of_posts
    3119668
    >>> len(hashtag.posts_url) # url of top posts as list
    68

### Instagram Post details

    >>> from instagramy import InstagramPost
        # Get post id from post url

    >>> post = InstagramPost("CGeYX2OA61s")
    >>> post.author
    '@virat.kohli'
    >>> post.number_of_likes
    2203830
    >>> post.number_of_comments
    4629

### [Full Documentation](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instagramy-docs.ipynb)
