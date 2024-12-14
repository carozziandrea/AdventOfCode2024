class Robot:
    def __init__(self, current, velocity):
        self.current = current
        self.velocity = velocity

    def getCurrentPosition(self):
        return self.current
    
    def getVelocity(self):
        return self.velocity
    
    def setCurrentPosition(self, new):
        self.current = new


