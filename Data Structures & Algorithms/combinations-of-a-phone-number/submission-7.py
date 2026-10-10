class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        for num in digits:
            if not res:
                res = list(numberToChar[num])
                continue
            resCopy = []
            for char in numberToChar[num]:
                for string in res:
                    resCopy.append(string+char)
            res = resCopy

        return res