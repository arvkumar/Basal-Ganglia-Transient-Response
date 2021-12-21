import sys
sys.path.insert(0, "/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/")
import BGcore.tls as tls
import BGcore.Simulations.BasalFiring.paramtest8 as param # Desired parameters
import BGcore.Model.BGnodes
import BGcore.Model.BGnetwork as BG
import matplotlib.pyplot as plt
import nest
import time


# Pipeline
# 
# Step 1 : Create a py file with desired parameters. pparam, nparam, cparam, and connections. 
# Step 2: Use createParam that takes the params and exports them into json
# Step 3: Create object BGnetwork
# Step 4: Simulate and save to file
# Step 5: Analyse
# 
# 
#

#paramNEW= t.tune(param.nparam, param.cparamOLD, param.staticsyn, param.noise, param.staticsynNoise, param.connections)
#print("New syn ",paramNEW.synparam)
#print("/nOld syn ", param.staticsyn)
#print(paramNEW.pparam)

pop = 100

testPop = {

            'D1' : pop,
            'D2' : pop,
            'FSN' : pop,
            'STN' : pop,
            'GPTA' : pop,
            'GPTI' : pop,
            'GPI' : pop
}
nest.ResetKernel()
BG1 = BG.BGnetwork(param.nparam, param.cparam, param.staticsyn, param.noise,param.staticsynNoise, param.connections,param.pparam)
nest.SetKernelStatus({'data_path': '/Users/kimhedelin/Google Drive/VT18/Neuroscience/simulation/BGnetwork/sample/BasalFiring/data/', 'overwrite_files':True})
#BG1.connectMultimeterNew(to_file = True)
BG1.connectSpikeDet()
BG1.setIe(0.0)

currentTime = time.time()
BG1.simulate(500.0)

print('Simulation took: ', time.time()-currentTime)




plotVm = False
plotRaster = True
if plotVm: 

	fig, axes = plt.subplots(3, 3)
	
	dmm = BG1.getVmNew('D1')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 0
	v = 0
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('D1')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')


	dmm = BG1.getVmNew('D2')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 0
	v = 1
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('D2')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')
	

	dmm = BG1.getVmNew('FSN')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 0
	v = 2
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('FSN')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')



	dmm = BG1.getVmNew('GPI')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 1
	v = 0
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('GPI')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')



	dmm = BG1.getVmNew('GPTI')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 2
	v = 0
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('D1')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')



	dmm = BG1.getVmNew('GPTA')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 1
	v = 1
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('GPTA')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')


	dmm = BG1.getVmNew('STN')[0]

	
	#plt.plot(dmm['events']['V_m'][::pop])
	n = 2
	v = 2
	axes[(n,v)].plot(dmm['events']['times'][::pop], dmm['events']['V_m'][::pop])
	axes[(n,v)].set_title('STN')
	axes[(n,v)].set_xlabel('ms')
	axes[(n,v)].set_ylabel('Vm')



	


	fig.set_dpi(70)
	fig.set_size_inches(8, 6)
	plt.subplots_adjust(hspace = 0.5, wspace = 0.5)
	plt.show()
	

#BG1.connectSpikeDet()
#BG1.setIe(0.0)

#BG1.simulate(1000.0)
if plotRaster:
	
	BG1.plotRaster('D1')
	BG1.plotRaster('D2')
	BG1.plotRaster('FSN')
	BG1.plotRaster('GPI')
	BG1.plotRaster('GPTA')
	BG1.plotRaster('GPTI')
	BG1.plotRaster('STN')