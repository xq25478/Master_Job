#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
from typing import List
# @lc code=start
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post_stack = []#采用栈来存储推文
        self.user = {}#采用hash来保存用户数据

    def createId(self,useId):
        if useId not in self.user:
            self.user[useId] = []
            self.user[useId].append(useId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self.user[userId] = []
            self.user[userId].append(userId)#每个用户必须关注其自己
        self.post_stack.append((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            self.user[userId] = []
            self.user[userId].append(userId)
            return []

        res = []
        max_recently_posts = 10
        user = self.user[userId] #包含了该用户的关注列表
        for i in range(len(self.post_stack)-1,-1,-1):
            if self.post_stack[i][0] in user:
                res.append(self.post_stack[i][1])
                if len(res) == max_recently_posts:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.createId(followerId)
        self.createId(followeeId)

        if followerId == followeeId:
            return 

        if followeeId not in self.user[followerId]:
            self.user[followerId].append(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.createId(followerId)
        self.createId(followeeId)

        if followerId == followeeId:
            return 

        if followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

s = Twitter()
s.postTweet(1,5)
print(s.getNewsFeed(1))

s.follow(1,1)
print(s.getNewsFeed(1))