class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set)
        self.time = 0
        self.userTweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweetMap[userId].append([self.time, tweetId ])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get list of all users this user follows from followingmap
        userList = list(self.followingMap[userId])

        # add this user to that list
        userList.append(userId)

        # get all their tweets and dump them in a minheap or sort by -time
        minHeap = []
        for user in userList:
            for tweet in self.userTweetMap[user]:
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        # get the top 10
        res = []
        count = 0
        while minHeap and count < 10:
            res.append(heapq.heappop(minHeap)[1])
            count +=1
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)
        
