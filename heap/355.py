import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.user_folowees = defaultdict(set)
        self.user_feeds = defaultdict(list)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_count += 1

        if len(self.user_feeds[userId]) == 10:
            self.user_feeds[userId].pop(0)

        self.user_feeds[userId].append((self.tweet_count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for uid in list(self.user_folowees[userId]) + [userId]:
            feed = heapq.nlargest(10, feed + self.user_feeds[uid], key=lambda x: x[0])

        return [x[1] for x in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_folowees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_folowees[followerId]:
            self.user_folowees[followerId].remove(followeeId)
