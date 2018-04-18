'''
Created on Mar 10, 2018

@author: Louis
'''
import copy

class Problem(object):
    def __init__(self):
        self.initialState = None
        self.finalState = None
        self.type = None
        self.height = None
        
    #Function for returning the set of valid numbers that can be used
    def getValues(self, values, used):
        return [value for value in values if value not in used]
    
    #Function for returning the first empty cell on the grid
    def get_cell(self, height, state):
        print("get_cell: ",state)
        for row in range(height):
            for column in range(height):
                if state[row][column]  == 0:
                    return row, column
                    
    def actions(self, state):
        numbers = range(1, self.type+1) #search space for a cell
        in_column = [] #list of valid values in a cell's column
        in_block = [] #list of valid values in a cell's block
        
        row, column = self.get_cell(self.height, state) #get the first empty cell of the board
        
        in_row = [number for number in state[row] if (number != 0)]
        options = self.getValues(numbers, in_row) #get the valid values based on the row
        
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        options = self.getValues(options, in_column) #get the valid values based on the row + on the column
        
        row_start = int(row/self.height)*self.height
        column_start = int(column/2)*2
        
        for block_row in range(0, self.height):
            for block_column in range(0, self.height):
                in_block.append(state[row_start + block_row][column_start + block_column])
        options = self.getValues(options, in_block) #get the valid values based on row+column+block
        
        for number in options:
            yield number, row, column, len(options)    
            
    #Function that returns the updated board after adding a new valid value        
    def result(self, state, action):    
        value = action[0]
        row = action[1]
        column = action[2]
        
        new_state = copy.deepcopy(state)
        new_state[row][column] = value
        
        return new_state
    
    
    # Use sums of each row, column and quadrant to determine validity of board state
    def goal_test(self, state):

        # Expected sum of each row, column or quadrant.
        total = sum(range(1, self.type+1))

        # Check rows and columns and return false if total is invalid
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Check quadrants and return false if total is invalid
        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True
        
        
    def expand(self, state):
        return state.expand(state.state)
        
    #Function that determines which node of the tree we choose next for building the solution
    def heuristic(self, state):
        maximum = -1;
        chosen_action = None
        for action in self.actions(state):
            if action[3] > maximum:
                maximum = action[3]
                chosen_action = action
        
        new_state = self.result(state, chosen_action)
        return new_state
        
        
    def readFromFile(self, filename):
        state = [[0]*10 for i in range(10)]
        with open(filename, "r") as f:
            row = 0
            for line in f.readlines():
                line = line.strip()
                line = line.split(";")
                typeP = 0
                for item in line:
                    typeP += 1

                for column in range(0, typeP):
                    state[row][column] = int(line[column])
                row += 1
        
        iState = [[0]*typeP for i in range(typeP)]
        for row in range(0, typeP):
            for column in range(0, typeP):
                    iState[row][column] = state[row][column]
        
        self.initialState = iState
        self.type = typeP
        self.height = int(self.type/3)+1

        
