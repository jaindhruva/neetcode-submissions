class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        write, read = 0, 0
        n = len(prices)
        i = 0
        while True:
            print(write, read)
            if write >= n:
                break
            if read >= n:
                write += 1
                read = write + 1
                continue
            if read == write or prices[write] < prices[read] :
                # look at next price
                read += 1
                continue
            if prices[write] >= prices[read]:
                # found discount
                prices[write] = prices[write]-prices[read]
                write += 1
                read = write+1
            

        return prices
