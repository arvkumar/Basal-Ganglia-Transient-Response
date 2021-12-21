import sys
import os
import copy
import array as arr

# Always specify the path of your working environment
#sys.path.insert(0, "/home/kingshuk/Documents/TCSBG/TCSCode/BGnetwork-BGnetwork-edits_Transient_RatModel_SI/BGcore/Simulations/Templates/") 
#sys.path.insert(0, "/home/tcs/Documents/Kingshuk/BGnetwork-BGnetwork-edits_Transient_RatModel/BGcore/") 

import nest

# Import aditional libraries of your choosing 
import matplotlib.pyplot as plt
import time
import numpy as np
import csv

dopeffectArray = arr.array('f', [0.0]) # Purposefully divided by 10

pdConnRestor = {

		#"STNTI_and_TISTNDisconnected":{"Source":"STNTI_and_TISTNDisconnected", "Target":"None"},
		#"D2TIDisconnected":{"Source":"D2TIDisconnected", "Target":"None"},
		#"TATI_and_TITAisconnected":{"Source":"TATI_and_TITAisconnected", "Target":"None"},
		#"TIFSNDisconnected":{"Source":"TIFSNDisconnected", "Target":"None"},
		#"TIFSN":{"Source":"GPTI","Target":"FSN"},
		"D2TI":{"Source":"D2","Target":"GPTI"},
		"STNTILOOP":{"Source":"STNTILOOP","Target":"None"},
		"TATIAll":{"Source":"TATIAll","Target":"None"},		
		"D1GPI":{"Source":"D1","Target":"GPI"},
		#"FSNDisconnected":{"Source":"FSNDisconnected","Target":""},
}

for connchanges in pdConnRestor:
	# argv[1] is for run id
	argument = 'template_15thFeb_dop840_poisson_SI_V7_restoration.py ' + ' ' + str(connchanges) + ' ' + str(pdConnRestor[connchanges]["Source"]) + ' ' + str(pdConnRestor[connchanges]["Target"] + ' ' + sys.argv[1]) + ' ' + str(1)
	print (argument)
	os.system('python '+argument)


#"TAD1D2Disconnected":{"Source":"TAD1D2Disconnected", "Target":"None"},
#"FSND2Disconnected":{"Source":"FSND2Disconnected", "Target":"None"},
#"STNIncreased":{"Source":"STNIncreased", "Target":"None"},
#"FSNReduced":{"Source":"FSNReduced", "Target":"None"},

#		"TAFSNDisconnected":{"Source":"TAFSNDisconnected", "Target":"None"},
#		"TAD1Disconnected":{"Source":"TAD1Disconnected", "Target":"None"},
#		"TAD2Disconnected":{"Source":"TAD2Disconnected", "Target":"None"},
#		"TATIReduced":{"Source":"TATIReduced", "Target":"None"},
#		"TAD2AndTIFSNDisconnected":{"Source":"TAD2AndTIFSNDisconnected", "Target":"None"},		
#}


