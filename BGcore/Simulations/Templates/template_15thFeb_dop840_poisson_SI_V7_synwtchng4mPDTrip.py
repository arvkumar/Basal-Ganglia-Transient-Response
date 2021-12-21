import sys
import os
import time
import math
import copy

# Always specify the path of your working environmentf
#sys.path.insert(0, "/home/kingshuk/Documents/TCSBG/TCSCode/BGnetwork-BGnetwork-edits_Transient_RatModel_SI/BGcore/") 
#sys.path.insert(0, "/home/aniruddha/NEST/BGnetwork-BGnetwork-edits/BGcoreTCS30thApril20_TriP_CTX_1N_PD_3TISTN/")
#sys.path.insert(0, "/home/tcs/Documents/Kingshuk/BGnetwork-BGnetwork-edits_Transient_RatModel/BGcore/")
sys.path.insert(0, "/home/hw1036849/Documents/kingshuk/TCSBG/GitReleaseEneuro/BGcore/")  

# Import the base modules BGnodes and BGnetwork (or just BGnodes if you wish not connect anything in your setup)
import Model.BGnodes3rdJune_transient_SI
from Model.BGnetwork3rdJune_transient_SI import BGnetwork
# Import the param.py file of your choosing
import Simulations.BasalFiring.param_tcs_Transient11thNov_SI as param # Desired parameters
import nest

# Import aditional libraries of your choosing 
import matplotlib.pyplot as plt
import time
import numpy as np
import csv
import array as arr

class myclass(BGnetwork):
	
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections, rateD1, rateD2, dopAlpha, percentNRecruitedForTrans,  currentForStimulation, triphasic, stimulationStartPoint,p,pparam=True):

		#(p, cparam, synparam, synparamNoise, noise) = self.setDopConnectionWeights(p, cparam, synparam, synparamNoise, noise, dopAlpha)

		# All arguments are sent to the parent class BGnetwork
		super().__init__(nparam,cparam,synparam, noise, synparamNoise, connections,rateD1, rateD2, dopAlpha, percentNRecruitedForTrans, currentForStimulation, triphasic,stimulationStartPoint,p, pparam)


def getD1D2FR(FR_Table, dopAlpha):		
	fa = math.floor(dopAlpha*10)
	if (fa != 10):
		fb = math.floor(dopAlpha*10)+1		
		freq = FR_Table[fa] + (FR_Table[fb] - FR_Table[fa])*(dopAlpha*10 - fa)/(fb - fa)
	else:
		freq = FR_Table[fa]

	#print ("fa, fb, freq-----------", freq)
	return float(freq)

