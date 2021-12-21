#########
#Param file version 1, date:3rd April 2020
#basal: 0,0,"[1.064, 1.002, 0.882, 0.824, 12.7, 6.668693009118541, 29.12145748987854, 29.295546558704455, 10.603092783505154, 61.15119363395225, 61.79840848806366, 0.0, 0.0, 0.0, 0.0]"
#########

import sys
import copy
import numpy,shelve,pylab,os
import Simulations.BasalFiring.param_val_Transient11thNov_SI_SNrLIF as params

p = params.get_parameters()  	


# Connectivity state. "Destination neuron" : { "Source neurons"}
state = {
"D1": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"CTX":1}, # Ani - added TA
"D2": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"CTX":1}, # Ani - added TA
"GPTA": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0}, # Ani - removed CTX
"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"CTX":0}, # Ani - removed CTX
"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"CTX":1},
"FSN": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":0,"CTX":1},
"GPI": {"D1": 1,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"CTX":0}, # Ani - removed CTX
"drawAll": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":1,"STN":1,"CTX":0},
}

sc = 0.1
sc2 = 0.1
start = 0.0
stop = 50000.0

'''
basal firing in BG:
D1: ~1Hz
D2: ~1Hz
TI: ~30-40Hz
TA: 5-10Hz
STN: ~15-20Hz
GPi: ~5-10Hz

  D1, D2, FSN, TA, TI, STN, GPI tuned in UT with the following background noise
"[0.743, 0.742, 14.025, 8.74772036474164, 38.072874493927124, 17.216494845360824, 5.135278514588859]"
"[0.758, 0.739, 13.975, 8.729483282674773, 38.16801619433198, 17.314432989690722, 5.254641909814324]"

NEW
"[1.647, 0.066, 13.75, 9.592705167173252, 40.12348178137652, 15.34020618556701, 1.1962864721485411]"
"[1.644, 0.073, 13.825, 9.610942249240122, 40.058704453441294, 15.329896907216495, 1.2705570291777188]"

NEW
"[1.444, 0.181, 13.925, 9.64741641337386, 39.59919028340081, 15.350515463917526, 1.0185676392572944]"
"[1.393, 0.191, 14.0, 9.653495440729483, 39.55668016194332, 15.34020618556701, 0.9814323607427056]"

NEW
50,50,"[1.128, 0.362, 14.125, 8.498480243161094, 38.945344129554655, 17.18041237113402, 6.89920424403183]"
50,150,"[1.124, 0.367, 13.9, 8.516717325227964, 38.917004048582996, 17.211340206185568, 6.89920424403183]"
'''

'''     For Normal
	'D1' : {'rate' : 1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070.0*0.15}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 925.0}, #900.0},
	'STN' : {'rate' : 260.*9},
	'GPI' : {'rate' : 4400.0},
	
	Normal new
	'D1' : {'rate' : 1775.0}, #1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070.0*0.15}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 925.0}, #900.0},
	'STN' : {'rate' : 260.*9},
	'GPI' : {'rate' : 4100.0},
'''
'''
	For PD 2
	'D1' : {'rate' : 1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070*0.07}, #Changed for PD # 2070.0*0.15}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 925.0}, #900.0},
	'STN' : {'rate' : 260.*12.0}, # For PD
	'GPI' : {'rate' : 4400.0+950.0}, # For PD
'''
'''
	For PD 3
	'D1' : {'rate' : 1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0 }, #For PD 1950.0}, #2196.0},# 2196.0},
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070*0.07}, #Changed for PD # 2070.0*0.15}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 50.0}, #For PD 925.0}, #900.0},
	'STN' : {'rate' : 260.*11.1}, # For PD
	'GPI' : {'rate' : 3400.0}, # For PD
'''
'''
	For PD 4
	'D1' : {'rate' : 1580.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0 }, #For PD 1950.0}, #2196.0},# 2196.0},
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070*0.07}, #Changed for PD # 2070.0*0.15}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 50.0}, #For PD 925.0}, #900.0},
	'STN' : {'rate' : 260.*11.1}, # For PD
	'GPI' : {'rate' : 2950.0}, # For PD

	For PD 5
	'D1' : {'rate' : 1450.0}, #1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 1820.0}, #1300.0},
	'GPTA' : {'rate' : 2070.0*0.07}, #Changed for PD #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 50.0}, #Changed for PD #900.0},
	'STN' : {'rate' : 260.*11.1}, #Changed for PD 
	'GPI' : {'rate' : 3000.0}, #Changed for PD 

'''
'''
if p.runPD == True: # Old one with no special weights
	noise = {
		'D1' : {'rate' : 1450.0}, #1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
		'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
		'FSN' : {'rate' : 1820.0}, #1300.0},
		'GPTA' : {'rate' : 2070.0*0.07}, #Changed for PD #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
		'GPTI' : {'rate' : 50.0}, #Changed for PD #900.0},
		'STN' : {'rate' : 260.*11.1}, #Changed for PD 
		'GPI' : {'rate' : 3000.0}, #Changed for PD 
}
'''

