class UsernameNotFound(Exception):
    """ Username not found in Instagram """

    def __str__(self):
        return "Username not found in Instagram"


class HashTagNotFound(Exception):
    """ Hashtag not found in Instagram """

    def __str__(self):
        return "Hashtag not found in Instagram"


class PostIdNotFound(Exception):
    """ Post id not found in Instagram """

    def __str__(self):
        return "Post id not found in Instagram"
