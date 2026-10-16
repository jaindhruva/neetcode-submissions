class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.snake = deque()
        self.snake.append((0,0))
        self.snake_set = set()
        self.snake_set.add((0,0))
        self.dirs = {
            "L":[0,-1],
            "R":[0,1],
            "U":[-1,0],
            "D":[1,0]
        }


    def move(self, direction: str) -> int:
        dx, dy = self.dirs[direction]
        curr = self.snake[0]
        new_x, new_y = curr[0] + dx, curr[1] + dy
        if new_x < 0 or new_x >= self.height or new_y < 0 or new_y >= self.width :
            return -1

        # move snake
        self.snake.appendleft((new_x, new_y))
        
        
        if self.food_index < len(self.food) and [new_x,new_y] == self.food[self.food_index]:
            # if food eaten, go to next food index
            self.food_index += 1
        else:
            # if no food, pop tail
            tail_x, tail_y = self.snake.pop()
            self.snake_set.remove((tail_x, tail_y))
        
        if (new_x,new_y) in self.snake_set:
            return 
        self.snake_set.add((new_x, new_y))
        
        return len(self.snake_set)-1


        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