# Have set for New PD run with changed weights
'''
if p.runPD == True:
	noise = {		
		'D1' : {'rate' : 3500.0}, #1725.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
		'D2' : {'rate' : 1450.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
		'FSN' : {'rate' : 1820.0}, #1300.0},
		'GPTA' : {'rate' : 2070.0*0.13}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
		'GPTI' : {'rate' : 210.0}, #900.0},
		'STN' : {'rate' : 260.0*4.05},
		'GPI' : {'rate' : 3000.0},
	}
else:
'''
'''
# For dop = 1.0 
noise = {
	'D1' : {'rate' : 1350.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 2000.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 1700.0}, #1300.0},
	'GPTA' : {'rate' : 165.6}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 920.0}, #900.0},
	'STN' : {'rate' : 3068.0},
	'GPI' : {'rate' : 4600.0},
}
'''

# For dop = 0.8 
if p.STNCollateral == False: #  Not tuned for GPI 30
	noise = {		
		'D1' : {'rate' : 1745.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
		'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
		'FSN' : {'rate' : 1870.0}, #1300.0},
		'GPTA' : {'rate' : 380.5}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
		'GPTI' : {'rate' : 927.0}, #900.0},
		#'STN' : {'rate' : 2340.0},
		'STN' : {'rate' : 2800.0}, #3190.0},# witn STN NO collateral normal
		'GPI' : {'rate' : 650.25},
	}
else: # tuned for GPI 30
	noise = {		
		'D1' : {'rate' : 1745.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
		'D2' : {'rate' : 1950.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
		'FSN' : {'rate' : 1820.0}, #1300.0},
		'GPTA' : {'rate' : 350.5}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
		'GPTI' : {'rate' :  827.0}, #900.0},
		#'STN' : {'rate' : 2340.0},
		'STN' : {'rate' : 2820.0},# witn STN collateral normal
		#'STN' : {'rate' : 2860.0},# witn STN NO collateral normal
		'GPI' : {'rate' : 450.25},
	}

noiseBase = copy.deepcopy(noise)

'''
# For dop = 0.0
noise = {		
	'D1' : {'rate' : 15200.0}, #2100.0}, #2124.0},# changed from 1900 to make D1 and D2 basal firing rate comparable ((14th feb))
	'D2' : {'rate' : 1650.0}, #2196.0},# 2196.0}, #changed from 1900 to make D1 and D2 basal firing rate comparable(14th feb)
	'FSN' : {'rate' : 2400.0}, #1820.0}, #1300.0},
	'GPTA' : {'rate' : 1035.0}, #3000.0},# changed from 700 to make TA bit higher @ basal (14th feb)
	'GPTI' : {'rate' : 1000.0}, #900.0},
	'STN' : {'rate' : 1378.0},
	'GPI' : {'rate' : 3200.0},
}
'''

#w1 = 3.0 # Ani - Jc1
#w2 = 3.0 # Ani - Jc2
#w3 = 4.5 # Ani - Jfsictx
staticsynNoise = {
            'D1' : {'weight' : p.wd1,'delay':p.delayD1}, # Ani - w1
            'D2' : {'weight' : p.wd2,'delay':p.delayD1},
            'FSN' : {'weight' : p.wfsi,'delay':p.delayfsi},
            'GPTA' : {'weight' : p.wTA,'delay':p.delayTA},
            'GPTI' : {'weight' : p.wTI,'delay':p.delayTI},
            'STN' : {'weight' : p.wstn,'delay':p.delaystn},
            'GPI' : {'weight' : p.wGPI,'delay':p.delayGPI},
}

staticsynNoiseBase = copy.deepcopy(staticsynNoise)

staticsynNoiseDopEffect = {
            'D1' : {"dopeffect":p.beta_jctxd1}, # Ani - w1
            'D2' : {"dopeffect":p.beta_jctxd2},
            'FSN' : {"dopeffect":0.},
            'GPTA' : {"dopeffect":0.},
            'GPTI' : {"dopeffect":0.},
            'STN' : {"dopeffect":p.beta_jctxstn},
            'GPI' : {"dopeffect":0.},
}


if p.STNCollateral == False:
	connections = {
	"D1": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"GPI":0, "CTX":1},
	"D2": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"GPI":0, "CTX":1},
	"GPTA": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	#"GPTI": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},#d2ti disconnecred
	#"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"GPI":0, "CTX":1},# STN collateral
	"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":0,"GPI":0, "CTX":1},# STN NO collateral
	"FSN": {"D1": 0,"D2":0,"FSN":1,"GPTA":1,"GPTI":1,"STN":0,"GPI":0, "CTX":1},
	"GPI": {"D1": 1,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	}
else:
	connections = {
	"D1": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"GPI":0, "CTX":1},
	"D2": {"D1": 1,"D2":1,"FSN":1,"GPTA":1,"GPTI":0,"STN":0,"GPI":0, "CTX":1},
	"GPTA": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	#"GPTI": {"D1": 0,"D2":1,"FSN":0,"GPTA":1,"GPTI":0,"STN":0,"GPI":0, "CTX":1}, # STN to GPTI disconnected
	#"GPTI": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":1,"GPI":0, "CTX":1},#d2ti disconnecred
	"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"GPI":0, "CTX":1},# STN collateral
	#"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":0,"GPI":0, "CTX":1},# STN NO collateral
	#"STN": {"D1": 0,"D2":0,"FSN":0,"GPTA":0,"GPTI":0,"STN":1,"GPI":0, "CTX":1},# STN collateral & GPTI to STN disconnected
	"FSN": {"D1": 0,"D2":0,"FSN":0,"GPTA":1,"GPTI":1,"STN":0,"GPI":0, "CTX":1},
	"GPI": {"D1": 1,"D2":0,"FSN":0,"GPTA":0,"GPTI":1,"STN":1,"GPI":0, "CTX":1},
	}

