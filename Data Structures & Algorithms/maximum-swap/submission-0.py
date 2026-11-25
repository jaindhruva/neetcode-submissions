class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        for i in range(len(num_str)):
            n = int(num_str[i])
            # find max number after this and swap it
            max_after_n = n
            max_index = i
            for j in range(i+1, len(num_str)):
                n2 = int(num_str[j])
                if n2 >= max_after_n:
                    max_after_n = n2
                    max_index = j
            if max_after_n > n:
                res = list(str(num))
                res[max_index] = str(n)
                res[i] = str(max_after_n)
                return int("".join(res))
        return num
