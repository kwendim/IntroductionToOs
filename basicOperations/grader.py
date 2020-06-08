#This is a template for the grader

from onpit import Grader
import os
from  os.path import join
class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if os.path.exists(os.path.join(workingDir, 'firstLab')):
			return True
		return False

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if os.path.exists(join(workingDir, 'backup')):
			if os.path.exists(join(workingDir, 'firstLab', 'file1.txt')) and os.path.exists(join(workingDir, 'firstLab', 'file2.txt')):
				return True
		return False

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		if os.path.exists(join(workingDir, 'backup', 'file1.txt')) and os.path.exists(join(workingDir, 'backup', 'file0.txt')):
			return True
		return False


