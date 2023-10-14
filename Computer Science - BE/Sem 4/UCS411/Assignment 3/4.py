import copy

# c_ state => current


class puzzle:
    def __init__(self, initial, final):
        self.current_s = initial
        self.final = final
        self.blank_id = self.current_s.index(0)
        self.msg = " Invalid move"

    def up(self):
        if (self.blank_id > 2):
            t = self.current_s[self.blank_id]
            self.current_s[self.blank_id] = self.current_s[self.blank_id - 3]
            self.current_s[self.blank_id - 3] = t
            # self.display()
            self.blank_id = self.current_s.index(0)
            # self.goal_state()
            return True
        else:
            # print(self.msg)
            return False

    def down(self):
        if (self.blank_id < 6):
            t = self.current_s[self.blank_id]
            self.current_s[self.blank_id] = self.current_s[self.blank_id + 3]
            self.current_s[self.blank_id + 3] = t
            # self.display()
            self.blank_id = self.current_s.index(0)
            # self.goal_state()
            return True
        else:
            # print(self.msg)
            return False

    def left(self):
        if (self.blank_id % 3 != 0):
            t = self.current_s[self.blank_id]
            self.current_s[self.blank_id] = self.current_s[self.blank_id - 1]
            self.current_s[self.blank_id - 1] = t
            # self.display()
            self.blank_id = self.current_s.index(0)
            # self.goal_state()
            return True
        else:
            # print(self.msg)
            return False

    def right(self):
        if (self.blank_id % 3 != 2):
            t = self.current_s[self.blank_id]
            self.current_s[self.blank_id] = self.current_s[self.blank_id + 1]
            self.current_s[self.blank_id + 1] = t
            # self.display()
            self.blank_id = self.current_s.index(0)
            # self.goal_state()
            return True
        else:
            # print(self.msg)
            return False

    def display(self):
        self.displayHeuristic()
        for i in range(0, 3):
            print(self.current_s[i*3 + 0],
                  self.current_s[i*3 + 1], self.current_s[i*3 + 2])
        print("."*30)

    def goal_state(self):
        if self.current_s == self.final:
            print("Reached At Final State")
            print("."*30)
            return True
        return False

    def misplacedtiles(self):
        count = 0
        i = 0
        while i < len(self.current_s):
            if self.current_s[i] != self.final[i]:
                count = count + 1
            i = i + 1
        self.heuristic = count
        return count
        # print(count)

    def __lt__(self,other):
        if self.heuristic < other.heuristic:
            return True
        return False

    def displayHeuristic(self):
        self.misplacedtiles()
        print("heuristic => ",self.heuristic)


def checkClosedList(current_s):
    if current_s in closed_list:
        return False
    return True

def placeLast4(open_list):
    n=len(open_list)
    i=n-4
    if i<0:
        i=0
        
    while i < n :
        key=open_list[i]
        j=i-1

        while j>=0 and key < open_list[j]:
            open_list[j+1]=open_list[j]
            j-=1
        open_list[j+1]=key    
        i+=1



open_list = []
closed_list = []
print("Initial State is =>")

def bestFirstSearch(state):

    if(state.goal_state()):
        p.display()
        print("Caught")
        return

    open_list.append(state)

    while len(open_list) !=0:

        node = open_list.pop(0)
        closed_list.append(node.current_s)

        node.display()

        new_state_up = copy.deepcopy(node)
        if new_state_up.up() and checkClosedList(new_state_up.current_s):
            if new_state_up.goal_state():
                new_state_up.display()
                break
            new_state_up.misplacedtiles()
            open_list.append(new_state_up)
        else:
            del new_state_up

        new_state_left = copy.deepcopy(node)
        if new_state_left.left() and checkClosedList(new_state_left.current_s):
            if new_state_left.goal_state():
                new_state_left.display()
                break
            new_state_left.misplacedtiles()
            open_list.append(new_state_left)
        else:
            del new_state_left

        new_state_down = copy.deepcopy(node)
        if new_state_down.down() and checkClosedList(new_state_down.current_s):
            if new_state_down.goal_state():
                new_state_down.display()
                break
            new_state_down.misplacedtiles()
            open_list.append(new_state_down)
        else:
            del new_state_down

        new_state_right = copy.deepcopy(node)
        if new_state_right.right() and checkClosedList(new_state_right.current_s):
            if new_state_right.goal_state():
                new_state_right.display()
                break
            new_state_right.misplacedtiles()
            open_list.append(new_state_right)
        else:
            del new_state_right
        
        placeLast4(open_list)
    print("Closed List Length => ", len(closed_list))
    print("Open List Length => ", len(open_list))


initial = [2, 0, 3, 1, 8, 4, 7, 6, 5]
final = [1, 2, 3, 8, 0, 4, 7, 6, 5]

p = puzzle(initial, final)
bestFirstSearch(p)