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

### [More Info](https://github.com/yogeshwaran01/instagramy/blob/master/instagramy%20_documentation.ipynb)
