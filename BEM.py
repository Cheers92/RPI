# Preamble
import numpy as np
import os
# Importing airfoildata
class airfoils:
	def __init__(self,dir):
		self.dir = dir

	def imp(self,dir):
		airfoil_1 = np.genfromtxt('.\\airfoils\\tjaere04_ds.dat')
		airfoil_2 = np.genfromtxt('.\\airfoils\\tjaere05_ds.dat')
		airfoil_3 = np.genfromtxt('.\\airfoils\\tjaere06_ds.dat')
		airfoil_4 = np.genfromtxt('.\\airfoils\\tjaere07_ds.dat')
		airfoil_5 = np.genfromtxt('.\\airfoils\\tjaere08_ds.dat')
		airfoil_6 = np.genfromtxt('.\\airfoils\\tjaere09_ds.dat')
		airfoil_7 = np.genfromtxt('.\\airfoils\\tjaere10_ds.dat')
		airfoil_8 = np.genfromtxt('.\\airfoils\\tjaere11_ds.dat')
		airfoil_9 = np.genfromtxt('.\\airfoils\\tjaere12_ds.dat')
		airfoil_10 = np.genfromtxt('.\\airfoils\\tjaere13_ds.dat')
		airfoil_11 = np.genfromtxt('.\\airfoils\\tjaere14_ds.dat')
		
		alphatab = np.array([airfoil_1[:,0],
							airfoil_2[:,0],
							airfoil_3[:,0],
							airfoil_4[:,0],
							airfoil_5[:,0],
							airfoil_6[:,0],
							airfoil_7[:,0],
							airfoil_8[:,0],
							airfoil_9[:,0],
							airfoil_10[:,0],
							airfoil_11[:,0]])
		alphatab = np.deg2rad(alphatab)
		
		cltab   = np.array([airfoil_1[:,1],
							airfoil_2[:,1],
							airfoil_3[:,1],
							airfoil_4[:,1],
							airfoil_5[:,1],
							airfoil_6[:,1],
							airfoil_7[:,1],
							airfoil_8[:,1],
							airfoil_9[:,1],
							airfoil_10[:,1],
							airfoil_11[:,1]])
		
		cdtab   = np.array([airfoil_1[:,2],
							airfoil_2[:,2],
							airfoil_3[:,2],
							airfoil_4[:,2],
							airfoil_5[:,2],
							airfoil_6[:,2],
							airfoil_7[:,2],
							airfoil_8[:,2],
							airfoil_9[:,2],
							airfoil_10[:,2],
							airfoil_11[:,2]])
FILE_LIST = os.listdir('.\\airfoils')
print(FILE_LIST)


