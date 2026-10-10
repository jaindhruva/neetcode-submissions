class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        startingColor = image[sr][sc]
        m, n = len(image), len(image[0])

        q.append((sr,sc))

        while q:
            r,c = q.popleft()
            if r<0 or r>=m or c<0 or c>=n or image[r][c]==color or image[r][c]!=startingColor :
                continue
            image[r][c] = color
            q.append((r+1,c))
            q.append((r-1,c))
            q.append((r,c+1))
            q.append((r,c-1))

        return image