connectionsBase = copy.deepcopy(connections)


staticsyn = {
                "D1" : {
                        "D1" : {"weight" : p.jd1d1, "delay" : p.delay21},
                        "D2" : {"weight" : p.jd2d1, "delay" : p.delay21} ,  
                        "FSN" : {"weight" : p.jfsid1 , "delay" : p.delay22},
                        'GPTA': {'weight': p.jTAd1, 'delay': p.delayTAd1},                            
                        }, 
                "D2" :  {
                        "D1" : {"weight" : p.jd1d2, "delay" : p.delay21},
                        "D2" : {"weight" : p.jd2d2, "delay" : p.delay21} ,  
                        "FSN" : {"weight" : p.jfsid2, "delay" : p.delay22},
                        'GPTA': {'weight': p.jTAd2, 'delay': p.delayTAd2},  
                        },

                "FSN" : {
                        "GPTA" : {"weight" : p.jTAfsi, "delay" : p.delayTAfsi}, 
                        "GPTI" : {"weight" : p.jTIfsi, "delay" : p.delayTIfsi},
                        "FSN" : {"weight" : p.jfsifsi, "delay" : p.delayfsifsi},  
                        },

                "GPTA" : {
                        'GPTA': {'weight': p.jTATA, 'delay': p.delayTATA}, 
                        'GPTI': {'weight': p.jTITA, 'delay': p.delayTITA},  
			'STN': {'weight':p.jstnTA,'delay':p.delaystnTA},			
                        },

                "GPTI" : {   
                        'D2': {'weight': p.jd2TI, 'delay': p.delayd2TI}, 
                        'GPTA': {'weight': p.jTATI, 'delay': p.delayTATI}, 
                        'GPTI': {'weight': p.jTITI, 'delay': p.delayTITI},  
			'STN': {'weight':p.jstnTI,'delay':p.delaystnTI},
                        },
               
                "STN" : {
                        "GPTI": {"weight" : p.jTIstn, "delay" : p.delayTIstn}, 
                        #"STN": {"weight" : p.jstnstn, "delay" : p.delaystnstn}, # STN collateral
                        "STN": {"weight" : p.jstnstn, "delay" : p.delaystnstn}, # STN NO collateral
			},
                "GPI" :  {
                        "D1" : {"weight" : p.jd1GPI, "delay" : p.delayd1GPI} , 
                        "GPTI": {"weight" : p.jTIGPI, "delay" : p.delayTIGPI},
                        "STN": {"weight" : p.jstnGPI, "delay" : p.delaystnGPI},

			#"D1A1" : {"model": "tsodyks_synapse","U":0.192*1, "tau_rec": 423.-200,"tau_fac": 559.-300,"weight" : p.jd1GPI, "delay" : p.delayd1GPI},
			#"D1A1" : {"model": "quantal_stp_synapse","U":0.85, "tau_rec": 623.,"tau_fac": 559.,"weight" : p.jd1GPI, "delay" : p.delayd1GPI},

			#"GPTIA1" : {"model": "quantal_stp_synapse","U":0.396*2, "tau_fac": 969.,"tau_rec": 0.,"weight" : p.jTIGPI, "delay" : p.delayTIGPI},
			#"STN": {"model": "quantal_stp_synapse","U":0.85, "tau_rec": 800.,"tau_fac": 0.,"weight" : p.jstnGPI, "delay" : p.delaystnGPI}
                        },

}
staticsynBase = copy.deepcopy(staticsyn)

