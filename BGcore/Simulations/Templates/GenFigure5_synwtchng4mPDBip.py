import sys
import os
import copy
import array as arr

# Always specify the path of your working environment
sys.path.insert(0, "/home/kingshuk/Documents/TCSBG/TCSCode/BGnetwork-BGnetwork-edits_Transient_RatModel_SI/BGcore/Simulations/Templates/") 
#sys.path.insert(0, "/home/tcs/Documents/Kingshuk/BGnetwork-BGnetwork-edits_Transient_RatModel/BGcore/") 

import nest

# Import aditional libraries of your choosing 
import matplotlib.pyplot as plt
import time
import numpy as np
import csv

dopeffectArray = arr.array('f', [0.0]) # Purposefully divided by 10

pdConnRestor = {
		#"D1GPIIncreased":{"Source":"D1GPIIncreased", "Target":"None"},
		#"D1GPIDecreased":{"Source":"D1GPIDecreased", "Target":"None"},	
		#"D1GPIDecreased4mPDTrip":{"Source":"D1GPIDecreased4mPDTrip", "Target":"None"},
		"D1GPIDecreased4mPDBip":{"Source":"D1GPIDecreased4mPDBip", "Target":"None"},	

		#"TATIIncreased":{"Source":"TATIIncreased", "Target":"None"},
		#"TATIDecreased":{"Source":"TATIDecreased", "Target":"None"},
		#"TATIDecreased4mPDTrip":{"Source":"TATIDecreased4mPDTrip", "Target":"None"},
		"TATIDecreased4mPDBip":{"Source":"TATIDecreased4mPDBip", "Target":"None"},

		#"TITAIncreased":{"Source":"TITAIncreased", "Target":"None"},
		#"TITADecreased":{"Source":"TITADecreased", "Target":"None"},
		#"TITADecreased4mPDTrip":{"Source":"TITADecreased4mPDTrip", "Target":"None"},
		"TITADecreased4mPDBip":{"Source":"TITADecreased4mPDBip", "Target":"None"},

		#"STNTIIncreased":{"Source":"STNTIIncreased", "Target":"None"},
		#"STNTIDecreased":{"Source":"STNTIDecreased", "Target":"None"},
		#"STNTIDecreased4mPDTrip":{"Source":"STNTIDecreased4mPDTrip", "Target":"None"},
		"STNTIDecreased4mPDBip":{"Source":"STNTIDecreased4mPDBip", "Target":"None"},

		#"TISTNIncreased":{"Source":"TISTNIncreased", "Target":"None"},
		#"TISTNDecreased":{"Source":"TISTNDecreased", "Target":"None"},
		#"TISTNDecreased4mPDTrip":{"Source":"TISTNDecreased4mPDTrip", "Target":"None"},
		"TISTNDecreased4mPDBip":{"Source":"TISTNDecreased4mPDBip", "Target":"None"},


		#"D2TIIncreased":{"Source":"D2TIIncreased", "Target":"None"},
		#"D2TIDecreased":{"Source":"D2TIDecreased", "Target":"None"},
		#"D2TIDecreased4mPDTrip":{"Source":"D2TIDecreased4mPDTrip", "Target":"None"},
		"D2TIDecreased4mPDBip":{"Source":"D2TIDecreased4mPDBip", "Target":"None"},
}

for connchanges in pdConnRestor:
	# argv[1] is for run id
	argument = 'template_15thFeb_dop840_poisson_SI_V7_synwtchng4mPDBip.py ' + ' ' + str(connchanges) + ' ' + str(pdConnRestor[connchanges]["Source"]) + ' ' + str(pdConnRestor[connchanges]["Target"] + ' ' + sys.argv[1]) + ' ' + str(0.0)
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


