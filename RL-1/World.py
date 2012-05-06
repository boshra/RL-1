"""
Code by: Rober Boshra

Description: This is a basic module where an 
    environment is implemented for the RL application.
    It sees the world as either continuous or discrete.
    The coordinate system starts from bottom left where 
    (0,0) is. 
    
    The board has predetermined meanings which are:
        0 : Nothing is there. no penalty no reward
        1 : Unpassable wall
        2 : Goal
        3 : Punishment
    
Version 0.01: The continous part is left for the time
    being. Discrete world is being built.     

"""

class World:
    
    
    dirs = range(0,3)
    dirsLabel = ['Up', 'Right', 'Down', 'Left']
    
    def __init__(self,board, discrete = True, length= 5, width= 5, begin = [0,0]):
        if not discrete:
            print "Continuous module not complete!"
            exit
        self.discrete = discrete
        self.length = length
        self.width = width
        self.position = begin
        self.board = board
        
    def move(self, dir):
        if self.discrete:
            if dir is 0:
                if self.y == self.width or self.board[self.x][self.y+1] is 1:
                    print "Incorrect move"
                self.y += 1
            if dir is 1:
                if self.x == self.length or self.board[self.x+1][self.y] is 1:
                    print "Incorrect move"
                self.x += 1
            if dir is 2:
                if self.y == 0 or self.board[self.x][self.y-1] is 1:
                    print "Incorrect move"
                self.y -= 1
            if dir is 3:
                if self.x == 0 or self.board[self.x-1][self.y] is 1:
                    print "Incorrect move"
                self.x -= 1
        else:
            pass
        
    def setGoal(self, x, y):
        self.board[x][y] = 2
        
    def reset(self, begin = [0,0]):
        self.position = begin
    
                
        
            