def resetDopConnectionWeightsSelective(source, target,mv):
	#Restore synweights
	if source =="None" and target == "None":
		print("+++++++++++++++++++++++++++ It is PD state++++++++++++++++++++++++++++++++")
	else:
		if source == "D2TIIncreased":
			RangeUp = np.absolute(param.staticsyn['GPTI']['D2']['weight'] - param.staticsyn['GPTI']['D2']['weight']*1.8024)/3
			param.staticsyn['GPTI']['D2']['weight'] = param.staticsyn['GPTI']['D2']['weight'] - RangeUp*mv #(p.beta_jd2TI = -1.003)
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] + 5*mv
		elif source == "D2TIDecreased":
			RangeDown = np.absolute(param.staticsyn['GPTI']['D2']['weight'] - param.staticsyn['GPTI']['D2']['weight']/1.8024)/3
			param.staticsyn['GPTI']['D2']['weight'] = param.staticsyn['GPTI']['D2']['weight'] + RangeDown*mv #(p.beta_jd2TI = -1.003)
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] - 5.
		elif source == "D2TIDecreased4mPDTrip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['D2']['weight']/1.3866664 - param.staticsyn['GPTI']['D2']['weight'])/3
			param.staticsyn['GPTI']['D2']['weight'] = param.staticsyn['GPTI']['D2']['weight'] + RangeDown*mv #(p.beta_jd2TI = -1.003)
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] - 35.*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 20.
		elif source == "D2TIDecreased4mPDBip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['D2']['weight']/1.8024 - param.staticsyn['GPTI']['D2']['weight'])/3
			param.staticsyn['GPTI']['D2']['weight'] = param.staticsyn['GPTI']['D2']['weight'] + RangeDown*mv #(p.beta_jd2TI = -1.003)
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] - 35.*mv


		elif source == "STNTIIncreased":#$$$$
			RangeUp = np.absolute(param.staticsyn['GPTI']['STN']['weight'] - param.staticsyn['GPTI']['STN']['weight']*1.24)/3
			param.staticsyn['GPTI']['STN']['weight'] = param.staticsyn['GPTI']['STN']['weight'] + RangeUp*mv #p.beta_jstnGPe = -0.3
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] -6
		elif source == "STNTIDecreased":
			RangeDown = np.absolute(param.staticsyn['GPTI']['STN']['weight'] - param.staticsyn['GPTI']['STN']['weight']/1.24)/3
			param.staticsyn['GPTI']['STN']['weight'] = param.staticsyn['GPTI']['STN']['weight'] - RangeDown*mv #p.beta_jstnGPe = -0.3
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] +5
		elif source == "STNTIDecreased4mPDTrip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['STN']['weight']/1.24 - param.staticsyn['GPTI']['STN']['weight'])/3
			param.staticsyn['GPTI']['STN']['weight'] = param.staticsyn['GPTI']['STN']['weight'] - RangeDown*mv #p.beta_jstnGPe = -0.3
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] +15*mv
			param.noise['STN']['rate'] = param.noise['STN']['rate'] -10*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 20.
		elif source == "STNTIDecreased4mPDBip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['STN']['weight']/1.24 - param.staticsyn['GPTI']['STN']['weight'])/3
			param.staticsyn['GPTI']['STN']['weight'] = param.staticsyn['GPTI']['STN']['weight'] - RangeDown*mv #p.beta_jstnGPe = -0.3
			param.noise['GPTI']['rate'] = param.noise['GPTI']['rate'] +15*mv
			param.noise['STN']['rate'] = param.noise['STN']['rate'] -10*mv

		elif source == "TISTNIncreased":
			RangeUp = np.absolute(param.staticsyn['STN']['GPTI']['weight'] - param.staticsyn['STN']['GPTI']['weight']*1.43)/3
			param.staticsyn['STN']['GPTI']['weight'] = param.staticsyn['STN']['GPTI']['weight'] - RangeUp*mv #p.beta_jTIstn = -0.538
			param.noise['STN']['rate'] = param.noise['STN']['rate'] +35*mv
		elif source == "TISTNDecreased":
			RangeDown = np.absolute(param.staticsyn['STN']['GPTI']['weight'] - param.staticsyn['STN']['GPTI']['weight']/1.43)/3
			param.staticsyn['STN']['GPTI']['weight'] = param.staticsyn['STN']['GPTI']['weight'] + RangeDown*mv #p.beta_jTIstn = -0.538
			param.noise['STN']['rate'] = param.noise['STN']['rate'] -25*mv
		elif source == "TISTNDecreased4mPDTrip":
			RangeDown = np.absolute(param.staticsyn['STN']['GPTI']['weight']/1.192 - param.staticsyn['STN']['GPTI']['weight'])/3
			param.staticsyn['STN']['GPTI']['weight'] = param.staticsyn['STN']['GPTI']['weight'] + RangeDown*mv #p.beta_jTIstn = -0.538
			param.noise['STN']['rate'] = param.noise['STN']['rate'] -25*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 20.
		elif source == "TISTNDecreased4mPDBip":
			RangeDown = np.absolute(param.staticsyn['STN']['GPTI']['weight']/1.43 - param.staticsyn['STN']['GPTI']['weight'])/3
			param.staticsyn['STN']['GPTI']['weight'] = param.staticsyn['STN']['GPTI']['weight'] + RangeDown*mv #p.beta_jTIstn = -0.538
			param.noise['STN']['rate'] = param.noise['STN']['rate'] -25*mv

		elif source == "TITAIncreased":
			RangeUp = np.absolute(param.staticsyn['GPTA']['GPTI']['weight'] - param.staticsyn['GPTA']['GPTI']['weight']*1.664)/3
			param.staticsyn['GPTA']['GPTI']['weight'] = param.staticsyn['GPTA']['GPTI']['weight'] - RangeUp*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] +92*mv
		elif source == "TITADecreased":
			RangeDown = np.absolute(param.staticsyn['GPTA']['GPTI']['weight'] - param.staticsyn['GPTA']['GPTI']['weight']/1.664)/3
			param.staticsyn['GPTA']['GPTI']['weight'] = param.staticsyn['GPTA']['GPTI']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -52*mv
		elif source == "TITADecreased4mPDTrip":
			RangeDown = np.absolute(param.staticsyn['GPTA']['GPTI']['weight']/1.664 - param.staticsyn['GPTA']['GPTI']['weight'])/3
			param.staticsyn['GPTA']['GPTI']['weight'] = param.staticsyn['GPTA']['GPTI']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -50*mv
			#param.noise['GPI']['rate'] = param.noise['GPI']['rate'] -40*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 20.
		elif source == "TITADecreased4mPDBip":
			RangeDown = np.absolute(param.staticsyn['GPTA']['GPTI']['weight']/1.664 - param.staticsyn['GPTA']['GPTI']['weight'])/3
			param.staticsyn['GPTA']['GPTI']['weight'] = param.staticsyn['GPTA']['GPTI']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -50*mv
			#param.noise['GPI']['rate'] = param.noise['GPI']['rate'] -40*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] - 20.	

		elif source == "TATIIncreased":
			RangeUp = np.absolute(param.staticsyn['GPTI']['GPTA']['weight'] - param.staticsyn['GPTI']['GPTA']['weight']*1.664)/3
			param.staticsyn['GPTI']['GPTA']['weight'] = param.staticsyn['GPTI']['GPTA']['weight'] - RangeUp*mv #p.beta_jGPeGPe = -0.83
			#param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] +50*mv
		elif source == "TATIDecreased":
			RangeDown = np.absolute(param.staticsyn['GPTI']['GPTA']['weight'] - param.staticsyn['GPTI']['GPTA']['weight']/1.664)/3
			param.staticsyn['GPTI']['GPTA']['weight'] = param.staticsyn['GPTI']['GPTA']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			#param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -40*mv
		elif source == "TATIDecreased4mPDTrip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['GPTA']['weight']/1.664 - param.staticsyn['GPTI']['GPTA']['weight'])/3
			param.staticsyn['GPTI']['GPTA']['weight'] = param.staticsyn['GPTI']['GPTA']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -20*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 20.
		elif source == "TATIDecreased4mPDBip":
			RangeDown = np.absolute(param.staticsyn['GPTI']['GPTA']['weight']/1.664 - param.staticsyn['GPTI']['GPTA']['weight'])/3
			param.staticsyn['GPTI']['GPTA']['weight'] = param.staticsyn['GPTI']['GPTA']['weight'] + RangeDown*mv #p.beta_jGPeGPe = -0.83
			param.noise['GPTA']['rate'] = param.noise['GPTA']['rate'] -20*mv

		elif source == "D1GPIIncreased":
			RangeUp = np.absolute(param.staticsyn['GPI']['D1']['weight'] - param.staticsyn['GPI']['D1']['weight']*0.552)/3
			param.staticsyn['GPI']['D1']['weight'] = -1*(np.absolute(param.staticsyn['GPI']['D1']['weight']) - RangeUp*mv) #p.beta_jd1GPI = 0.56
			param.noise['GPI']['rate'] = param.noise['GPI']['rate'] -40*mv#+50*mv
			print("****************************************",param.noise['GPI']['rate'])
		elif source == "D1GPIDecreased":
			RangeDown = np.absolute(param.staticsyn['GPI']['D1']['weight'] - param.staticsyn['GPI']['D1']['weight']/0.552)/3
			param.staticsyn['GPI']['D1']['weight'] = -1*(np.absolute(param.staticsyn['GPI']['D1']['weight']) + RangeDown*mv) #p.beta_jd1GPI = 0.56
			param.noise['GPI']['rate'] = param.noise['GPI']['rate'] +90*mv#-90*mv
		elif source == "D1GPIDecreased4mPDTrip":
			RangeUp = np.absolute(param.staticsyn['GPI']['D1']['weight']/0.66664 - param.staticsyn['GPI']['D1']['weight'])/3
			param.staticsyn['GPI']['D1']['weight'] = -1*(np.absolute(param.staticsyn['GPI']['D1']['weight']) + RangeUp*mv) #p.beta_jd1GPI = 0.56
			#param.noise['GPI']['rate'] = param.noise['GPI']['rate'] -40*mv#+50*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] + 10.
		elif source == "D1GPIDecreased4mPDBip":
			RangeUp = np.absolute(param.staticsyn['GPI']['D1']['weight']/0.552 - param.staticsyn['GPI']['D1']['weight'])/3
			param.staticsyn['GPI']['D1']['weight'] = -1*(np.absolute(param.staticsyn['GPI']['D1']['weight']) + RangeUp*mv) #p.beta_jd1GPI = 0.56
			#param.noise['GPI']['rate'] = param.noise['GPI']['rate'] -40*mv#+50*mv
			param.nparam["GPI"]["I_e"]  = param.nparam["GPI"]["I_e"] - 20.


