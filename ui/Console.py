'''
Created on Mar 10, 2018

@author: Louis
'''

class Console(object):
    def __init__(self, controller):
        self.controller = controller
        
    def mainMenu(self):
        cmd = 1
        while (cmd != 0):
            print("1-BFS;2-GBFS;0-Exit")
            cmd = input("Enter command: ")
            if cmd == "0":
                break
            if cmd == "1":
                solution = self.controller.BFS(self.controller.instance)
                if solution:
                    print ("Found solution")
                else:
                    print ("No possible solutions")
            