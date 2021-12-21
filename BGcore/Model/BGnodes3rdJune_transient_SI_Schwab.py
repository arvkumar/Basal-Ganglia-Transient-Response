# Base model class where all other classes should be derived from
# BGnodes take two arguments : nparam = neuron parameters (dictionary), pparam = population parameters (dictionary)
import os
import sys
#sys.path.insert(0, "/home/aniruddha/NEST/BGnetwork-BGnetwork-edits/")
import tls as tls

import nest
import nest.raster_plot
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from collections import Counter
#import BGcore.Simulations.BasalFiring.param_val_Transient2ndApril as params
#import BGcore.Model.TCSRaster 
import pylab
from pylab import show, savefig
import copy

#p = params.get_parameters()  

class BGnodes:
	#kingshuk added for our own raster plot
	__all__ = [
	    'extract_events',
	    'from_data',
	    'from_device',
	    'from_file',
	    'from_file_numpy',
	    'from_file_pandas',
	    'show',
	    'savefig',
	]


	def extract_events(data, time=None, sel=None):
		"""Extract all events within a given time interval.
		Both time and sel may be used at the same time such that all
		events are extracted for which both conditions are true.
		Parameters
		----------
		data : list
		Matrix such that
		data[:,0] is a vector of all node_ids and
		data[:,1] a vector with the corresponding time stamps.
		time : list, optional
		List with at most two entries such that
		time=[t_max] extracts all events with t< t_max
		time=[t_min, t_max] extracts all events with t_min <= t < t_max
		sel : list, optional
		List of node_ids such that
		sel=[node_id1, ... , node_idn] extracts all events from these node_ids.
		All others are discarded.
		Returns
		-------
		numpy.array
		List of events as (node_id, t) tuples
		"""
		val = []

		if time:
			t_max = time[-1]
		if len(time) > 1:
			t_min = time[0]
		else:
			t_min = 0

		for v in data:
			t = v[1]
			node_id = v[0]
			if time and (t < t_min or t >= t_max):
				continue
			if not sel or node_id in sel:
				val.append(v)

		return np.array(val)


	
	def _from_memory(self,detec):
		ev = nest.GetStatus(detec,keys = "events")[0]
		print("Inside _from_memory....................", len(ev["times"]), "trucated version ", len(ev["times"][100:len(ev["times"])]))
		return ev["times"], ev["senders"]

	def from_tcsdevice(self,subplt_indx,detec, neuronDevice, **kwargs):
		"""
		Plot raster from a spike detector.
		Parameters
		----------
		detec : TYPE
		Description
		kwargs:
		Parameters passed to _make_plot
		Raises
		------
		nest.kernel.NESTError
		"""

		type_id = True
		if type_id:
		
			TRUNCPOINT = 0.0
			ts_o, node_ids_o = self._from_memory(detec)
			res = [idx for idx, val in enumerate(ts_o) if val > TRUNCPOINT] 
			ts = ts_o[res]
			node_ids = node_ids_o[res]

			if not len(ts):
				#raise nest.kernel.NESTError("No events recorded!")
				print("No events recorded!")
			else:
				if "title" not in kwargs:
					kwargs["title"] = "Raster plot from device '%i'" % detec.get('global_id')

				#if detec.get('time_in_steps'):
				#	xlabel = "Steps"
				#else:
				xlabel = "Time (ms)"

				return self._make_plot(subplt_indx,ts, ts, node_ids, node_ids, neuronDevice, xlabel=xlabel,**kwargs)

		elif detec.get("record_to") == "ascii":
			fname = detec.get("filenames")
			return from_file(fname, **kwargs)

		else:
			raise nest.kernel.NESTError("No data to plot. Make sure that \
				record_to is set to either 'ascii' or 'memory'.")




	#def _make_plot(self,subplt_indx, ts, ts1, node_ids, neurons, neuronDevice, hist=True, hist_binwidth=5.0,
	#	       grayscale=False, title=None, xlabel=None):
	def _make_plot(self,subplt_indx, ts, ts1, node_ids, neurons, neuronDevice, grayscale=False, **kwargs):
		xlabel = kwargs['xlabel']
		hist = kwargs['hist']
		title = kwargs['title']
		hist_binwidth = kwargs['hist_binwidth']

		"""Generic plotting routine.
		Constructs a raster plot along with an optional histogram (common part in
		all routines above).
		Parameters
		----------
		ts : list
		All timestamps
		ts1 : list
		Timestamps corresponding to node_ids
		node_ids : list
		Global ids corresponding to ts1
		neurons : list
		Node IDs of neurons to plot
		hist : bool, optional
		Display histogram
		hist_binwidth : float, optional
		Width of histogram bins
		grayscale : bool, optional
		Plot in grayscale
		title : str, optional
		Plot title
		xlabel : str, optional
		Label for x-axis
		"""
		#pylab.figure()

		if grayscale:
			color_marker = ".k"
			color_bar = "gray"
		else:
			color_marker = "p"
			color_bar = "blue"
		color_edge = "black"

		if xlabel is None:
			xlabel = "Time (ms)"

		ylabel = "Neuron ID"
		print("hist_binwidth**************************************",hist_binwidth)
		if hist:
			
			#ax1 = pylab.axes([0.1, 0.3, 0.85, 0.6])
			#self.axs_raster[subplt_indx].axes([0.1, 0.3, 0.85, 0.6])

			plotid1 = self.axs_raster[subplt_indx].plot(ts1, node_ids, color_marker)
			pylab.ylabel(ylabel)
			pylab.xticks([])
			xlim = pylab.xlim()
			#pylab.axes([0.1, 0.1, 0.85, 0.17])
			
			t_bins = np.arange(np.amin(ts), np.amax(ts),float(hist_binwidth))
			n, bins = self._histogram(ts, bins=t_bins)
			#print("------------------------", n, bins)
			#num_neurons = len(np.unique(neurons))

			num_neurons = (float(len(self.nID[neuronDevice])))

			print("####################### = ", subplt_indx, num_neurons)
			heights = 1000* n / (hist_binwidth * num_neurons)
			plotid = self.axs[subplt_indx].bar(t_bins, heights, width=hist_binwidth, color=color_bar,edgecolor=color_edge)
			#mng.window.showMaximized()
			if not len(heights):
				print("Null output in histogram")
			else:
				self.axs[subplt_indx].set_yticks([int(x) for x in np.linspace(0.0, int(max(heights) * 1.1) + 5, 4)])
	
			self.axs[subplt_indx].set_ylabel("Rate (Hz)")
			pylab.xlabel(xlabel)
			'''			
			if(subplt_indx == 0 or subplt_indx == 1 or subplt_indx  == subplt_indx == 3):
				UB = 10
			elif( subplt_indx == 5):
				UB = 50
			else:
				UB = 100
			self.axs[subplt_indx].set_ylim(0,UB)
			'''
			self.axs[subplt_indx].set_xlim(0, p.runtime) #(250, 400) #Assuming the stimulation is at 300msec
			#pylab.axes(ax1)
			#self.axs[subplt_indx].set_axes([0.1, 0.1, 0.85, 0.17])
			
		else:
			plotid = pylab.plot(ts1, node_ids, color_marker)
			pylab.xlabel(xlabel)
			pylab.ylabel(ylabel)

		if title is None:
			self.axs[subplt_indx].title.set_text("Raster plot")
			self.axs_raster[subplt_indx].title.set_text("Raster plot")
		else:
			print("Title ======",  title)
			self.axs[subplt_indx].title.set_text(title)
			self.axs_raster[subplt_indx].title.set_text(title)
			self.axs_raster[subplt_indx].set_xlim(0, p.runtime) #(250, 400) #Assuming the stimulation is at 300msec
		pylab.draw()

		return plotid1, plotid


	
	def _histogram(self,a, bins=10, bin_range=None, normed=False):
		"""Calculate histogram for data.
		Parameters
		----------
		a : list
		Data to calculate histogram for
		bins : int, optional
		Number of bins
		bin_range : TYPE, optional
		Range of bins
		normed : bool, optional
		Whether distribution should be normalized
		Raises
		------
		ValueError
		"""
		from numpy import asarray, iterable, linspace, sort, concatenate

		a = asarray(a).ravel()
		if bin_range is not None:
			mn, mx = bin_range
			if mn > mx:
				raise ValueError("max must be larger than min in range parameter")
		if not iterable(bins):
			if bin_range is None:
				bin_range = (a.min(), a.max())
			mn, mx = [mi + 0.0 for mi in bin_range]
			if mn == mx:
				mn -= 0.5
				mx += 0.5
			bins = linspace(mn, mx, bins, endpoint=False)
		else:
			if (bins[1:] - bins[:-1] < 0).any():
				raise ValueError("bins must increase monotonically")

	    # best block size probably depends on processor cache size
		block = 65536
		n = sort(a[:block]).searchsorted(bins)
		for i in range(block, a.size, block):
			n += sort(a[i:i + block]).searchsorted(bins)
		n = concatenate([n, [len(a)]])
		n = n[1:] - n[:-1]

		if normed:
			db = bins[1] - bins[0]
			return 1.0 / (a.size * db) * n, bins
		else:
			return n, bins



	def get_histogram_data(self, neuronDevice,hist_binwidth,p):
		ev = nest.GetStatus(self.spikeID[neuronDevice],keys = "events")[0]
		t_bins = np.arange(0, p.runtime, float(hist_binwidth))
		n, bins = self._histogram(ev["times"], bins=t_bins)
		num_neurons = (float(len(self.nID[neuronDevice])))
		heights = 1000* n / (hist_binwidth * num_neurons)
		print("%%%%%%%%%%%%%%%%%%%%%%%%",len(t_bins))
		return t_bins, heights



	def __init__(self,nparam, dopAlpha, p,pparam = True):
		# nparam must be a dictionary of the form nparam = {"neuron" : {"param1": var, "param2" : var}}
		# pparam must be a dictionary of the form pparam = {"neuron" : population}
		# nID = the device ID given from nest at creation
		nest.SetKernelStatus({"local_num_threads": 4})
		self.ctx = -1
		self.detect_cortex_d1 = -1
		self.detect_cortex_d2 = -1
		self.st01_list=[]
		#self.nID = {"D1" : None, "D2" : None,  "FSN" : None, "GPTA":None, "GPTI":None}
		#self.nModel = {"D1" :"iaf_cond_alpha" , "D2" : "iaf_cond_alpha", "FSN" : "iaf_cond_alpha", 
		#			 "GPTA" : "aeif_cond_exp", "GPTI" : "aeif_cond_exp" }
		#self.nID = {"D1" : None, "D2" : None,  "FSN" : None}
		#self.nModel = {"D1" :"iaf_cond_alpha" , "D2" : "iaf_cond_alpha", "FSN" : "iaf_cond_alpha"}
		self.nID = {"D1" : None, "D2" : None, "FSN" : None, "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None}
		self.nModel = {"D1" :"iaf_cond_alpha" , "D2" : "iaf_cond_alpha", "FSN" : "iaf_cond_alpha", 
					  "GPI" : "aeif_cond_exp", "GPTA" : "aeif_cond_exp", "GPTI" : "aeif_cond_exp", "STN" : "iaf_cond_alpha"}
		
		#nest.SetDefaults('aeif_cond_exp',{'gsl_error_tol': 1e-06})I

		self.fig, self.axs = plt.subplots(7)
		self.fig.set_figheight(25)
		self.fig.set_figwidth(15)
		self.fig_raster, self.axs_raster = plt.subplots(7)
		self.fig_raster.set_figheight(25)
		self.fig_raster.set_figwidth(15)


		
		for ID in self.nID :
			#print("Nparam = ",nparam[ID])
			

			if pparam == True:
				self.nID[ID] = nest.Create(self.nModel[ID],1,nparam[ID])
				
			else:
				print(ID)
				print(pparam[ID])
				print('ID:',nparam[ID])
				
				self.nID[ID] = nest.Create(self.nModel[ID],int(pparam[ID]),nparam[ID])
				if (ID == "D1") or (ID == "D1A1") or (ID == "D1A2"):					
					vid1 = np.random.uniform(p.vi1low,p.vi1hi,int(pparam[ID]))
					vidl = vid1.tolist()
					nest.SetStatus(self.nID[ID],params="V_m",val=vidl)

					"""
					# Set for dopamine level
					vth = p.thD1*(1+p.beta_V_thD1*(dopAlpha - p.dopAlpha_0))
					vthd1 = np.random.uniform(vth,vth,int(pparam[ID]))
					vthd1l = vthd1.tolist()
					nest.SetStatus(self.nID[ID],params="V_th",val=vthd1l)

					E_L = p.vm1*(1+p.beta_E_LD1*(dopAlpha - p.dopAlpha_0))
					E_Ld1 = np.random.uniform(E_L,E_L,int(pparam[ID]))
					E_Ld1l = E_Ld1.tolist()
					nest.SetStatus(self.nID[ID],params="V_reset",val=E_Ld1l)
					nest.SetStatus(self.nID[ID],params="E_L",val=E_Ld1l)
					"""
					
				elif(ID == "D2") or (ID == "D2A1") or (ID == "D2A2"):					
					vid1 = np.random.uniform(p.vi1low,p.vi1hi,int(pparam[ID]))
					vidl = vid1.tolist()
					nest.SetStatus(self.nID[ID],params="V_m",val=vidl)
				
				elif(ID == "FSN"):				
					vifsi = np.random.uniform(p.vi3low,p.vi3hi,int(pparam[ID]))
					vifsil = vifsi.tolist()
					nest.SetStatus(self.nID[ID],params="V_m",val=vifsil)
					"""
					# Set for dopamine level					
					vm = p.vm*(1+p.beta_VrFSN*(dopAlpha - p.dopAlpha_0))
					vresetFSN = np.random.uniform(vm,vm,int(pparam[ID]))
					vresetFSNl = vresetFSN.tolist()
					nest.SetStatus(self.nID[ID],params="V_reset",val=vresetFSNl)
					nest.SetStatus(self.nID[ID],params="E_L",val=vresetFSNl)
					"""

				elif(ID == "GPTA"):
					viTA = np.random.uniform(p.viTAlow,p.viTAhi,int(pparam[ID]))
					viTAl = viTA.tolist()
					nest.SetStatus(self.nID[ID],params="V_m",val=viTAl)
				
					"""
					# Set for dopamine level				
					E_L = -55.1*(1+p.beta_E_LTA*(dopAlpha - p.dopAlpha_0)) #"E_L":-55.1
					E_LTA = np.random.uniform(E_L,E_L,int(pparam[ID]))
					E_LTAl = E_LTA.tolist()
					nest.SetStatus(self.nID[ID],params="E_L",val=E_LTAl)
					"""
	
				elif(ID == "GPTI") or (ID == "GPTIA1") or (ID == "GPTIA2"):
					viTI = np.random.uniform(p.viTIlow,p.viTIhi,int(pparam[ID]))
					viTIl = viTI.tolist()
					nest.SetStatus(self.nID[ID],params="V_m",val=viTIl)

					"""
					# Set for dopamine level
					E_L = -55.1*(1+p.beta_E_LTI*(dopAlpha - p.dopAlpha_0)) #"E_L":-55.1
					E_LTI = np.random.uniform(E_L,E_L,int(pparam[ID]))
					E_LTIl = E_LTI.tolist()
					nest.SetStatus(self.nID[ID],params="E_L",val=E_LTIl)
					"""
				
				elif(ID == "STN") or (ID == "STNA1") or (ID == "STNA2"):
					vistn = np.random.uniform(p.vistnlow, p.vistnhi, int(pparam[ID]))
					vistnl = vistn.tolist()
					nest.SetStatus(self.nID[ID], params="V_m", val=vistnl)

				elif(ID == "GPI") or (ID == "GPIA1") or (ID == "GPIA1"):
					viGPI = np.random.uniform(p.viGPIlow, p.viGPIhi, int(pparam[ID]))
					viGPIl = viGPI.tolist()
					nest.SetStatus(self.nID[ID], params="V_m", val=viGPIl)
					
					"""
					# Set for dopamine level
					E_L = -55.8*(1+p.beta_E_LGPI*(dopAlpha - p.dopAlpha_0)) #"E_L":-55.8
					E_LGPI = np.random.uniform(E_L,E_L,int(pparam[ID]))
					E_LGPIl = E_LGPI.tolist()
					nest.SetStatus(self.nID[ID],params="E_L",val=E_LGPIl)
					"""


	def createInputSlowV3(self,synparamNoise, pparam, percentageN, voltageForStimulation,p,CTXpopsize,SlowIPStimulationStartPoint):
		#spiktimes = [random.randint(SlowIPStimulationStartPoint, SlowIPStimulationStartPoint+p.slowip_dur) for i in range(p.slowip_nospikes)] 

		#spiketimes_VarovrTrials = np.sort((p.slowip_dur*0.5)*np.random.randn(p.slowip_nospikes) + SlowIPStimulationStartPoint+p.slowip_dur/2)

		#spiketimes = spiketimes_VarovrTrials
		#print("spiketimes",SlowIPStimulationStartPoint,p.spiketimes_FixedovrTrials)


		spiketimes = p.spiketimes_FixedovrTrials +  SlowIPStimulationStartPoint +  p.slowip_dur/2 #not varying ove trials
		print("spiketimes",SlowIPStimulationStartPoint,p.spiketimes_FixedovrTrials)

		slowip = nest.Create('spike_generator',p.slowip_nospikes)#, params = {'spike_times': np.array([10.0, 20.0, 50.0])})

		a = []
		for k in range(len(spiketimes)):
			a.append(round(float(spiketimes[k]),1))
			nest.SetStatus([slowip[k]],params = {'spike_times':[a[k]]})

			indicesD1 = random.sample(range(0, int(p.numAll)), int(p.numAll*(percentageN/100.0)))
			indicesD2 =  random.sample(range(0,int(p.numAll)), int(p.numAll*(percentageN/100.0)))
			indicesFSN = random.sample(range(0,int(p.numFSI)), int(p.numFSI*(percentageN/100.0)))
			indicesSTN = random.sample(range(0,int(p.numstn)), int(p.numstn*(percentageN/100.0)))


			syn_dict =  copy.deepcopy(synparamNoise['D1'])
			syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd1*.3 # This is done to get the required strength with one neuron
			nest.Connect([slowip[k]],[ self.nID['D1'][i] for i in indicesD1 ], 'all_to_all', syn_dict)

			syn_dict =  copy.deepcopy(synparamNoise['D2'])	
			syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd2*.3
			nest.Connect([slowip[k]],[ self.nID['D2'][i] for i in indicesD2 ], 'all_to_all', syn_dict)

			syn_dict =  copy.deepcopy(synparamNoise['FSN'])
			syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxfsn*.3
			nest.Connect([slowip[k]],[ self.nID['FSN'][i] for i in indicesFSN ], 'all_to_all', syn_dict)


			syn_dict =  copy.deepcopy(synparamNoise['STN'])	
			syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxstn*.3
			nest.Connect([slowip[k]],[ self.nID['STN'][i] for i in indicesSTN ], 'all_to_all', syn_dict)

			
	def createInputTransientV3(self,synparamNoise, pparam, percentageN, voltageForStimulation,p,CTXpopsize,pg,D1pg,D2pg,FSNpg,STNpg):
		#m = 1.5

		print(synparamNoise['D1'])
		print(synparamNoise['D2'])
		print(synparamNoise['STN'])

		syn_dict =  copy.deepcopy(synparamNoise['D1'])
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd1 # This is done to get the required strength with one neuron
		conn_dict = {'rule': 'fixed_indegree', 'indegree': len(pg)}
		nest.Connect(D1pg, self.nID['D1'][0:int(p.numAll*(percentageN/100.0))] , conn_dict , syn_dict)
		print("for D1",syn_dict["weight"],p.tx_jctxd1)	
	
		syn_dict =  copy.deepcopy(synparamNoise['D2'])	
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd2
		conn_dict = {'rule': 'fixed_indegree', 'indegree': len(pg)}
		nest.Connect(D2pg, self.nID['D2'][0:int(p.numAll*(percentageN/100.0))], conn_dict ,  syn_dict)
		print("for D2",syn_dict["weight"],p.tx_jctxd2)

		syn_dict =  copy.deepcopy(synparamNoise['FSN'])
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxfsn
		conn_dict = {'rule': 'fixed_indegree', 'indegree': len(pg)}
		nest.Connect(FSNpg, self.nID['FSN'][0:int(p.numFSI*(percentageN/100.0))], conn_dict, syn_dict)
		print("for FSN",syn_dict["weight"],p.tx_jctxfsn)

		syn_dict =  copy.deepcopy(synparamNoise['STN'])	
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxstn
		conn_dict = {'rule': 'fixed_indegree', 'indegree': len(pg)}
		nest.Connect(STNpg, self.nID['STN'][0:int(p.numstn*(percentageN/100.0))], conn_dict, syn_dict)
		print("for STN",syn_dict["weight"],p.tx_jctxstn)


	def createInputTransientV2(self,synparamNoise, pparam, percentageN, voltageForStimulation,p,CTXpopsize):
		#m = 1.5
		print("int(CTXpopsize)--",int(CTXpopsize))
		self.ctx = nest.Create('iaf_cond_alpha',int(CTXpopsize))
		pot = np.random.uniform(20., 20., int(CTXpopsize))
		pot = pot.tolist()
		nest.SetStatus(self.ctx, params="V_m", val=pot) #'V_m', -50.0)

		print(synparamNoise['D1'])
		print(synparamNoise['D2'])
		print(synparamNoise['STN'])
		syn_dict =  copy.deepcopy(synparamNoise['D1'])
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd1 # This is done to get the required strength with one neuron
		nest.Connect(self.ctx,self.nID['D1'][0:int(p.numAll*(percentageN/100.0))] , 'all_to_all', syn_dict)
		print("for D1",syn_dict["weight"])	
	
		syn_dict =  copy.deepcopy(synparamNoise['D2'])	
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxd2
		nest.Connect(self.ctx, self.nID['D2'][0:int(p.numAll*(percentageN/100.0))], 'all_to_all',  syn_dict)
		print("for D2",syn_dict["weight"])

		syn_dict =  copy.deepcopy(synparamNoise['FSN'])
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxfsn
		nest.Connect(self.ctx, self.nID['FSN'][0:int(p.numFSI*(percentageN/100.0))], 'all_to_all', syn_dict)
		print("for FSN",syn_dict["weight"])

		syn_dict =  copy.deepcopy(synparamNoise['STN'])	
		syn_dict["weight"] = syn_dict["weight"]*p.tx_jctxstn
		nest.Connect(self.ctx, self.nID['STN'][0:int(p.numstn*(percentageN/100.0))], 'all_to_all', syn_dict)
		print("for STN",syn_dict["weight"])

		'''
		nest.SetStatus(self.nID['D1'][0:int(len(self.nID['D1'])*(percentageN/100.0))], params="V_m", val=voltageForStimulation[0]) #'V_m', -50.0)
		nest.SetStatus(self.nID['D2'][0:int(len(self.nID['D2'])*(percentageN/100.0))], params="V_m", val=voltageForStimulation[1]) #'V_m', -50.0)
		nest.SetStatus(self.nID['FSN'][0:int(len(self.nID['FSN'])*(percentageN/100.0))], params="V_m", val=voltageForStimulation[2]) #'V_m', -40.1)
		nest.SetStatus(self.nID['STN'][0:int(len(self.nID['STN'])*(percentageN/100.0))], params="V_m", val=voltageForStimulation[3]) #'V_m', -40.1)
		'''
		

		'''
		extraVm = 0.0
		vid1 = np.random.uniform(p.vi1low,p.vi1hi+extraVm,int(pparam['D1']/m))
		vidl = vid1.tolist()
		nest.SetStatus(self.nID['D1'][0:int(len(self.nID['D1'])/m)], params="V_m", val=vidl) #'V_m', -50.0) #1000.0	
		
		extraVm = 10.0
		vid1 = np.random.uniform(p.vi1low,p.vi1hi+extraVm,int(pparam['D2']/m))
		vidl = vid1.tolist()
		nest.SetStatus(self.nID['D2'][0:int(len(self.nID['D2'])/m)], params="V_m", val=vidl) #'V_m', -50.0) #1000.0

		extraVm = 0.0
		vifsi = np.random.uniform(p.vi3low,p.vi3hi+extraVm,int(pparam['FSN']/m))
		vifsil = vifsi.tolist()
		nest.SetStatus(self.nID['FSN'][0:int(len(self.nID['FSN'])/m)], params="V_m", val=vifsil) #'V_m', -40.1) #1000.0

		extraVm = 10.0
		vistn = np.random.uniform(p.vistnlow, p.vistnhi+extraVm, int(pparam['STN']/m))
		vistnl = vistn.tolist()
		nest.SetStatus(self.nID['STN'][0:int(len(self.nID['STN'])/m)], params="V_m", val=vistnl) #'V_m', -40.1) #1000.0
		'''

	def connectMultimeter(self,recordG = False): # Old, dont use this
		# Connects multimeter that records from V_m. Todo: record from other parameters as well
		if not recordG:
			self.multimeter = nest.Create("multimeter")
			nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m"]})

			for ID in self.nID: # Connects the multimeter to every node in the network
				nest.Connect(self.multimeter, self.nID[ID])

		else:
			self.multimeter = nest.Create("multimeter")
			nest.SetStatus(self.multimeter, {"withtime":True, "record_from":["V_m","g_ex"]})
			for ID in self.nID: # Connects the multimeter to every node in the network
				nest.Connect(self.multimeter, self.nID[ID])


	def connectMultimeterNew(self, recordG = False,**kwargs):
		self.multiID = dict()
		if not recordG:
			for ID in self.nID:
				self.multiID[ID] = nest.Create('multimeter')
				nest.SetStatus(self.multiID[ID],{'label' : ID, 'withtime': True,'record_from': ['V_m','g_ex','g_in'],'to_file' : False})
				if kwargs['to_file']:
					nest.SetStatus(self.multiID[ID],{'to_file':True})
				nest.Connect(self.multiID[ID], self.nID[ID])
			else:
				self.multiID[ID] = nest.Create('multimeter')
				nest.SetStatus(self.multiID[ID],{'label' : ID, 'withtime': True,'record_from': ['V_m','g_ex'],'to_file' : False})
				nest.Connect(self.multiID[ID], self.nID[ID])





	


	def connectSpikeDet(self):

		# Connects spike detector to every node
		self.spikeID = dict()
		#self.spikedetector = nest.Create("spike_detector",
                #params={"withgid": True, "withtime": True})

		for ID in self.nID:
			self.spikeID[ID] = nest.Create("spike_detector",1)
			nest.SetStatus(self.spikeID[ID], [{"label": ID,"withtime": True,"withgid": True, "to_file" : True}])
			nest.Connect(self.nID[ID], self.spikeID[ID])




	def simulate(self, t):
		nest.Simulate(float(t))

	def plotRaster(self,device,R1,R2,Hz,subplt_indx,percentageN, dirname, outFileName):
		#self.axs[subplt_indx].set_xlim(0,550)
		#nest.raster_plot.from_device(self.spikeID[device], hist = True, hist_binwidth=.1, title= device+' activity')
		#self.from_tcsdevice(subplt_indx,self.spikeID[device], hist = True, hist_binwidth=.1, title= device+' activity')
		
		IMAGEFOLDERPATH = "images/"+dirname 
		#nest.raster_plot.show()
		if subplt_indx == 6:
			if not os.path.exists(IMAGEFOLDERPATH):
			    os.makedirs(IMAGEFOLDERPATH)
			self.from_tcsdevice(subplt_indx,self.spikeID[device], device, hist = True, hist_binwidth=1., title= device+' activity '+str(percentageN))
			self.fig.savefig(IMAGEFOLDERPATH+'SingleTrialSample_'+device+'_'+str(outFileName)+'_N='+str(percentageN)+'percnt'+'.png')
			self.fig_raster.savefig(IMAGEFOLDERPATH+'SingleTrialSample_'+ device+'_'+str(outFileName)+'_N='+str(percentageN)+'percnt'+'_Raster.png')
		else:
			self.from_tcsdevice(subplt_indx,self.spikeID[device], device, hist = True, hist_binwidth=1., title= device+' activity '+str(percentageN))
			

	def get_G(self):

		self.G = {
					"GPTA" : { "G" : np.array([]), "t" : np.array([])},
					"GPTI" : { "G" : np.array([]), "t" : np.array([])},
					"STN" : { "G" : np.array([]), "t" : np.array([])},
					"GPI" : { "G" : np.array([]), "t" : np.array([])},
					"D1" : { "G" : np.array([]), "t" : np.array([])},
					"D2" : { "G" : np.array([]), "t" : np.array([])},
					"FSN" : { "G" : np.array([]), "t" : np.array([])}
					}
		x = (0,1,2)
		it = list(product(x,x))
		names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
		dmm = nest.GetStatus(self.multimeter)[0]
		
		
		for i in range(7):
		    g = dmm["events"]["g_ex"][i::7]
		    ts = dmm["events"]["times"][i::7]
		    d = self.G[names[i]]
		    d["G"] = g
		    d["t"] = ts
		return self.G



	def plot_G(self,name =1):
		if name == 1:
			G = self.get_G()
			x = (0,1,2)
			it = list(product(x,x))
			names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
			
			fig, axes = plt.subplots(3, 3)
			for i in range(7):
			    
			    axes[it[i]].plot(G[names[i]]["t"], G[names[i]]["G"])
			    axes[it[i]].set_title(names[i])
			    axes[it[i]].set_xlabel('ms')
			    axes[it[i]].set_ylabel('G')
			    #axes[it[i]].set_xlim((0,200))

			fig.set_dpi(70)
			fig.set_size_inches(8, 6)
			plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
			plt.show()
		else:
			G = self.get_G()
			fig, axes = plt.subplots(1, 1)
			print(sum(G[name]["G"]))
			plt.plot(G[name]["t"], G[name]["G"])
			plt.title(name)
			plt.xlabel('ms')
			plt.ylabel('G')
			plt.show()



	def getVmNew(self,device):
		self.vm = {
					"GPTA" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPTI" : { "Vm" : np.array([]), "t" : np.array([])},
					"STN" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPI" : { "Vm" : np.array([]), "t" : np.array([])},
					"D1" : { "Vm" : np.array([]), "t" : np.array([])},
					"D2" : { "Vm" : np.array([]), "t" : np.array([])},
					"FSN" : { "Vm" : np.array([]), "t" : np.array([])}
					}
		return nest.GetStatus(self.multiID[device])


	def get_vm(self): # Retrieves the membrane potential data and return it as a dictionary
			
		self.vm = {
					"GPTA" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPTI" : { "Vm" : np.array([]), "t" : np.array([])},
					"STN" : { "Vm" : np.array([]), "t" : np.array([])},
					"GPI" : { "Vm" : np.array([]), "t" : np.array([])},
					"D1" : { "Vm" : np.array([]), "t" : np.array([])},
					"D2" : { "Vm" : np.array([]), "t" : np.array([])},
					"FSN" : { "Vm" : np.array([]), "t" : np.array([])}
					}
		x = (0,1,2)
		it = list(product(x,x))
		names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
		dmm = nest.GetStatus(self.multimeter)[0]
		
		
		for i in range(7):
		    Vms = dmm["events"]["V_m"][i::7]
		    ts = dmm["events"]["times"][i::7]
		    d = self.vm[names[i]]
		    d["Vm"] = Vms
		    d["t"] = ts
		return self.vm



	def plotVm(self,name = 1):
		if name == 1:
			vm = self.get_vm()
			x = (0,1,2)
			it = list(product(x,x))
			names = ["D1","D2","STN","GPI","GPTA", "GPTI","FSN"]
			
			fig, axes = plt.subplots(3, 3)
			for i in range(7):
			    
			    axes[it[i]].plot(vm[names[i]]["t"], vm[names[i]]["Vm"])
			    axes[it[i]].set_title(names[i])
			    axes[it[i]].set_xlabel('ms')
			    axes[it[i]].set_ylabel('Vm')
			    #axes[it[i]].set_xlim((0,200))

			fig.set_dpi(70)
			fig.set_size_inches(8, 6)
			plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
			plt.show()
		else:
			vm = self.get_vm()
			fig, axes = plt.subplots(1, 1)
			plt.plot(vm[name]["t"], vm[name]["Vm"])
			plt.title(name)
			plt.xlabel('ms')
			plt.ylabel('Vm')
			plt.show()

	def countSpikes(self,p):
		freq_node=["D1","D2","FSN","GPTA","GPTI","STN","GPI"]
		
		self.freq ={ "D1" : None, "D2" : None, "FSN" : None, "GPTA" : None, "GPTI" : None, "STN": None, "GPI" : None}

		spike_event_list = []
		mn_freq = []
		mn_freq2 = []
		SimulationTime = p.ctxEndInputtime - p.ctxStartInputtime # 500.0
		secs =  float(SimulationTime)/1000.
		
		for ID in freq_node:
			dSD = nest.GetStatus(self.spikeID[ID],keys="events")[0]
			evs = dSD["senders"]
			ts = dSD["times"]
			tsNew = [i for i in ts if p.ctxStartInputtime <= i < p.ctxEndInputtime ]

			spike_event_list.append(dSD)
			self.count = Counter(evs)
			self.freq[ID] = self.count[self.nID[ID][0]]
			#print("Start",self.nID[ID][0])
			#print("Variable = ", list(self.count.keys()));
			print("ID",ID, "Count = ",self.count )
			#'''
			if ID == "GPTI":
				list1= list(self.count.keys())
				#list2= list(self.count.values())
				list2 = self.count
				print("GPTI inh:", len(list(x for x in list1 if 4410 <= x <= 4410+858)) )
				a = list(x for x in list1 if 4410 <= x <= 4410+858)
				print(a)
				print("FR-----------------", [list2[x] for x in a])
				print("GPTI excited:", len(list(x for x in list1 if 4410+858 +1 <= x <= 4410+858+ 1+ 84)) )
				a = list(x for x in list1 if 4410+858 +1 <= x <= 4410+858+ 1+ 84)
				print("FR-----------------", [list2[x] for x in a])
				print("GPTI nothing:", len(list(x for x in list1 if 4410+858 +1 + 84 + 1 <= x <= 4410+858 +1 + 84 + 1 + 43 )) )
				a = list(x for x in list1 if 4410+858 +1 + 84 + 1 <= x <= 4410+858 +1 + 84 + 1 + 43)
				print("FR-----------------", [list2[x] for x in a])
			#'''
			#SimulationTime = p.ctxEndInputtime - p.ctxStartInputtime #500.0
			#secs =  float(SimulationTime)/1000.

			tmp2 = (len(tsNew)/secs)/(float(len(self.nID[ID])))
			mn_freq2.append(tmp2)
			print("ID: ",ID, " Mean freq: ",tmp2)
		'''
		dsd =[]
		dSD = nest.GetStatus(self.detect_cortex_d1,keys="events")[0]
		evs = dSD["senders"]
		ts = dSD["times"]
		tmp_d1 = (len(ts)/secs)/(float(150))
		mn_freq2.append(tmp_d1)
		dsd =[]
		dSD = nest.GetStatus(self.detect_cortex_d2,keys="events")[0]
		evs = dSD["senders"]
		ts = dSD["times"]
		tmp_d2	= (len(ts)/secs)/(float(150))
		mn_freq2.append(tmp_d2)		
		'''
		return spike_event_list, self.freq, mn_freq2


	def setIe(self,I_e,device = 1): # Set constant input current
		if device ==1:
			for ID in self.nID:
				nest.SetStatus(self.nID[ID],{"I_e" : float(I_e)})
		else:
			nest.SetStatus(self.nID[device],{"I_e" : float(I_e)})


if __name__ == '__main__':
	cparam = tls.importParam()
	# Building the pparam
	pparam = { "GPTA" : None, "GPTI" : None, "STN" : None, "GPI" : None, "D1" : None, "D2": None, "FSN" : None}
	for p in cparam:
		if p[0] in ["P"] and not p in ["P_n"]:
			pparam[p.split("_")[1]] = int(cparam[p])

	#print(pparam)
	BG1 = BGnodes(nparam)
	BG1.connectMultimeter(1234)
	BG1.connectSpikeDet()
	BG1.simulate(1000.0)
	BG1.setIe(0.0,"GPTA")
	BG1.simulate(1000.0)
	BG1.countSpikes()
	f = BG1.freq
	print(f)
	BG1.plot_G('GPTA')
