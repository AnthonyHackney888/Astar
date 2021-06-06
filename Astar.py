import tkinter as tk
class Node():

    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0 #cost of path
        self.f = 0 #estimated cose
        self.h = 0 # lowest cost
    def __eq__(self, value):
        return self.position == value.position

def astar(maze,start,end):
    #need a null value
    value = None
    #init both open and closed lists
    openL = []
    closedL = []

    #add the start node

    startNode = Node(value, start)
    startNode.g = startNode.f = startNode.h =0
    endNode = Node(value,end)
    endNode.g = endNode.f = endNode.h =0

    openL.append(startNode)
    #loop though until empty and openL is not empty
    while len(openL) > 0:
        #obtain current node
        currNode = openL[0]
        currIndex = 0
        for i, item in enumerate(openL):
            if item.h < currNode.h:
                currNode = item
                currIndex = i
        #pop off the current node

        openL.pop(currIndex)
        closedL.append(currNode)

        #found the goal
        if currNode == endNode:
            path = []
            curr = currNode
            while curr is not None:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1] #get the reversed path

        child = []
        for newPosition in [(0,-1), (0,1), 
                            (-1,0),(-1,-1),
                            (-1,1),(1,-1),(1,1)]:
            nodePostion =(currNode.position[0] + newPosition[0],currNode.position[1] + newPosition[1])

            if nodePostion[0]>(len(maze)-1) or nodePostion[0] < 0 or nodePostion[1] > (len(maze[len(maze)-1])-1) or nodePostion[1] < 0:
                continue
            if maze[nodePostion[0]][nodePostion[1]] !=0:
                continue
            #create a new node
            newNode = Node(currNode,nodePostion)

            #append node
            child.append(newNode)

        for c in child:
            for closedChild in closedL:
                if c == closedChild:
                    continue
            c.g = currNode.g +1
            c.f = ((c.position[0] - endNode.position[0])**2)+((c.position[1] - endNode.position[1])**2) 
            c.h = c.g+c.f

            for openNode in openL:
                if c == openNode and c.g > openNode.g:
                    continue
            openL.append(c)

           
def main():

   
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    start = (0,0)
    end = (7,6)
    path = astar(maze,start,end)
    print(path) 

   


  
if __name__ =='__main__':
    main()
