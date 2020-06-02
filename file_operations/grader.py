"""This is an auto-generated grader template. For the grader to work it is important not to modify the structure and name of the class"""

import os
class LabGrader():
    def __init__(self):
        self.workingDirectory = '/home/student'   #the directory in which the student is supposed to perform the lab
        self.gradingScripts = {1: self.step1, 2: self.step2, 3: self.step3 }  #the grading script associated with each step
        self.numberOfTasks = 3 #total number of tasks
    
    "Must perorm check and return True or False"
    def step1(self, inputCommand):
        workingDirectory = "/home/student"
        filePath = os.path.join(workingDirectory, 'test.txt')
        if os.path.exists(filePath):
            return True
        else: 
            return False

    "Must perorm check and return True or False"
    def step2(self, inputCommand):
        workingDirectory = "/home/student"
        filePath = os.path.join(workingDirectory, 'test.txt')
        if os.path.exists(os.path.join(workingDirectory, 'test.txt')):
            with open(filePath, 'r') as f:
                fileContent = f.read()
                if fileContent.strip() == "Hello World":
                    return True
        return False
    
    "Must perorm check and return True or False"
    def step3(self, inputCommand):
        if inputCommand == "cat test.txt":
            return True
        return False

