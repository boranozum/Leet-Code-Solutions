from typing import List


class Twitter:

    def __init__(self):

        self.follow_map = [[False for i in range(501)] for j in range(501)]
        self.all_posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_posts = [(userId, tweetId)] + self.all_posts

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for post in self.all_posts:
            if self.follow_map[userId][post[0]] or userId == post[0]:
                feed.append(post[1])
                if len(feed) == 10:
                    break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId][followeeId] = False

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)