def resetDopConnectionWeights():
	param.staticsyn	 = copy.deepcopy(param.staticsynBase)
	param.staticsynNoise = copy.deepcopy(param.staticsynNoiseBase)
	param.cparam = copy.deepcopy(param.cparamBase)
	param.noise = copy.deepcopy(param.noiseBase)
	param.connections = copy.deepcopy(param.connectionsBase)
	param.nparam = copy.deepcopy(param.nparamBase)
	
	param.p.tx_jctxd1 = param.p.tx_jctxd1_Orig
	param.p.tx_jctxd2 = param.p.tx_jctxd2_Orig
	param.p.tx_jctxfsn = param.p.tx_jctxfsn_Orig
	param.p.tx_jctxstn = param.p.tx_jctxstn_Orig


def setDopConnectionWeights(dopAlpha, STNCollateral):
	for dest in param.staticsyn:
		for source in param.staticsyn[dest]:
			if source == "GPTI" and dest == "STN":
				print("###########", param.staticsyn[dest][source]["weight"], param.staticsynDopEffect[dest][source],param.staticsyn[dest][source]["weight"])
			param.staticsyn[dest][source]["weight"] = param.staticsyn[dest][source]["weight"]*(1+param.staticsynDopEffect[dest][source]["dopeffect"]*(dopAlpha - param.p.dopAlpha_0))
			if source == "GPTI" and dest == "STN":
				print("###########", param.staticsyn[dest][source]["weight"], param.staticsynDopEffect[dest][source],param.staticsyn[dest][source]["weight"])


	# CTX to neuron connection weight
	param.staticsynNoise["D1"]["weight"] = param.staticsynNoise["D1"]["weight"]*(1+param.staticsynNoiseDopEffect["D1"]["dopeffect"]*(dopAlpha - param.p.dopAlpha_0))
	param.staticsynNoise["D2"]["weight"] = param.staticsynNoise["D2"]["weight"]*(1+param.staticsynNoiseDopEffect["D2"]["dopeffect"]*(dopAlpha - param.p.dopAlpha_0))
	param.staticsynNoise["STN"]["weight"]= param.staticsynNoise["STN"]["weight"]*(1+param.staticsynNoiseDopEffect["STN"]["dopeffect"]*(dopAlpha - param.p.dopAlpha_0))

	
	# target <--- source
	param.cparam["D2"]["FSN"] = int(param.cparam["D2"]["FSN"]*(1+param.cparamDopEffect["D2"]["FSN"]*( dopAlpha - param.p.dopAlpha_0)))
	param.cparam["D1"]["D1"] = int(param.cparam["D1"]["D1"]*(1+param.cparamDopEffect["D1"]["D1"]*(dopAlpha - param.p.dopAlpha_0)))
	param.cparam["D1"]["D2"] = int(param.cparam["D1"]["D2"]*(1+param.cparamDopEffect["D1"]["D2"]*(dopAlpha - param.p.dopAlpha_0)))
	param.cparam["D2"]["D1"] = int(param.cparam["D2"]["D1"]*(1+param.cparamDopEffect["D2"]["D1"]*(dopAlpha - param.p.dopAlpha_0)))
	param.cparam["D2"]["D2"] = int(param.cparam["D2"]["D2"]*(1+param.cparamDopEffect["D2"]["D2"]*(dopAlpha - param.p.dopAlpha_0)))


	#local_noise['D1']['rate'] = 15165.62 - 80248.8*dopAlpha + 245905*dopAlpha**2 - 412831.8*dopAlpha**3 + 345276.1*dopAlpha**4 - 111939.1*dopAlpha**5
	#local_noise['D2']['rate'] = 1648.671 + 383.343*dopAlpha - 592.803*dopAlpha**2 + 1304.39*dopAlpha**3 - 743.007*dopAlpha**4

	D1_FR_Table = [15200, 9100, 6270, 4650, 3635, 2925, 2420, 2035, 1745, 1540, 1350] # for 2nd and 3rd profile
	D2_FR_Table = [1650, 1680, 1710, 1740, 1775, 1810, 1850, 1885, 1950, 1975, 2000] # for 2nd and 3rd profile

	param.noise['D1']['rate'] = getD1D2FR(D1_FR_Table, dopAlpha)
	param.noise['D2']['rate'] = getD1D2FR(D2_FR_Table, dopAlpha)


 	## From here
	if (STNCollateral == False):	#nottuned with GPI30
		if dopAlpha == 0.8:
			param.p.tx_jctxd1 = 7.5 *param.p.tx_jctxd1_Orig 
			param.p.tx_jctxd2 = 7.5 *param.p.tx_jctxd2_Orig 
			param.p.tx_jctxfsn = 16.0*param.p.tx_jctxfsn_Orig
			param.p.tx_jctxstn = 11.5*param.p.tx_jctxstn_Orig

			param.noise['D1']['rate'] = param.noise['D1']['rate'] -45
			param.noise['D2']['rate'] = param.noise['D2']['rate'] -45
			param.noise['FSN']['rate'] = 2400 - (825*dopAlpha) + (125*dopAlpha**2) + 50 - 60
			param.noise['GPTA']['rate'] = 1035 - (1050.525*dopAlpha) + (181.125*dopAlpha**2) + 70 + 5 #-30
			param.noise['GPTI']['rate'] = 80. + 10
			param.noise['STN']['rate'] = 1230.534 +850. +  147.4664*np.exp(2.522542*dopAlpha) - 650 -50
			param.noise['GPI']['rate'] = 375. + 400.+ 500 + 50 + 125 - 25


		elif dopAlpha == 0.0:

			if param.p.PD_BIPHASIC == True:

				param.p.tx_jctxd1 = 2.35*param.p.tx_jctxd1_Orig 
				param.p.tx_jctxd2 = 10.0*param.p.tx_jctxd2_Orig 
				param.p.tx_jctxfsn = 13.5*param.p.tx_jctxfsn_Orig
				param.p.tx_jctxstn = 8.0*0.5*param.p.tx_jctxstn_Orig 

				param.noise['D1']['rate'] = param.noise['D1']['rate'] + 100
				param.noise['D2']['rate'] = param.noise['D2']['rate'] - 45 + 46 - 70

				param.noise['FSN']['rate'] = 2400 - (825*dopAlpha) + (125*dopAlpha**2) + 65 - 35 + 35 - 45
				param.noise['GPTA']['rate'] = 1035 - (1050.525*dopAlpha) + (181.125*dopAlpha**2) -20 + 15 + 20

				##23rdJune consolidated
				param.nparam["GPI"]["V_reset"] = param.nparam["GPI"]["V_th"] + 6. #PD bursting
				param.nparam["GPI"]["tau_w"] = param.nparam["GPI"]["tau_w"]*4. #PD decay time
				param.nparam["GPI"]["b"] = param.nparam["GPI"]["b"]*1.5 # PD decay time

				param.nparam["GPI"]["tau_syn_ex"] = param.nparam["GPI"]["tau_syn_ex"]*0.5263#1.5 #PD rise time
				param.nparam["GPI"]["tau_syn_in"] = param.nparam["GPI"]["tau_syn_in"]*0.1666665 #0.222222 PD decay 


				param.noise['GPI']['rate'] = 0. #PD
				param.nparam["GPI"]["I_e"]  = -950. + 130 + 330  -100 + 500 -65 -10 + 10#PD


				param.noise['STN']['rate'] = 1230.534 +210. + 147.4664*np.exp(2.522542*dopAlpha) -235 -25 +26 - 20 + 10 - 10#PD

				param.nparam["GPTI"]["tau_syn_ex"] = param.nparam["GPTI"]["tau_syn_ex"]*0.625#5. # Pd reduced out of dictionary
				param.nparam["GPTI"]["tau_syn_in"] = param.nparam["GPTI"]["tau_syn_in"]*5;
				param.noise['GPTI']['rate'] =  35. + 750 -100 - 5


			elif param.p.PD_TRIPHASIC == True:
				param.p.tx_jctxd1 = 7.5*param.p.tx_jctxd1_Orig 
				param.p.tx_jctxd2 = 8.5*1.2*param.p.tx_jctxd2_Orig
				param.p.tx_jctxfsn = 16.0*param.p.tx_jctxfsn_Orig
				param.p.tx_jctxstn = 12.5*param.p.tx_jctxstn_Orig

				param.noise['D1']['rate'] = param.noise['D1']['rate'] + 100
				param.noise['D2']['rate'] = param.noise['D2']['rate'] - 45 + 55 - 85

				param.noise['FSN']['rate'] = 2400 - (825*dopAlpha) + (125*dopAlpha**2) + 65 - 35 + 50 - 70

				param.nparam['STN']['tau_syn_in'] = 6.*1.1
				param.noise['STN']['rate'] = 1360. + 40 - 140 +340 +20 + 50 - 60 + 50 - 50

				param.noise['GPTA']['rate'] = 1035 - (1050.525*dopAlpha) + (181.125*dopAlpha**2) -20 + 30

				param.nparam["GPTI"]["tau_syn_ex"] = param.nparam["GPTI"]["tau_syn_ex"]*1/8
				param.noise['GPTI']['rate'] = 36. + 1125 + 40 - 30 + 10


				
				param.nparam["GPI"]["tau_syn_ex"] = param.nparam["GPI"]["tau_syn_ex"]/3.5625#1/2.85
				param.noise['GPI']['rate'] = 0.0 + 35 + 5 - 31 + 10
				param.nparam["GPI"]["I_e"]  = -930. + 925.+200

				

	else: # tuned for GPI 30
		print("Nothing to be done as of now")



	# Set for dopamine level of of D1
	vthD1 = param.p.thD1*(1+param.p.beta_V_thD1*(dopAlpha - param.p.dopAlpha_0))
	param.nparam["D1"]["V_th"]  = vthD1

	E_LD1 = param.p.vm1*(1+param.p.beta_E_LD1*(dopAlpha - param.p.dopAlpha_0))
	param.nparam["D1"]["V_reset"]  = E_LD1	
	param.nparam["D1"]["E_L"]  = 	E_LD1					

	# Set for dopamine level of FSN					
	vmFSN = param.p.vm*(1+param.p.beta_VrFSN*(dopAlpha - param.p.dopAlpha_0))
	param.nparam["FSN"]["V_reset"]  = vmFSN	
	param.nparam["FSN"]["E_L"]  = 	vmFSN		

	# Set for dopamine level of GPTA				
	E_LTA = -55.1*(1+param.p.beta_E_LTA*(dopAlpha - param.p.dopAlpha_0)) #"E_L":-55.1
	param.nparam["GPTA"]["E_L"]  = 	E_LTA	

	# Set for dopamine level of GPTI
	E_LTI = -55.1*(1+param.p.beta_E_LTI*(dopAlpha - param.p.dopAlpha_0)) #"E_L":-55.1
	param.nparam["GPTI"]["E_L"]  = 	E_LTI

	# Set for dopamine level of GPI
	E_LGPI = -55.8*(1+param.p.beta_E_LGPI*(dopAlpha - param.p.dopAlpha_0)) #"E_L":-55.8
	param.nparam["GPI"]["E_L"]  = 	E_LGPI






