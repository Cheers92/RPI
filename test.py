# Preamble
import numpy as np
import os
# Importing airfoildata
class airfoil_import:
	def __init__(self,dir):
		print('in init')
		self.dir = dir
		self.alphatab = []
		self.cltab = []
		self.cdtab = []
	def importing(self):
		FILE_LIST = os.listdir(dir)
		print(FILE_LIST)
		for files in FILE_LIST:
			airfoil = np.genfromtxt(dir + '\\' + files)
			self.alphatab.append(np.deg2rad(airfoil[:,0]))
			self.cltab.append(airfoil[:,1])
			self.cdtab.append(airfoil[:,2])
dir = '.\\airfoils'
airfoil_import.importing(dir)




