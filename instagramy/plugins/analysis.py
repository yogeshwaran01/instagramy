from instagramy.InstagramUser import InstagramUser


def analyze_users(usernames: list) -> dict:
    followers = []
    following = []
    posts = []
    for username in usernames:
        user = InstagramUser(username, from_cache=True)
        followers.append(user.number_of_followers)
        following.append(user.number_of_followings)
        posts.append(user.number_of_posts)
    data = {
        "Usernames": usernames,
        "Followers": followers,
        "Followings": following,
        "Posts": posts,
    }
    return data


def analyze_user_recent_posts(username: str) -> dict:

    user = InstagramUser(username)
    posts = user.posts
    urls = []
    likes = []
    comments = []
    for post in posts:
        urls.append(post["post_url"])
        likes.append(post["likes"])
        comments.append(post["comments"])

    return {"Posts": urls, "Likes": likes, "Comments": comments}
