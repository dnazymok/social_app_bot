import random

from core.models import User, Post, Like


class LikesGeneratorService:
    def __init__(self, users: [User], max_likes: int):
        self._users = users
        self._max_likes = max_likes

    def start(self) -> None:
        all_posts = self._get_posts_from_users(self._users)
        users_by_posts_count = self._sort_users_by_posts_count(self._users)

        for user in users_by_posts_count:
            users_with_zero_liked_post = self._get_users_with_zero_liked_post(
                self._users)
            if users_with_zero_liked_post:
                self._start_user_like_process(
                    user,
                    users_with_zero_liked_post,
                    all_posts
                )

    def _get_posts_from_users(self, users: [User]) -> [Post]:
        posts = []
        for user in users:
            for post in user.posts:
                posts.append(post)
        return posts

    def _sort_users_by_posts_count(self, users: [User]) -> [User]:
        return sorted(users, key=lambda user: user.posts_count, reverse=True)

    def _get_users_with_zero_liked_post(self, users: [User]) -> [User]:
        users_with_zero_liked_post = []
        for user in users:
            if user.is_zero_liked_post:
                users_with_zero_liked_post.append(user)
        return users_with_zero_liked_post

    def _start_user_like_process(self, user, users_with_zero_liked_post,
                                 all_posts):
        if user in users_with_zero_liked_post:
            users_with_zero_liked_post.remove(user)
        posts_to_like = self._get_posts_from_users(
            users_with_zero_liked_post)
        for i in range(self._max_likes):
            if posts_to_like:
                self._like_post(user, posts_to_like, all_posts)

    def _like_post(self, user, posts_to_like, all_posts):
        post = random.choice(posts_to_like)
        response = user.api.like_post(post.id)
        if response.status_code == 201:
            self._append_like_to_post(user, all_posts, post)
        if post in posts_to_like:
            posts_to_like.remove(post)

    def _append_like_to_post(self, user, all_posts, post):
        self._get_post_by_id(all_posts, post.id)
        like = Like(user=user, post=post)
        post.likes.append(like)

    def _get_post_by_id(self, posts: [Post], _id: int) -> Post:
        for post in posts:
            if post.id == _id:
                return post
