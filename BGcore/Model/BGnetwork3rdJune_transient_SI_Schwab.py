import sys
import nest
from Model.BGnodes3rdJune_transient_SI_Schwab import BGnodes
import numpy as np
import tls as tls
#import BGcore.Simulations.BasalFiring.param_val_Transient2ndApril as params
#p = params.get_parameters() 

#num01 = 150
#num1 = 4000

class BGnetwork(BGnodes):
	def __init__(self,nparam,cparam,synparam, noise,synparamNoise, connections,  rateD1, rateD2, dopAlpha, percentNRecruitedForTrans, currentForStimulation, triphasic, stimulationStartPoint,p,pparam=True):
		super().__init__(nparam,dopAlpha,p,pparam)
		
		self.connect(nparam,p,cparam,synparam, noise, connections, pparam)
		self.createPoisson(noise, synparamNoise, rateD1, rateD2,p)
		if (triphasic == True):
			self.createInputTransient(synparamNoise, percentNRecruitedForTrans, currentForStimulation,stimulationStartPoint,p)
		
	#Changed Ani for transition
	def createInputTransient(self, synparamNoise, percentageN, currentForStimulation,stimulationStartPoint,p):
		print("Current based Triphasic ------------------ ")
		print("currentForStimulation =", currentForStimulation)
		#m = 1.5
		dc = nest.Create('dc_generator',1)
		#nest.SetStatus(dc,{'amplitude':currentForStimulation,'start':float(stimulationStartPoint),'stop':stimulationStartPoint+0.2})
		nest.SetStatus(dc,{'amplitude':currentForStimulation,'start':float(stimulationStartPoint),'stop':stimulationStartPoint+25.0})
	
		syn_dict =  synparamNoise['D1']
		#nest.Connect(dc,self.nID['D1'][0:int(p.numAll*(percentageN/100.0))] , 'all_to_all', syn_dict)	
	
		syn_dict =  synparamNoise['D2']	
		#nest.Connect(dc, self.nID['D2'][0:int(p.numAll*(percentageN/100.0))], 'all_to_all',  syn_dict)

		syn_dict =  synparamNoise['FSN']	
		#nest.Connect(dc, self.nID['FSN'][0:int(p.numFSI*(percentageN/100.0))], 'all_to_all', syn_dict)

		syn_dict =  synparamNoise['STN']	
		nest.Connect(dc, self.nID['STN'][0:int(p.numstn*(percentageN/100.0))], 'all_to_all', syn_dict)


	def createPoisson(self,noise, synparamNoise, rateD1, rateD2,p):
		# Creates poisson generators with the desired parameters noise
		#
		#w1 = 3.0
		#w2 = 3.0
		#w3 = 4.5
		#j02 = 0.55
		
		print("RateD1 = ", rateD1, "RateD2 = ",rateD2)
		self.noiseID = dict()
		

		for i in noise:
			self.noiseID[i] = nest.Create("poisson_generator",1,noise[i])
		
		
		# Connect the CTX to BG neurons
		for i in self.noiseID:
			nest.Connect(self.noiseID[i],self.nID[i], 'all_to_all',synparamNoise[i])

			'''
			if(i=="GPI"):
				syn_dict = {'weight':4.,'delay':1}
				pg_Gpi = nest.Create('poisson_generator',1,{'rate':100., 'start':100., 'stop':300.})
				endIndx = int(len(self.nID['GPI'])/4)
				nest.Connect(pg_Gpi, self.nID['GPI'][0:endIndx],'all_to_all',syn_dict)
			'''
			'''			
			pg_d1 = []
			pg_d2 = []
			if(i=="D1"):
				pg_d1 = nest.Create('poisson_generator',1,{'rate':(rateD1/float(num01))})
				#st01_list=[]
				for i in range(round(num1/2)):
					self.st01_list.append(nest.Create('parrot_neuron',num01))
				

				syn_dict = {'weight':j02,'delay': 1.0}
				nest.Connect(pg_d1,np.array(self.st01_list[:int(num1/2)]).flatten().tolist(),'all_to_all',syn_dict)
				p = 0
				for msn in (self.nID['D1']):
					#print("MSN = ", msn)
					#print(st01_list[p])
					conn_dict = {'rule': 'fixed_indegree', 'indegree': (len(self.st01_list[p]))}
					syn_dict = {'weight':w1,'delay': 1.0}
					nest.Connect(self.st01_list[p],[msn],conn_dict, syn_dict)							 
					p = p + 1

				self.detect_cortex_d1 = nest.Create("spike_detector")
				nest.SetStatus(self.detect_cortex_d1,{"withgid" : True , "withtime" : True })
				print("CTX_D1 Spike detector ",self.detect_cortex_d1)
				nest.Connect(self.st01_list[0],self.detect_cortex_d1)
				
				#ctx_ip_d1 = nest.Create('poisson_generator',1,{'rate':rateD1/1.0,'start':0.0,'stop':500000.})
				#syn_dict = {'weight':w1*j02,'delay':1.0}
				#nest.SetDefaults("static_synapse", syn_dict)
				#nest.Connect(ctx_ip_d1,self.nID[i],'all_to_all',syn_spec="static_synapse")
				
			elif(i=="D2"):
				pg_d2 = nest.Create('poisson_generator',1,{'rate':(rateD2/float(num01))})
				#st01_list=[]
				for i in range(round(num1/2)):
					self.st01_list.append(nest.Create('parrot_neuron',num01))				
				
				syn_dict = {'weight':j02,'delay': 1.0}
				nest.Connect(pg_d2,np.array(self.st01_list[int(num1/2):num1]).flatten().tolist(),'all_to_all',syn_dict)

				p = int(num1/2)
				for msn in (self.nID['D2']):
					#print("MSN = ", msn)
					#print(st01_list[p])
					conn_dict = {'rule': 'fixed_indegree', 'indegree': (len(self.st01_list[p]))} 
					syn_dict = {'weight':w2,'delay': 1.0}
					nest.Connect(self.st01_list[p],[msn],conn_dict, syn_dict)							 
					p = p + 1

				self.detect_cortex_d2 = nest.Create("spike_detector")
				nest.SetStatus(self.detect_cortex_d2,{"withgid" : True , "withtime" : True })
				print("CTX_D2 Spike detector ",self.detect_cortex_d2)				
				nest.Connect(self.st01_list[int(num1/2)+2],self.detect_cortex_d2)

				#ctx_ip_d2 = nest.Create('poisson_generator',1,{'rate':rateD2/1.0,'start':0.0,'stop':500000.})
				#syn_dict = {'weight':w2*j02,'delay':1.0}
				#nest.SetDefaults("static_synapse", syn_dict)
				#nest.Connect(ctx_ip_d2,self.nID[i],'all_to_all',syn_spec="static_synapse")
				
			elif(i=="FSN"):
				pg_fsi = nest.Create('poisson_generator',1,{'rate':float(rateD2)})
				syn_dict = {'weight':w3,'delay': 1.0}					
				#nest.Connect(pg_fsi, self.nID[i],'all_to_all',syn_dict)							
			
				#ctx_ip_fsn = nest.Create('poisson_generator',1,{'rate':rateD2/1.0,'start':0.0,'stop':500000.0})
				#syn_dict = {'weight':w3}
				#nest.Connect(ctx_ip_fsn,self.nID[i],'all_to_all',syn_dict)
			'''	
			print('Connected poisson to: ',i,synparamNoise[i],noise[i])
			



	def connect(self, nparam,p,cparam,synparam, noise, connections, pparam=True,poisson = True):
		# Connects the network using cparam
		#

		if pparam == True:
			for TARGET in self.nID:
				for SOURCE in connections[TARGET]:
					if connections[TARGET][SOURCE]:
						if SOURCE not in ["CTX"]:
							#Connect nodes to each other
							
							
							nest.Connect(self.nID[SOURCE],self.nID[TARGET],"one_to_one",synparam[TARGET][SOURCE])
							print("Connected "+SOURCE+" to "+TARGET)


		else:
			for TARGET in self.nID:
				for SOURCE in connections[TARGET]:
					if connections[TARGET][SOURCE]:
						if SOURCE not in ["CTX"]:
							#Connect nodes to each other
							
							
							nest.Connect(self.nID[SOURCE],self.nID[TARGET],{'rule': 'fixed_indegree', 'indegree': cparam[TARGET][SOURCE],'autapses': False, 'multapses': False},synparam[TARGET][SOURCE])
							#nest.Connect(self.nID[SOURCE],self.nID[TARGET],{'rule': 'fixed_outdegree', 'outdegree': cparam[TARGET][SOURCE],'autapses': False, 'multapses': False},synparam[TARGET][SOURCE]) # Ani

							print("Connected "+SOURCE+" to "+TARGET + " with synparam "+ str(synparam[TARGET][SOURCE]))



