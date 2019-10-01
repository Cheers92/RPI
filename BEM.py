# Preamble
import numpy as np
import os
import matplotlib.pyplot as plt
print('\n')
print('\t\t\t>>>>> Blade element momentum tool <<<<<\n\n\n')

# --- --- --- --- --- Importing airfoildata --- --- --- --- --- #
alphatab = []
cltab = []
cdtab = []
dir = '.\\airfoils'
FILE_LIST = os.listdir(dir)
print('Importing airfoil data')
for files in FILE_LIST:
	print('Importing ' + files)
	airfoil = np.genfromtxt(dir + '\\' + files)
	alphatab.append(np.deg2rad(airfoil[:,0]))
	cltab.append(airfoil[:,1])
	cdtab.append(airfoil[:,2])
print('Finished importing airfoil data\n')

# --- --- --- --- --- Tjaereborg imput data --- --- --- --- --- #
# Data specific for the Tjaereborg wind turbine
omega = 2.3                             # Rotational speed [rad/s]
rho = 1.225                             # Density of air [kg/m^3]
R = 30.56                               # Rotor Radius [m]
B = 3                                   # Number of blades [-]
P_rat = 2000000                         # Rated power [w]
U_in = 5                                # Cut in wind speed [m/s]
U_out = 25                              # Cut out wind speed [m/s]
r_i = np.array([6.46, 9.46, 12.46,		# Blade elements [m]
                15.46, 18.46, 21.46,
                24.46, 27.46, 28.96,
                29.86, 30.56])          
c = np.array([3.3, 3.0, 2.7, 2.4,		# Chord length [m]
              2.1, 1.8, 1.5, 1.2,
              1.05, 0.96, 0.95])        
beta = ([8, 7, 6, 5, 4, 3, 2, 1,		# Twist angle [deg]
         0.5, 0.2, 0.16])               
beta = np.deg2rad(beta)
theta = np.deg2rad(0)                   # Pitch angle [deg]
delta_t = 0.01                          # Time increment [s]
Tend = 1
N = Tend/delta_t                        # Number of time steps [-]
V0 = np.array([5, 10, 15, 20 ,25])          # Array of wind speed [m/s]
# --- --- --- --- --- Initializing azimuthal angle --- --- --- --- --- #
# Array initialization
t = np.zeros(100)                       # Initializing time step array
theta_1 = np.zeros(100)                 # Initializing azimuthal angle of blade 1
theta_2 = np.zeros(100)                 # Initializing azimuthal angle of blade 2
theta_3 = np.zeros(100)                 # Initializing azimuthal angle of blade 3
for n in np.arange(1,100):
    t[n] = t[n-1] + delta_t
    theta_1[n] = theta_1[n-1] + (omega*delta_t)
    theta_2[n] = theta_1[n-1] + (2*np.pi/3)
    theta_3[n] = theta_1[n-1] + (4*np.pi/3)
# --- --- --- --- --- Initializing azimuthal angle --- --- --- --- --- #
# Initializing
Init = (N, r_i.size)
W_qs_y = 0
W_qs_z = 0
W_z = 0
Pt = np.zeros(11)
Pn = np.zeros(11)
alpha = np.zeros(11)
C_l = np.zeros([11])
C_d = np.zeros([11])
L = np.zeros([11])
D = np.zeros([11])
V_rel = np.zeros([11])
results = []
# Source code
# Loop for each vind speed

if os.path.isfile('Loads.out'):
	os.remove('Loads.out')
for v in V0:
	print('Calculating aerodynamic forces for ' + str(v) + 'm/s')
	# Loop for each time increment
	for n in np.arange(0, N):
    # Loop for each blade
		for b in np.arange(0, B):
        # Loop for each element
			for e in np.arange(0, r_i.size-1):

				Vy = 0
				Vz = v
				# Calculating relative velocities
				V_rely = Vy + W_qs_y - (omega*r_i[e])           # Relative velocity y-direction [m/s]
				V_relz = Vz + W_qs_z                            # Relative velocity z-direction [m/s]
				V_rel[e] = np.sqrt(V_rely**2 + V_relz**2)       # Relative velocity [m/s]
				# Calculating flow angle
				Phi = np.arctan(V_relz/(-V_rely))               # Flow angle [rad]
				alpha[e] = (Phi - (beta[e]+theta))              # Angle of attack [rad]
	
				# Interpolating lift and drag coefficients from airfoil data
	
				C_l[e] = np.interp(alpha[e], alphatab[e], cltab[e])
				C_d[e] = np.interp(alpha[e], alphatab[e], cdtab[e])
	
				# Calculating lift and drag from corresponding coefficients
				L[e] = 0.5*rho*c[e]*C_l[e]*V_rel[e]**2
				D[e] = 0.5*rho*c[e]*C_d[e]*V_rel[e]**2
	
				# Induction factor
				a = -W_qs_z/Vz
				if a <= (1/3):
					fg = 1
				else:
					fg = 0.25*(5-3*a)
	
				VOW = np.sqrt(Vy**2 + (Vz+fg*W_qs_z)**2)
	
				if np.sin(Phi) > 0.0001:
					f = ((B/2)*((R-r_i[e])/(r_i[e]*np.sin(Phi))))
					F = (2/np.pi)*(np.arccos(np.exp(-f)))
				else:
					F = 1
	
				# Updating values
				W_qs_z = (-B*L[e]*np.cos(Phi))/(4*np.pi*rho*r_i[e]*F*VOW)
				W_qs_y = (-B*L[e]*np.sin(Phi))/(4*np.pi*rho*r_i[e]*F*VOW)
	
				Ct = C_l[e]*np.sin(Phi)-C_d[e]*np.cos(Phi)
				Cn = C_l[e]*np.cos(Phi)-C_d[e]*np.sin(Phi)
				Pt[e] = 0.5*rho*V_rel[e]**2*c[e]*Ct
				Pn[e] = 0.5*rho*V_rel[e]**2*c[e]*Cn
	with open('Loads.out','a') as file:
		for i in Pt:
			file.write(str(round(i,2)) + '\t')
		file.write('\n')