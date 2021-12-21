#########
#Param file version 1, date:3rd April 2020
#basal: 0,0,"[1.064, 1.002, 0.882, 0.824, 12.7, 6.668693009118541, 29.12145748987854, 29.295546558704455, 10.603092783505154, 61.15119363395225, 61.79840848806366, 0.0, 0.0, 0.0, 0.0]"
#########
from NeuroTools.parameters import ParameterSet
from NeuroTools.parameters import ParameterRange
from NeuroTools.parameters import ParameterTable
from NeuroTools.parameters import ParameterSpace
import NeuroTools.signals as signal

import numpy,shelve,pylab,os,random


def get_parameters():

	p = ParameterSpace({})

	#p.runPD = False
	p.dopAlpha_0 = 0.8 # Normal dopamine level

	# Parameters for neuronal features
	p.outpath = '.'
	p.vm = -65. # Striatal Fast-Spiking Interneurons: From Firing Patterns to Postsynaptic Impact (prev -80.)
	p.vm1 = -87.2 #Gertler D1
	p.vm2 = -85.4 #Gertler D2
	p.vmTA = -55.1
	p.vmTI = -55.1
	p.vmstn = -80.2
	p.vmGPI = -55.8

	p.thD1 = -45.
	p.thD2 = -45.
	p.thfsi = -54.
	p.thTA = -54.7
	p.thTI = -54.7
	p.thstn = -64.0
	p.thGPI = -55.2

	#p.th3 = -45.
	p.tau_synE1 = 0.3
	p.tau_synE2 = 0.3
	p.tau_synI1 = 2.
	p.tau_synI2 = 2.
	p.E_ex = 0.
	p.E_in1 = -64.
	p.E_in2 = -76.
	p.ie = 0.
	p.ie1 = 128.
	#p.ie2 = 80.
	p.cm1 = 192.   	# For MSN (Gertler 2008)
	p.cm2 = 157.	# For MSN (Gertler 2008)
	p.cm_fsi = 700. # Striatal Fast-Spiking Interneurons: From Firing Patterns to Postsynaptic Impact (prev -500.)
	p.gL11 = 8.04 #1000./(124.4) # From Gertler, D1 and D2 1/(124.4Mohm) and 1/(154.83Mohm)
	p.gL12 = 6.46 #1000./(154.83)
	p.gL_fsi = 16.67 #50.0 # Old value was set at 3.84. #"Comparison of IPSCs Evoked by Spiny and Fast-Spiking Neurons in the Neostriatum" mentions Series resistances in the postsynaptic neuron were 20 Mohm or less.
			# Dynamics of action potential firing in electrically connected striatal fast-spiking interneurons - says Input Resistnce is 60 Mohm. Hence gL = 1000.0/60 = 16.67
	#p.cm = 200.		# 200 For MSN (Wolf 2005)	
	#p.gL1 = 12.5		# For MSN (Wolf 2005)	
	#p.gL2 = 25.
	p.tref = 2.
	p.vi1low = p.vm1 #-80.
	p.vi2low = p.vm2 #-80.
	p.vi3low = p.vm #-80. FSI
	p.vi1hi = p.thD1
	p.vi2hi = p.thD2
	p.vi3hi = p.thfsi # FSI
	
	p.viTAlow = p.vmTA
	p.viTIlow = p.vmTI
	p.viTAhi = p.thTA
	p.viTIhi = p.thTI

	p.vistnlow = p.vmstn
	p.viGPIlow = p.vmGPI
	p.vistnhi = p.thstn
	p.viGPIhi = p.thGPI

	# Parameters for running
	p.timestep = 0.1
	p.min_delay = 0.1
	p.max_delay = 50.

	'''
	#""" for restoration/triphasic analysis default values""""	
	p.ctxStartInputtime = 0.0 #In msec
	p.ctxEndInputtime = 700.0 #700.0 #In msec
	p.runtime = 700.0 #700.0 #In msec
	p.leftTimeWindow = 100.0
	p.rightTimeWindow = 300
	#""" for restoration/triphasic analysis default values""""
	'''
	'''
	p.ctxStartInputtime = 0.0 #In msec
	p.ctxEndInputtime = 701.0 #700.0 #In msec
	p.runtime = 701. #.0 #700.0 #In msec
	p.leftTimeWindow = 400.0 #100.0
	p.rightTimeWindow = 200.#2048.0 #250.
	'''
	
	p.ctxStartInputtime = 0.0 #In msec
	p.ctxEndInputtime = 1801.#1201
	p.runtime = 1801. #.0 #1201
	p.leftTimeWindow = 700.0 #100.0
	p.rightTimeWindow = 900.#300
	
	'''
	# For long duration
	p.ctxStartInputtime = 0.0 #In msec
	p.ctxEndInputtime = 5400.0 #700.0 #In msec
	p.runtime = 5400. #.0 #700.0 #In msec
	p.leftTimeWindow = 0.0 #100.0
	p.rightTimeWindow = 5200.#2048.0 #250.
	'''

	p.num01 = 16 # Neuron population in the cortex that receive correlated input

	#For action selection D1 and D2 are broken into two action  A1, A2
	p.num01D1A1 = 150 # Neuron population in the cortex that receive correlated input
	p.num01D1A2 = 150 # Neuron population in the cortex that receive correlated input
	p.num01D2A1 = 150 # Neuron population in the cortex that receive correlated input
	p.num01D2A2 = 150 # Neuron population in the cortex that receive correlated input    

	p.num02 = 10
	p.num1 = 4000 # Pair of neurons in MSN ( inhibitory ) which recieve input from cortex  The ratio of cortex::MSn is 10:1	
	p.numAll = p.num1/2

	#For action selection D1 and D2 are broken into two  pools A1, A2
	p.numAllD1A1 = p.num1/4
	p.numAllD1A2 = p.num1/4
	p.numAllD2A1 = p.num1/4
	p.numAllD2A2 = p.num1/4

	p.numFSI = 80
	p.numTA = 329 # Lindahl 2016 #int(658/2.5)
	p.numTI = 988 # Lindahl 2016 #int(1976/2.5)
	#For action selection TI is broken into two  pools A1, A2
	p.numTIA1 = int(988/2) # Lindahl 2016 #int(1976/2.5)
	p.numTIA2 = int(988/2) # Lindahl 2016 #int(1976/2.5)

	p.numstn = 388 # Lindahl 2016 #int(1508/2.5)
	p.numCTXSTN = round(p.numstn*0.2) # 13 Apr

	p.numGPI = 754 # Lindahl 2016 #int(776/2.5)

	#For action selection GPI is broken into two action pools A1, A2
	p.numGPIA1 = int(754/2)
	p.numGPIA2 = int(754/2)
	p.numParrotNeurons = 16


	p.p_copy = 0.03
	p.nc21 = 10
	p.prob11 = 0.23
	#p.delay11 = 1.
	#p.delay12 = 4.
	p.delay21 = 1.7 #1. # Among D1 and D2
	p.delay22 = 1.7 #0.5 # FSI to D1 and FSI to D2

	p.delayd2TI = 7.0  # From -> To
	p.delayTAd1 = 7.0 
	p.delayTAd2 = 7.0
	p.delayTAfsi = 7.0
	p.delayTATA = 1.0
	p.delayTATI = 1.0

	p.delayTITI = 1.0 # FSI to TA and TI are connected - as not given in Lindahl 2016
	p.delayTITA = 1.0
	p.delayTIfsi = 7.0
	p.delayfsifsi = 1.7

	p.delaystnTA = 2.0 # Taken from param.py
	p.delaystnTI = 2.0
	p.delayTIstn = 1.0#+1.0 #changed
	p.delayTIGPI = 3.0
	p.delaystnGPI = 4.5 - 0.5 #26th June changed
	p.delayd1GPI = 7.0

	p.j01 = 3.1
	p.j02 = 0.55
	minInh = -0.5

	# synaptic strength		
	# Normal condition
	'''
	p.jd1d1 = minInh #-0.15 #
	p.jd2d2 = minInh*2.0 #minInh*(107/42) #-0.35 #
	p.jd1d2 = minInh*2.0*1.21 #minInh*(107/42) #-0.375 #
	p.jd2d1 = minInh*2.0*1.21*1.32 #minInh*(133/42) #-0.45 #
	'''
	p.jd1d1 = -0.15 #
	p.jd2d2 = -0.35 #
	p.jd1d2 = -0.375 #
	p.jd2d1 = -0.45 #

	p.jd1A1d1A2 = p.jd1d1*1.5
	p.jd1A2d1A1 = p.jd1d1*1.5
	p.jd2A1d2A2 = p.jd2d2*1.5
	p.jd2A2d2A1 = p.jd2d2*1.5
	
	p.jfsid1 = -2.6 # Changed for tuning
	p.jfsid2 = -2.6 #for fsn to fsn
	p.jfsifsi = -0.4

	p.jd2TI =  -0.9*1.2 #-1.0
	p.jTAd1 = -0.02
	p.jTAd2 = -0.04
	p.jTAfsi = -0.25 #-0.51
	p.jTATA = -0.11 #(King) # changed from -0.16 (14th feb) -0.33 #
	p.jTATI = -1.3

	p.jTITI = -1.3
	p.jTITA = -0.35 # changed from -0.16 (14th feb) -0.33 #
	p.jTIfsi = -1.0

	p.jstnTA = 0.06*4 #0.11 #
	p.jstnTI = 0.175 #0.300 #0.175  # change taken from Aniruddha da on 7th june
	p.jTIstn = -0.04*2*3*1.25 #- 2nd APR

	p.jTIGPI = -35.0*1.5 #-18.0 # Changed Ani -76.0 #-35.0 #-18.0 #(King) # changed -35.0, to bring down GPI at higher inputs - 2nd APR
	p.jstnGPI = 1.91*2.5 #0.91 #0.45 #0.91 #
	p.jd1GPI = -12.5*1.2 #-13.5-1.5 #-12.0 #-3.0 #-1.0 - 2nd APR

	p.STNCollateral = False
	p.jstnstn = 0.5
	p.delaystnstn  = 1.

	# CTX to neuron connection weight
	p.wd1 = 3.0
	p.wd2 = 3.0
	p.wstn = 1.05 #1.25 #0.25 #1.05 #Jstnctx  - 2nd APR

	#if (p.runPD == True): #PD condition
	# Factor for the changes due to PD condiiton
	p.beta_jGPefsi = -0.53
	p.beta_jd2TI = -0.83
	p.beta_jGPeGPe = -0.83
	#p.beta_jstnGPe = -0.45
	p.beta_jstnGPe = -0.3 #-0.45 # change taken from Aniruddha da on 7th june
	p.beta_jMSNmsn = 0.88
	p.beta_jTAd1 = -1.22
	p.beta_jTAd2 = -1.15
	p.beta_jd1GPI = 0.56
	p.beta_jTIstn = -0.24
	p.beta_jfsifsi = -1.27 #for fsn to fsn

	p.beta_jctxstn = -1.15 #-0.45 Did the calculation again
	p.beta_jctxd1 = 1.04
	p.beta_jctxd2 = -0.26

	# Changes in neuron connections
	p.betaNum_jfsid2 = -0.9
	p.betaNum_jMSNmsn = 0.88

	# Changes in the neuron models
	p.beta_V_thD1 = 0.205 # Computed with "V_th": p.thD1=-45 # 0.0296
	p.beta_E_LD1 = 0.05 # Computed with E_L = -87.2, at dop=0, it should be 10mv lesser # 0.0296
	p.beta_VrFSN = -0.078 # Lindahl 2016
	p.beta_E_LTA = -0.181 # Lindahl 2016
	p.beta_E_LTI = -0.181 # Lindahl 2016
	p.beta_E_LGPI = -0.0896 # Lindahl 2016


	# CTX to neuron connection weight	
	p.wfsi = 3.0
	p.wTA = 0.95 #JTActx
	p.wTI = 1.25 #JTIctx
	p.wGPI = 3.1 #JGPIctx


	
	p.j21 = -1.0  # New value , IPSP Koos1999
	
	p.RateInpD1 = numpy.arange(50.,3560.,500.)
	p.RateInpD2 = numpy.arange(50.,3560.,500.) 

	
	p.delayD1 = 2.5 #Delay Ctx to D1
	p.delayD2 = 2.5 #Delay Ctx to D1
	p.delayTA = 5.0 #Delay Ctx to TA
	p.delayTI = 5.0 #Delay Ctx to TI
	p.delaystn = 2.5 #Delay Ctx to stn
	p.delayGPI = 5.0 #Delay Ctx to GPI
	p.delayfsi = 2.5 #Delay Ctx to FSN

	temp_factor = 15
	p.tx_jctxd1 = 4.5/temp_factor
	p.tx_jctxd2 = 4.5/temp_factor
	p.tx_jctxfsn = 4.5/temp_factor
	p.tx_jctxstn = 3.2/(0.8*temp_factor) #4.0


	# informal deep copy
	p.tx_jctxd1_Orig = p.tx_jctxd1
	p.tx_jctxd2_Orig = p.tx_jctxd2
	p.tx_jctxfsn_Orig = p.tx_jctxfsn
	p.tx_jctxstn_Orig = p.tx_jctxstn

	p.PD_BIPHASIC = True #False 
	p.PD_TRIPHASIC = False #True

	if p.PD_BIPHASIC == True:
		#26th June changes
		p.beta_jtigpi = .416667 
		p.beta_jTIstn = -0.538
		p.beta_jd2TI = -1.003#333
		p.beta_j_tx_ctxstn = 0.625
		p.beta_j_tx_ctxd1 = 0.0
	elif p.PD_TRIPHASIC == True:
		p.beta_jd2TI  = -0.483333
		p.beta_jtigpi = .416667
		p.beta_jd1GPI = 0.4167
		p.beta_j_tx_ctxstn = 0.0
		p.beta_j_tx_ctxd2 = -0.25



	p.NUMTRIALS = 100 #1200 # 1248 for random.randint(775, 800)
	p.stimulationStartPoints =  [random.randint(700, 900) for i in range(p.NUMTRIALS)]
	#p.stimulationStartPoints =  [random.randint(400, 600) for i in range(p.NUMTRIALS)]

	#Create 5 Randomnumbers
	#p.stimulationStartPoints = [200 for i in range(p.NUMTRIALS)] #[random.randint(300, 400) for i in range(p.NUMTRIALS)] #[random.randint(300, 400) for i in range(p.NUMTRIALS)] #[200 for i in range(p.NUMTRIALS)] #[random.randint(300, 400) for i in range(p.NUMTRIALS)]
	#p.stimulationStartPoints = [300, 300]
	#p.stimulationStartPoints =  [random.randint(300, 400) for i in range(p.NUMTRIALS)] 

	## Choose one from below	
	#p.stimulationStartPoints =  [random.randint(700, 724) for i in range(p.NUMTRIALS)] 
	#p.stimulationStartPoints =  [random.randint(725, 749) for i in range(p.NUMTRIALS)]
	#p.stimulationStartPoints =  [random.randint(750, 774) for i in range(p.NUMTRIALS)]
	#p.stimulationStartPoints =  [random.randint(775, 800) for i in range(p.NUMTRIALS)]

	#arr = range(700, 801, 5)
	#p.stimulationStartPoints = numpy.repeat(arr, 100)
	#p.stimulationStartPoints =  [range(700, 801, 5) for i in range(p.NUMTRIALS)] 

	p.BasalTuning = False
	return p	
	