staticsynDopEffect = {
                "D1" : {
                        "D1" : {"dopeffect":p.beta_jMSNmsn},
                        "D2" : {"dopeffect":p.beta_jMSNmsn} ,  
                        "FSN" : {"dopeffect":0.},
                        'GPTA': {"dopeffect":p.beta_jTAd1},                            
                        }, 
                "D2" :  {
                        "D1" : {"dopeffect":p.beta_jMSNmsn},
                        "D2" : {"dopeffect":p.beta_jMSNmsn} ,  
                        "FSN" : {"dopeffect":0.},
                        'GPTA': {"dopeffect":p.beta_jTAd2},  
                        },

                "FSN" : {
                        "GPTA" : {"dopeffect":p.beta_jGPefsi}, 
                        "GPTI" : {"dopeffect":p.beta_jGPefsi}, 
			"FSN":{"dopeffect":p.beta_jfsifsi}, 
                        },

                "GPTA" : {
                        'GPTA': {"dopeffect":p.beta_jGPeGPe}, 
                        'GPTI': {"dopeffect":p.beta_jGPeGPe},  
			'STN': {"dopeffect":p.beta_jstnGPe},			
                        },

                "GPTI" : {   
                        'D2': {"dopeffect":p.beta_jd2TI}, 
                        'GPTA': {"dopeffect":p.beta_jGPeGPe}, 
                        'GPTI': {"dopeffect":p.beta_jGPeGPe},  
			'STN': {"dopeffect":p.beta_jstnGPe},
                        },
               
                "STN" : {
                        "GPTI": {"dopeffect":p.beta_jTIstn}, 
			"STN":{"dopeffect":0.0}, 
			},
                "GPI" :  {
                        "D1" : {"dopeffect":p.beta_jd1GPI} , 
                        "GPTI": {"dopeffect":p.beta_jtigpi},
                        "STN": {"dopeffect":0.0},
                        },

}


d1d1 = 0.13 #0.07 #
d1d2 = 0.03 #0.045 #
d2d1 = 0.135 #0.13 #
d2d2 = 0.18 #0.23 #
fsid1 = 0.27 #0.89 #
fsid2 = 0.18 #0.60 #

cparam = {"D1" : {"D1" : 364, "D2" : 392, "FSN" : 16, "GPTA" : 10 }, 
             "D2" : {"D1" : 84, "D2" : 504, "FSN": 11, "GPTA" : 10 }, 
             "FSN" : {"FSN" : 10, "GPTA" : 10, "GPTI" : 10 },
             "STN" : {"STN": 8,"GPTI" : 30}, #"STN" : {"GPTI" : 30},
             "GPTA" : {"STN" : 30, "GPTA" : 5, "GPTI" : 25 },
             "GPTI" : { "STN": 30,"D2" : 500, "GPTI" : 25, "GPTA" : 5},
             "GPI" : { "GPTI" : 32, "D1" : 500, "STN" : 30} }

cparamBase = copy.deepcopy(cparam)

