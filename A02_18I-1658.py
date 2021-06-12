import numpy as np
import sys
###################################
# Creating a class named NODE
###################################
class Node():
    def __init__(self, par, pos):
        self.parent = par
        self.position = pos
        self.f = 0 #Cost
    def __eq__(self, other):
                return self.position == other.position
###################################
# This function create a the maze
###################################
def createMaze():
       matrix = np.zeros((20,20))
       matrix = matrix.astype('int')
       matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
       [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0],
       [0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1],
       [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1],
       [0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1],
       [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
       [0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1],
       [0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1],
       [0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0],
       [0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1],
       [0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0],
       [1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1],
       [0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0],
       [0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0],
       [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
       return matrix
###################################
# This function displays the maze
###################################
def display(maze):
    for row in range(20):
      for column in range(20):
          print(maze[row][column],end=' ')
      print()    

#################################################################################################################
#                 Helper Functions
#################################################################################################################
def PathIsOpen(maze,row,col):
  if(maze[row][col]==1):
      return True
  if(maze[row][col]==0):
      return False   

def canMoveUp(row):
    if(row>0):
        return True
    else:
        return False     

def canMoveDown(row):
    if(row<19):
        return True
    else:
        return False 

def canMoveRight(col):
    if(col<19):
        return True
    else:
        return False

def canMoveLeft(col):
    if(col>0):
        return True
    else:
        return False                 
#######################################################################
#This function returns the list of reachable neigbours from currentNode
#######################################################################
def getNeighbours(maze,currentNodePosition, currentNode):
    neigbours = []
    row, column = currentNodePosition

    if(canMoveDown(row)):
        if(PathIsOpen(maze,row+1,column)):
             down = row+1, column
             neigbourNode = Node(currentNode, down)
             neigbours.append(neigbourNode)

    if(canMoveUp(row)):
        if(PathIsOpen(maze,row-1,column)):
             up = row-1, column
             neigbourNode = Node(currentNode, up)
             neigbours.append(neigbourNode)

    if(canMoveLeft(column)):
        if(PathIsOpen(maze,row,column-1)):
             left = row, column-1
             neigbourNode = Node(currentNode, left)
             neigbours.append(neigbourNode)  

    if(canMoveRight(column)):
        if(PathIsOpen(maze,row,column+1)):
             right = row, column+1
             neigbourNode = Node(currentNode, right)
             neigbours.append(neigbourNode)
    return neigbours    
####################################################################
# This function wiil calculate the Manhattan Distance and returns it
####################################################################
def manhattanDistance(current,destination):
     c1, c2 = current
     d1, d2 = destination
     d = abs(c1 - d1) + abs(c2-d2)
     return d
     
##################################################################################################################
#                 A* Algorithm Implementation
##################################################################################################################

def aStarAlgorithm(maze,source,destination):
    cost=0 
    closedList = []
    openList = []
    currentNode = Node(None, source)
    endNode   = Node(None, destination)
    currentNode.f=0
    endNode.f=0


    openList.append(currentNode)
    while openList:
        openList.sort(key = lambda x:x.f) #Sort the list so we have node with minimum cost on top
        currentNode = openList.pop(0)    #get the top most node which has minimum f
        closedList.append(currentNode)

        if currentNode == endNode:
            path = []
            temp = currentNode
            while temp is not None: #keep looping until or unless temp has none value
                path.append(currentNode.position)
                temp = temp.parent
            return path[::-1],cost    

        data =  getNeighbours(maze,currentNode.position,currentNode) #this fucntion returns a list of neighbours and each node has it's parent node data and it's postion
        cost+=1
        for tmp in data:  #iterating over the data of neigbours
            neighbours = Node(currentNode,tmp.position) #create a temporary node
            if neighbours in closedList:
                continue                 #if data has been already retrived do nothing
                 
            neighbours.f = currentNode.f + manhattanDistance(currentNode.position, endNode.position)
            openList.append(neighbours)




if __name__=="__main__":
    maze = createMaze()
    source = 14,0
    destination = 12,19
    display(maze)
    path, cost = aStarAlgorithm(maze,source,destination)
    print("#####################################################")
    print("Cost of A* Algorithm is = " + str(cost))
    print("#####################################################")
