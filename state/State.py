'''
Created on Mar 10, 2018

@author: Louis
'''
class State(object):
    def __init__(self, state, action=None):
        self.state = state
        self.action = action
        
    def child_state(self, problem, action):
        next_state = problem.result(self.state, action)
        return State(next_state, action)
        
    def expandState(self, problem):
        return (self.child_state(problem, action).state for action in problem.actions(self.state))
        
    def getValue(self, row, column):
        return self.state[row][column]
    
    def setValue(self, row, column, value):
        self.state[row][column] = value
    
    def getRow(self, row):
        return [ x for x in self.state[row]]