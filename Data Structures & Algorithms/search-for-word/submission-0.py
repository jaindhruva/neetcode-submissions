class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])
        found_word = False
        
        def dfs(i,j,word_index):
            if word_index == len(word):
                return True

            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                return False
            
            if board[i][j] == word[word_index]:
                
                visited.add((i,j))
                found_word = (dfs(i,j+1,word_index+1) or
                              dfs(i,j-1,word_index+1) or
                              dfs(i+1,j,word_index+1) or
                              dfs(i-1,j,word_index+1))
                visited.remove((i,j))
                return found_word




        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False