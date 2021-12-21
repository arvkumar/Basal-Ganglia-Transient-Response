import sys
import os
import copy
import array as arr

# Always specify the path of your working environment
#sys.path.insert(0, "/home/aniruddha/NEST/BGnetwork-BGnetwork-edits/BGcoreTCS30thApril20_TriP_CTX_1N_PD_3TISTN/Simulations/Templates/") 

import nest

# Import aditional libraries of your choosing 
import matplotlib.pyplot as plt
import time
import numpy as np
import csv

dopeffectArray = arr.array('f', [0.0]) # Purposefully divided by 10
#stimDur = 200 # msec
stimDurSeg1 = 0.2 #0 #100 # msec
stimDurSeg2 = 0 #0 #400 # msec
stimDurSeg3 = 3 #0 #200 # msec
stimDur = stimDurSeg1+stimDurSeg2+stimDurSeg3

for dopeffectIndx in range(len(dopeffectArray)):
	for stimIntv in range(1, 100, 200): #(10, 100, 200):		
		argument = 'template_15thFeb_dop840_poisson_SI_V7.py ' + ' ' + str(dopeffectArray[dopeffectIndx]) + ' ' + sys.argv[1] + '_' + str(stimIntv/10) + 'msec_Dur_' +str(stimDurSeg1) + '_' + str(stimDurSeg2) + '_' + str(stimDurSeg3) + 'msec' + ' ' + str(stimIntv/10) + ' ' +str(stimDurSeg1) + ' ' + str(stimDurSeg2) + ' ' + str(stimDurSeg3) 
		#argument = 'template_1stJuly_dop840_poisson_SI.py ' + ' ' + str(dopeffectArray[dopeffectIndx]) + ' ' + sys.argv[1] + '_' + str(stimIntv/10) + 'msec_Dur_' +str(stimDurSeg1) + '_' + str(stimDurSeg2) + '_' + str(stimDurSeg3) + 'msec' + ' ' + str(stimIntv/10) + ' ' +str(stimDurSeg1) + ' ' + str(stimDurSeg2) + ' ' + str(stimDurSeg3) 
		print (argument)
		os.system('python '+argument)

