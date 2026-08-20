# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.








# Brute force:
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        all_tweets = []

        # User ke khud ke tweets
        if userId in self.tweets:
            all_tweets.extend(self.tweets[userId])

        # Follow kiye hue users ke tweets
        for followee in self.following.get(userId, set()):
            if followee in self.tweets:
                all_tweets.extend(self.tweets[followee])

        # Latest tweets first
        all_tweets.sort(reverse=True)

        # Sirf latest 10
        return [tweetId for time, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)








# Optimal:
import heapq


class Twitter:

    def __init__(self):
        self.time = 0

        # userId -> list of (time, tweetId)
        self.tweets = {}

        # followerId -> set of followeeIds
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []

        # User khud ko bhi follow karta hua consider karo
        users = self.following.get(userId, set()).copy()
        users.add(userId)

        # Har relevant user ka latest tweet heap mein daalo
        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        result = []

        # Maximum 10 tweets
        while heap and len(result) < 10:

            neg_time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            # Isi user ka previous tweet
            if index > 0:
                prev_time, prev_tweetId = self.tweets[uid][index - 1]

                heapq.heappush(
                    heap,
                    (-prev_time, prev_tweetId, uid, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)