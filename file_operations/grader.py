#This is a template for the grader

from grader import Grader
import os

class LabGrader(Grader):
    @Grader.addStep(name='create')
    def step1(self, workingDir, inputCommand):
        filePath = os.path.join(workingDir, 'test.txt')
        if os.path.exists(filePath):
            return True
        else: 
            return False


    @Grader.addStep(name='addcontent')
    def step2(self, workingDir, inputCommand):
        filePath = os.path.join(workingDir, 'test.txt')
        if os.path.exists(os.path.join(workingDir, 'test.txt')):
            with open(filePath, 'r') as f:
                fileContent = f.read()
                if fileContent.strip() == "Hello World":
                    return True
        return False

    @Grader.addStep(name='displaycontent')
    def step3(self, workingDir, inputCommand):
        if inputCommand == "cat test.txt":
            return True
        return False