dirPrefix = "DopamineLevel/"

# Test cases of current or voltage stimulations from CTX
totalTestCases = {
	'Test3' : {'triphasicWithCur' : False, 'currentForStim' : 0.0, 'voltageForStim' : np.array([20.0,20.0, 20.0, 20.0]), 'populn': 50.0, 'ouFileName': "Volt_20"},
}



# Test cases for disconnections in the BG network. The first one is for fully connected network. Add from below as required.
disconnections = {
	'all_connectedE_exSTN0' : {'MultDisconnect': {}, 'dirName' : dirPrefix+"all_connected_doplevels"},
}




for disconnect in disconnections: #disconnections Not required as of now
	prevParamValue = []
	multipleDistconnect = []
	for multipleDistconnect in disconnections[disconnect]['MultDisconnect']:
		prevParamValue.append(param.connections[disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['dest']][disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['source']])
		param.connections[disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['dest']][disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['source']] = 0
	
	for testCase in totalTestCases:	#totalTestCases Not required as of now	
		myTestCase = totalTestCases[testCase]
		triphasicWithCurrent = myTestCase['triphasicWithCur']
		currentForStimulation = myTestCase['currentForStim']
		voltageForStimulation = myTestCase['voltageForStim']
		outFileName = myTestCase['ouFileName']
		dirName = disconnections[disconnect]['dirName'] + '_STNCol=' + str(param.p.STNCollateral) + '_' + str(sys.argv[4]) + '/'
		print("Dirname", dirName)


		for mv in range(1,2):		
			resetDopConnectionWeights()
			connchanges = sys.argv[1]
			connchangeSource = sys.argv[2] 
			connchangeTarget = sys.argv[3] 
			dopeffect = float(sys.argv[5]) 
			dopeffect = round (dopeffect,2)
			print(dopeffect)
			setDopConnectionWeights(dopeffect, param.p.STNCollateral)
			print ('-------------connchanges, connchangeSource, connchangeTarget are ',mv, connchanges, connchangeSource, connchangeTarget, '--------------' ) 
			resetDopConnectionWeightsSelective(connchangeSource, connchangeTarget,mv)

			with open("result_16thApril.csv", 'a', newline='') as f:
				writer = csv.writer(f)
				writer.writerow(["dopLevel=", dopeffect,"Source Connection Wts", str(mv), connchangeSource, connchangeTarget, param.staticsyn['GPI']['D1']['weight'],param.staticsyn['STN']['GPTI']['weight'], param.staticsyn['GPTI']['STN']['weight'],param.staticsyn['GPTI']['GPTA']['weight'],param.staticsyn['GPTA']['GPTI']['weight'],param.staticsyn['GPTI']['D2']['weight']])
	

			for percentNRecruitedForTrans in [50]: #, 20, 50, 90]: #(10, 101, 10): # % population used for the transient stimulation	

				CORTEX_trial_tbins = []
				CORTEX_trial_heights = []
				d1_trial_tbins = []
				d1_trial_heights = []
				d2_trial_tbins = []
				d2_trial_heights = []
				fsn_trial_tbins = []
				fsn_trial_heights = []
				ta_trial_tbins = []
				ta_trial_heights = []
				ti_trial_tbins = []
				ti_trial_heights = []
				stn_trial_tbins = []
				stn_trial_heights = []
				gpi_trial_tbins = []
				gpi_trial_heights = []



				for numTrials in range(0, param.p.NUMTRIALS, 1):				
					print(triphasicWithCurrent, currentForStimulation, voltageForStimulation, percentNRecruitedForTrans)
					# Start by reseting the kernel. Always perform this operation before creating any new class
					rateD1 = 0.0
					rateD2 = 0.0
					
					# Start by reseting the kernel. Always perform this operation before creating any new class
					nest.ResetKernel()

					#nest.SetKernelStatus({"resolution":p.timestep,"overwrite_files": True,"local_num_threads":8 })
					# Specify the resolutin of timestep and the folder where data should be writen to

					if dopeffect == 0.0 and param.p.PD_BIPHASIC == True:
						PDState = "Biphasic/"
					elif dopeffect == 0.0 and param.p.PD_TRIPHASIC == True:
						PDState = "Triphasic/"
					elif dopeffect == 0.8:
						PDState = "Normal/"
					
					#RESULTSFolder = "/home/kingshuk/Documents/TCSBG/TCSCode/BGnetwork-BGnetwork-edits_Transient_RatModel_SI/BGcore/Simulations/Templates/GDFS/" + PDState +"Trial" + str(numTrials)

					#RESULTSFolder = "/home/aniruddha/NEST/BGnetwork-BGnetwork-edits/BGcoreTCS30thApril20_TriP_CTX_1N_PD_3TISTN/Simulations/Templates/GDFS_poisson_2Apr21_10CTX/" + PDState +"Trial" + str(numTrials)
					RESULTSFolder = "/home/hw1036849/Documents/kingshuk/TCSBG/GitReleaseEneuro/BGcore/Simulations/Templates/GDFS/" + PDState + str(sys.argv[2]) + "/"+ str(mv) +"/Trial" + str(numTrials)

					if not os.path.exists(RESULTSFolder):
						print("***************************************************Directory does not exist***********************************************")
						os.makedirs(RESULTSFolder)

					nest.SetKernelStatus({"resolution":param.p.timestep, 'data_path': RESULTSFolder, 'overwrite_files':True})
					#print(os.times())
					#nest.SetKernelStatus({'grng_seed' : int(getattr(os.times(), 'elapsed'))})
					#nest.SetKernelStatus({'rng_seeds' : [int(0.8*getattr(os.times(), 'elapsed'))]})

					# Create a class with chosen parameters from param. Do NOT create more than one class since NEST can only simulate one set-up at a give		n time
					# If you want to create an aditional class with different parameters make sure to reset the kernel and specify a new path for your data 	to be writen
					# Do all this AFTER you have simulated the first class if you don't wanna loose any changes. 

					triphasic = triphasicWithCurrent
					mySetup1 = myclass(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,rateD1, rateD2, dopeffect, percentNRecruitedForTrans, currentForStimulation, triphasic, param.p.stimulationStartPoints[numTrials],param.p,param.pparam) # triphasic for transient current from ctx
			

					# Connect spike detector and set Ie to 0
					mySetup1.connectSpikeDet()


					# Perform any other operation on the class based on what methods you specified
					# You can put any operation in a loop, for example changing the poisson rate for a specific nodetus

					# Simulate
					SIMULATIONTIME = param.p.runtime
					
					#############################################
				
					print("Vm based Triphasic ****************, voltageForStimulation = ",numTrials+1, voltageForStimulation, " mV")
					
					numCORTEX_N = 10
					CTXPopSz = str(numCORTEX_N) #"1"
					CTXpopsize = CTXPopSz



					if param.p.BasalTuning == False:
						scaledbaseRate = [3.100000,   83.100000,   43.661930,   21.771249,    8.841317,    2.790898,    0.519879,    0.024115, 0.01, 0.01, 0.01, 0.01, 0.01,  0.253403,    0.715238, 1.199472,    1.627790,    1.979538,    2.257282,    2.471542,    2.634351,    2.756763,    2.848080,    2.915780,    2.965717, 3.002394,    3.029233,    3.048809,    3.1, 3.1]
					else:
						scaledbaseRate = [3.1]*30

					shiftedStimStartTime = float(param.p.stimulationStartPoints[numTrials]) + np.arange(0,29)#np.arange(0,34)
					shiftedStimStartTime = list(np.insert(shiftedStimStartTime, 0, 0.1))
					print(scaledbaseRate)
					print(shiftedStimStartTime)

					pg = nest.Create("inhomogeneous_poisson_generator", numCORTEX_N)
					nest.SetStatus(pg, {"rate_times": shiftedStimStartTime, "rate_values": scaledbaseRate, "allow_offgrid_times": True})

					stimInterval = len(shiftedStimStartTime) #Dummy
					StimSeg_1Dur = len(shiftedStimStartTime) #Dummy
					StimSeg_2Dur = len(shiftedStimStartTime) #Dummy
					StimSeg_3Dur = len(shiftedStimStartTime) #Dummy

					if (PDState == "Normal/"):
						'''
						param.p.tx_jctxd1 = 7.5 *param.p.tx_jctxd1_Orig 
						param.p.tx_jctxd2 = 7.5 *param.p.tx_jctxd2_Orig 
						param.p.tx_jctxfsn = 16.0*param.p.tx_jctxfsn_Orig
						param.p.tx_jctxstn = 11.5*param.p.tx_jctxstn_Orig
						'''
					elif (PDState == "Biphasic/"):
						'''
						param.p.tx_jctxd1 = 2.35*tx_jctxd1_Orig 
						param.p.tx_jctxd2 = 10.0*tx_jctxd2_Orig 
						param.p.tx_jctxfsn = 13.5*tx_jctxfsn_Orig
						param.p.tx_jctxstn = 8.0*tx_jctxstn_Orig
						''' 

					
					mySetup1.createInputTransientV3(param.staticsynNoise, param.pparam, percentNRecruitedForTrans, voltageForStimulation,param.p,CTXPopSz, pg)

					sdCtxProbe = nest.Create('spike_detector', 1) # Detector is one
					nest.SetStatus(sdCtxProbe, [{"withtime": True,"withgid": True, "to_file" : True}])
					nest.Connect(pg, sdCtxProbe, "all_to_all")

					mySetup1.simulate(SIMULATIONTIME)

					# This is for logging the poisson spikes for cortex
					ctxSpikeD = nest.GetStatus(sdCtxProbe,keys="events")[0]
					ctxEvs = ctxSpikeD["senders"]
					allSpikes = ctxSpikeD["times"]
					#############################################

					mySetup1.connectMultimeter(1234)
					spike_event_list, a, mn_firing_rate = mySetup1.countSpikes(param.p)
					print("frequency" + str(mySetup1.freq))			
					
					# Plot one single trial as a sample one
					
					print("Mean firing rate: ",mn_firing_rate)
					with open("result_16thApril.csv", 'a', newline='') as f:
						writer = csv.writer(f)
						writer.writerow([rateD1,rateD2,mn_firing_rate])

					hist_binwidth = 1.0

					color_marker = "p"
					color_bar = "blue"
					color_edge = "black"
					
					leftTimeWindow = param.p.leftTimeWindow#50.0
					rightTimeWindow = param.p.rightTimeWindow#1500.0

					# For CORTEX
					t_bins = np.arange(0, param.p.runtime, float(hist_binwidth))
					n, bins = mySetup1._histogram(ctxSpikeD["times"], bins=t_bins)
					heights = 1000* n / (hist_binwidth * numCORTEX_N)   # CORTEX has 1 inhomogeneous neuron
					tmp1_all = t_bins
					tmp2_all = heights
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]	
					CORTEX_trial_tbins.append(tmp1)
					CORTEX_trial_heights.append(tmp2)

					# For D1 onwards
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('D1',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]	
					d1_trial_tbins.append(tmp1)
					d1_trial_heights.append(tmp2)
					#plotid = axs1[0].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('D2',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					d2_trial_tbins.append(tmp1)
					d2_trial_heights.append(tmp2)
					#plotid = axs1[1].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('FSN',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					fsn_trial_tbins.append(tmp1)
					fsn_trial_heights.append(tmp2)
					#plotid = axs1[2].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('GPTA',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					ta_trial_tbins.append(tmp1)
					ta_trial_heights.append(tmp2)
					#plotid = axs1[3].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('GPTI',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					ti_trial_tbins.append(tmp1)
					ti_trial_heights.append(tmp2)
					#plotid = axs1[4].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('STN',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					stn_trial_tbins.append(tmp1)
					stn_trial_heights.append(tmp2)
					#plotid = axs1[5].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
					tmp1_all,tmp2_all = mySetup1.get_histogram_data('GPI',hist_binwidth,param.p)
					res = [idx for idx, val in enumerate(tmp1_all) if val >= param.p.stimulationStartPoints[numTrials] - leftTimeWindow and val < param.p.stimulationStartPoints[numTrials] + rightTimeWindow] 
					tmp1 = tmp1_all[res]
					for cn  in range(0,len(tmp1)):
						tmp1[cn] = tmp1[cn] -  (param.p.stimulationStartPoints[numTrials] - leftTimeWindow)
					tmp2 = tmp2_all[res]
					gpi_trial_tbins.append(tmp1)
					gpi_trial_heights.append(tmp2)
					#plotid = axs1[6].bar(tmp1, tmp2, width=hist_binwidth, color=color_bar,edgecolor=color_edge)

					print ("Num Trials **************", numTrials+1, "GPI time index=",tmp1)
					IMAGEFOLDERPATH = "images/"+dirName+"/" + connchanges  + "/"
					if not os.path.exists(IMAGEFOLDERPATH):
						os.makedirs(IMAGEFOLDERPATH)


					with open(IMAGEFOLDERPATH + 'dop_'+str(mv)+"_"+CTXpopsize+'_' + str(dopeffect)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '_SingleTrial_GPI_FR.csv','a', newline='') as f:
						writer = csv.writer(f)
						writer.writerow(gpi_trial_heights[-1])

					with open(IMAGEFOLDERPATH + 'dop_'+str(mv)+"_"+CTXpopsize+'_' + str(dopeffect)+ '_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '_SingleTrialTimestamp_GPI_FR.csv','a', newline='') as f1:
						writer = csv.writer(f1)
						writer.writerow([float(param.p.stimulationStartPoints[numTrials])])

				num_rows = len(CORTEX_trial_heights)
				num_cols = len(CORTEX_trial_heights[0])

				totals = num_cols * [0.0]
				for line in CORTEX_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_CORTEX = [total / num_rows for total in totals]

				num_rows = len(d1_trial_heights)
				num_cols = len(d1_trial_heights[0])

				totals = num_cols * [0.0]
				for line in d1_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_d1 = [total / num_rows for total in totals]

				num_rows = len(d2_trial_heights)
				num_cols = len(d2_trial_heights[0])

				totals = num_cols * [0.0]
				for line in d2_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_d2 = [total / num_rows for total in totals]

				num_rows = len(fsn_trial_heights)
				num_cols = len(fsn_trial_heights[0])

				totals = num_cols * [0.0]
				for line in fsn_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_fsn = [total / num_rows for total in totals]

				num_rows = len(ta_trial_heights)
				num_cols = len(ta_trial_heights[0])

				totals = num_cols * [0.0]
				for line in ta_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_ta = [total / num_rows for total in totals]

				num_rows = len(ti_trial_heights)
				num_cols = len(ti_trial_heights[0])

				totals = num_cols * [0.0]
				for line in ti_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_ti = [total / num_rows for total in totals]

				num_rows = len(stn_trial_heights)
				num_cols = len(stn_trial_heights[0])

				totals = num_cols * [0.0]
				for line in stn_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_stn = [total / num_rows for total in totals]

				num_rows = len(gpi_trial_heights)
				num_cols = len(gpi_trial_heights[0])

				totals = num_cols * [0.0]
				for line in gpi_trial_heights:
					#print(len(line))
					for index in range(num_cols):
						totals[index] = totals[index] + line[index]

				averages_gpi = [total / num_rows for total in totals]

				print("LEN =", len(d1_trial_tbins),len(averages_d1))
				color_marker = "p"
				color_bar = "blue"
				color_edge = "black"
				fig, axs = plt.subplots(8)
				fig.set_figheight(25)
				fig.set_figwidth(15)
				plotid = axs[0].bar(CORTEX_trial_tbins[0][600:800], averages_CORTEX[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[0].title.set_text(' CORTEX ')
				plotid = axs[1].bar(d1_trial_tbins[0][600:800], averages_d1[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[1].title.set_text(str(percentNRecruitedForTrans) +'% D1 ')
				plotid = axs[2].bar(d2_trial_tbins[0][600:800], averages_d2[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[2].title.set_text(str(percentNRecruitedForTrans)+' % D2 ')
				plotid = axs[3].bar(fsn_trial_tbins[0][600:800], averages_fsn[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[3].title.set_text(str(percentNRecruitedForTrans)+ '% FSN ')
				plotid = axs[4].bar(ta_trial_tbins[0][600:800], averages_ta[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[4].title.set_text(str(percentNRecruitedForTrans)+'% TA ')
				plotid = axs[5].bar(ti_trial_tbins[0][600:800], averages_ti[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[5].title.set_text(str(percentNRecruitedForTrans)+'% TI ')
				plotid = axs[6].bar(stn_trial_tbins[0][600:800], averages_stn[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[6].title.set_text(str(percentNRecruitedForTrans)+'% STN ')
				plotid = axs[7].bar(gpi_trial_tbins[0][600:800], averages_gpi[600:800], width=hist_binwidth, color=color_bar,edgecolor=color_edge)
				axs[7].title.set_text(str(percentNRecruitedForTrans)+'% GPI ')

				IMAGEFOLDERPATH = "images/"+dirName + "/" + connchanges + "/"
				if not os.path.exists(IMAGEFOLDERPATH):
					os.makedirs(IMAGEFOLDERPATH)

				fig.savefig(IMAGEFOLDERPATH +connchanges +'dop_'+str(mv)+"_"+CTXpopsize+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+'_GPI'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.png')

				with open(IMAGEFOLDERPATH + 'dop_'+str(mv)+"_"+CTXpopsize+'_'+str(dopeffect) + '_MultiTrial_'+str(param.p.NUMTRIALS)+ '_GPI'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_gpi)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_TA'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_ta)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_TI'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_ti)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_STN'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_stn)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_FSN'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_fsn)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_D1'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_d1)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_D2'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_d2)
				with open(IMAGEFOLDERPATH+'dop_'+CTXPopSz+'_'+str(dopeffect)+'_MultiTrial_'+str(param.p.NUMTRIALS)+ '_CORTEX'+'_'+str(outFileName)+'_N='+str(percentNRecruitedForTrans)+'percnt_' + str(StimSeg_1Dur) + 'ms_' + str(StimSeg_2Dur) + 'ms_' + str(StimSeg_3Dur) + 'ms' + '.csv', 'w', newline='') as f:
					writer = csv.writer(f)
					writer.writerow(averages_CORTEX)
				fig.clear()
				plt.close('all')
				#End of trials
			# End of population

	# Not required as of now
	# Restore the value for the next test case
	listed = 0
	for multipleDistconnect in disconnections[disconnect]['MultDisconnect']:
		#time.sleep(2)
		param.connections[disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['dest']][disconnections[disconnect]['MultDisconnect'][multipleDistconnect]['source']] = prevParamValue[listed]
		listed = listed + 1
	
	# End of inner for loops
# End of testCase for loop

