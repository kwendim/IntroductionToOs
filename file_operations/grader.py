#This is a template for the grader

from onpit import Grader
import os

class LabGrader(Grader):
    @Grader.addStep(order='1')
    def step1(self, workingDir, inputCommand):
        filePath = os.path.join(workingDir, 'test.txt')
        if os.path.exists(filePath):
            return True
        else: 
            return False


    @Grader.addStep(order='2')
    def step2(self, workingDir, inputCommand):
        filePath = os.path.join(workingDir, 'test.txt')
        if os.path.exists(os.path.join(workingDir, 'test.txt')):
            with open(filePath, 'r') as f:
                fileContent = f.read()
                if fileContent.strip() == "Hello World":
                    return True
        return False

    @Grader.addStep(order='3')
    def step3(self, workingDir, inputCommand):
        if inputCommand == "cat test.txt":
            return True
        return False
