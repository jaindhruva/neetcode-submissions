class Solution:
    def compress(self, chars: List[str]) -> int:
        charIndex = 0
        n = len(chars)
        i = 0
        while i < n:
            curr = chars[i]
            count = 0
            while i < n and chars[i] == curr:
                i += 1
                count += 1
            chars[charIndex] = curr
            charIndex += 1
            if count == 1:
                continue
            for c in str(count):
                if charIndex == n:
                    break
                chars[charIndex] = c
                charIndex += 1

        return charIndex

