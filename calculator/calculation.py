class calculation:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def getOutput(self):
        # Call the stored operation with x and y
        return self.operation(self.x, self.y)

    
