# Preamble
import numpy as np
import os
import matplotlib.pyplot as plt
# Importing airfoildata
alphatab = []
cltab = []
cdtab = []
dir = '.\\airfoils'
FILE_LIST = os.listdir(dir)
for files in FILE_LIST:
	airfoil = np.genfromtxt(dir + '\\' + files)
	alphatab.append(np.deg2rad(airfoil[:,0]))
	cltab.append(airfoil[:,1])
	cdtab.append(airfoil[:,2])






