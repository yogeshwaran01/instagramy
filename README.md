# instagramy

[![PyPI](https://img.shields.io/pypi/v/instagramy.svg)](https://pypi.org/project/instagramy/) [![Downloads](https://pepy.tech/badge/instagramy)](https://pepy.tech/project/instagramy)

Get Instagram users informations, posts details
and hash tag details
</br>

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

### Check Username is in Instagram

    >>> from instagramy import check_username

    >>> check_username("github")
    True
    >>> check_username("khwrhfg")
    False

### Check E-Mail used by any User of Instagram

    >>> from instagramy import check_email

    >>> check_email("google@gmail.com")
    True
    >>> check_email("example@hoo.com")
    False

### Suggest Username for Instagram

    >>> from instagramy import suggest_username

    >>> suggest_username("sample")
    ['sample5851', 'sample3923', 'sa.mple6820', 'sa.mple9538', 'sa.mple152', 'sa.mple2100']

### [Full Documentation](https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/instagramy-docs.ipynb)
