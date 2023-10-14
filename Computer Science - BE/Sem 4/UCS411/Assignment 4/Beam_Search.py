import copy
class Swapnil:
     def __init__(self, map):
          Swapnil.map=map
          self.currentNode=0
          self.goalNode=6
          self.heuristic=0
          self.visitedList=[]
          self.visitedList.append(self.currentNode)
          self.prevState=None

     def displayState(self):
          print("--------------------------------")
          print(f"Current node:{self.currentNode}     Visited nodes={self.visitedList}")

     def __gt__(self, other):
          return self.heuristic>other.heuristic

     def __lt__(self, other):
          return self.heuristic<other.heuristic

     def __eq__(self, other):
          return self.visitedList==other.visitedList

     def isGoalReached(self):
          if self.goalNode in self.visitedList:
               return True
          else:
               return False

     def move(self, node):
          if node!=self.currentNode and node not in self.visitedList and Swapnil.map[self.currentNode][node]!=-1:
               print(f"Moving from node {self.currentNode} to {node}")
               self.heuristic=Swapnil.map[self.currentNode][node]
               self.currentNode=node
               self.visitedList.append(self.currentNode)
               return True
          else:
               #print("Already visited")
               return False

     def possibleNextStates(self):
          stateList=[]
          for i in range(0, len(Swapnil.map[0])):
               state=copy.deepcopy(self)
               if state.move(i):
                    self.prevState=copy.deepcopy(self)
                    stateList.append(state)
          
          return stateList
               
def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BeamSearch(startState, beta):
     open=[]
     closed=[]
     flag=0
     B=beta

     open.append(startState)
     
     while(open):

          thisState=open.pop(0)
          thisState.displayState()

          if thisState not in closed:
               closed.append(thisState)

               if thisState.isGoalReached():
                    print("Goal state found.. stopping search")
                    constructPath(thisState)
                    flag=1
                    break

               nextStates=thisState.possibleNextStates()
               for eachState in nextStates:
                    open.append(eachState)
               
               open.sort()

               if len(open)>B:
                    while len(open)!=B:
                         open.pop()

     if flag!=1:
          print("Error, can't reach goal node")

map=[[-1,  1,  3, -1, -1, -1, -1], [-1, -1, -1,  2,  2, -1, -1],[-1, -1, -1, -1, -1,  3,  0], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1]]
beta=int(input("Enter B (2/3): "))
problem=Swapnil(map)
BeamSearch(problem, beta)