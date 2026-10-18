class FileSystem:

    def __init__(self):
        self.fileMap = {}
    
    def isValidPath(self, path):
        if path == '' or path == '/' or path in self.fileMap:
            return False
        dirs = path.split('/')
        dirs = dirs[1:(len(dirs)-1)]
        currPath = ""
        for dir in dirs:
            currPath += '/' + dir
            if currPath not in self.fileMap:
                return False
        return True


    def createPath(self, path: str, value: int) -> bool:
        if not self.isValidPath(path):
            return False
        self.fileMap[path] = value
        return True

    def get(self, path: str) -> int:
        return self.fileMap[path] if path in self.fileMap else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