cparamDopEffect = {"D1" : {"D1" : p.betaNum_jMSNmsn, "D2" : p.betaNum_jMSNmsn, "FSN" : 1, "GPTA" : 1 }, 
             "D2" : {"D1" : p.betaNum_jMSNmsn, "D2" : p.betaNum_jMSNmsn, "FSN": p.betaNum_jfsid2, "GPTA" : 1}, 
             "FSN" : {"FSN" : 0, "GPTA" : 0, "GPTI" : 0 },
             "STN" : {"STN": 0,"GPTI" : 0},
             "GPTA" : {"STN" : 0, "GPTA" : 0, "GPTI" : 0 },
             "GPTI" : { "STN": 0,"D2" : 0, "GPTI" : 0, "GPTA" : 0},
             "GPI" : { "GPTI" : 0, "D1" : 0, "STN" : 0} }



pparam = {'D1': p.numAll, 'D2': p.numAll, 'FSN': p.numFSI,'GPTA': p.numTA, 'GPTI': p.numTI, 'STN':p.numstn, 'GPI':p.numGPI}



nparam = {
#"GPI":{"a":3.0, "b":200.0, "Delta_T":1.6, "tau_w":20.0, "V_reset":-65.0, "V_th": -55.2, "tau_syn_ex":2.0*2.85, "tau_syn_in":1.7*1.2, "E_L":-55.8, "E_ex":0.0, "E_in":-80.0, "I_e":0.0, "C_m":80.0, "g_L":3.0, "t_ref":p.tref}, # retained to 1.7 from 1.55 #changed from "tau_syn_in":1.7 to bring down Gpi ((14th feb)), changed from "tau_syn_ex":6.0
"GPI":{"V_reset":-65.0, "V_th": -55.2, "tau_syn_ex":2.0*2.85, "tau_syn_in":1.7*1.2, "E_L":-55.8, "E_ex":0.0, "E_in":-80.0, "I_e":0.0, "C_m":80.0, "g_L":3.0, "t_ref":p.tref},

"STN":{"V_reset":-70.0, "V_th": -64.0, "tau_syn_ex":.33, "tau_syn_in":6.0*0.25, "E_L":-80.2, "E_ex": -10.0, "E_in":-84.0, "I_e":1.0, "C_m":60.0, "g_L":10.0, "t_ref":p.tref},

"GPTI" : {"a":2.5, "b":70.0, "Delta_T":1.7, "tau_w":20.0, "V_reset":-60.0, "V_th": -54.7, "tau_syn_ex":0.6*8., "tau_syn_in":1.0, "E_L":-55.1, "E_ex":0.0, "E_in":-65.0, "I_e":12.0, "C_m":40.0, "g_L":1.0, "t_ref":p.tref},

"GPTA" : {"a":2.5, "b":105.0, "Delta_T":2.55, "tau_w":20.0, "V_reset":-60.0, "V_th": -54.7, "tau_syn_ex":1., "tau_syn_in":5.5, "E_L":-55.1, "E_ex":0.0, "E_in":-65.0, "I_e":1.0, "C_m":60.0, "g_L":1.0, "t_ref":p.tref},#changed from "tau_syn_in":2.0 to bring down Gpi(14th feb)

"FSN" : {"V_reset":p.vm, "V_th": p.thfsi, "tau_syn_ex":p.tau_synE1, "tau_syn_in":p.tau_synI1, "E_L":p.vm, "E_ex":p.E_ex, "E_in":p.E_in2, "I_e":p.ie, "C_m":p.cm_fsi, "g_L":p.gL_fsi, "t_ref":p.tref},

"D1" : {"V_reset":p.vm1, "V_th": p.thD1, "tau_syn_ex":p.tau_synE1, "tau_syn_in":p.tau_synI1, "E_L":p.vm1, "E_ex":p.E_ex, "E_in":p.E_in1, "I_e":p.ie1, "C_m":p.cm1, "g_L":p.gL11, "t_ref":p.tref},

"D2" : {"V_reset":p.vm2, "V_th": p.thD2, "tau_syn_ex":p.tau_synE1, "tau_syn_in":p.tau_synI1, "E_L":p.vm2, "E_ex":p.E_ex, "E_in":p.E_in1, "I_e":p.ie, "C_m":p.cm2, "g_L":p.gL12, "t_ref":p.tref},}

nparamBase = copy.deepcopy(nparam)

