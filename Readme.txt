Setup instruction
1. Download and unzip the code in your local folder (say, /home/username/Documents/arv contains the code)
2. open  arv/BGcore/Simulations/Templates/template_15thFeb_dop840_poisson_SI_V7.py
	-- set/update 
		==> sys.path.insert(0, "/home/username/Documents/arv/BGcore/")
	-- set/update 
		==> RESULTSFolder = "/home/username/Documents/arv/BGcore/Simulations/Templates/GDFS/" + PDState +"Trial" + str(numTrials)
3. create folders GDFS, images, images_2Apr21 (if they are not there)


For basal tuning
1. set p.BasalTuning = True in /BGcore/Simulations/BasalFiring/param_val_Transient11thNov_SI.py

For increase/decrease number of trials
1. set/update p.NUMTRIALS = NUMTRIALS (default NUMTRIALS = 100)


1. To generate Figure 3

	-- for normal, 
		-- change following in dopeffectArray = arr.array('f', [XX]) in /BGcore/Simulations/Templates/GenFigure3.py
			==> for normal/healthy, XX = 0.8
			==> for PD-biphasic/triphasic, XX = 0.0
		-- change  following in /BGcore/Simulations/BasalFiring/param_val_Transient11thNov_SI.py
			==> for PD biphasic, 
				-- set p.PD_BIPHASIC = True 
				-- set p.PD_TRIPHASIC = False
			==> for PD triphasic, 
				-- set p.PD_BIPHASIC = False 
				-- set p.PD_TRIPHASIC = True 

	-- Now given a setting (healthy/PD-biphasic/Triphasic)
		-- Run 
			>> python  GenFigure3.py Target OutputDirName 
	OUTPUT
		-- GDFS will be saved under /BGcore/Simulations/Templates/GDFS
		-- images would be saved under /BGcore/Simulations/Templates/images_2Apr21

	-- Postprocessing - How to generate only STNStimulation ?
                Input - From image folder i) Normal, PDbiphasic, Pdtriphasic ii) only STNStimulation - Normal, PDbiphasic, Pdtriphasic 
		MATLAB code Fig3.m, corticalinput_plot.m

2. To generate Figure 5
	-- For Normal

		open  arv/BGcore/Simulations/Templates/template_15thFeb_dop840_poisson_SI_V7_synwtchng4mnorm.py
		-- set/update 
			==> sys.path.insert(0, "/home/username/Documents/arv/BGcore/")
		-- set/update 
			==> RESULTSFolder = "/home/username/Documents/arv/BGcore/Simulations/Templates/GDFS/" + PDState + str(sys.argv[2]) + "/"+ str(mv) +"/Trial" + str(numTrials)

		-- Run
			>> python GenFigure5_synwtchng4mnorm.py Figure5_Normal
		OUTPUT
			-- GDFS will be saved under /BGcore/Simulations/Templates/GDFS
			-- images would be saved under /BGcore/Simulations/Templates/images

	-- For PD biphasic 

		open  arv/BGcore/Simulations/Templates/template_15thFeb_dop840_poisson_SI_V7_synwtchng4mPDBip.py
		-- set/update 
			==> sys.path.insert(0, "/home/username/Documents/arv/BGcore/")
		-- set/update 
			==> RESULTSFolder = "/home/username/Documents/arv/BGcore/Simulations/Templates/GDFS/" + PDState + str(sys.argv[2]) + "/"+ str(mv) +"/Trial" + str(numTrials)

		-- change  following in /BGcore/Simulations/BasalFiring/param_val_Transient11thNov_SI.py
			-- set p.PD_BIPHASIC = True 
			-- set p.PD_TRIPHASIC = False 

		-- Run
			>> python GenFigure5_synwtchng4mPDBip.py OutputDirName
		OUTPUT
			-- GDFS will be saved under /BGcore/Simulations/Templates/GDFS
			-- images would be saved under /BGcore/Simulations/Templates/images

	-- For PD triphasic 

		open  arv/BGcore/Simulations/Templates/template_15thFeb_dop840_poisson_SI_V7_synwtchng4mPDTrip.py
		-- set/update 
			==> sys.path.insert(0, "/home/username/Documents/arv/BGcore/")
		-- set/update 
			==> RESULTSFolder = "/home/username/Documents/arv/BGcore/Simulations/Templates/GDFS/" + PDState + str(sys.argv[2]) + "/"+ str(mv) +"/Trial" + str(numTrials)

		-- change  following in /BGcore/Simulations/BasalFiring/param_val_Transient11thNov_SI.py
			-- set p.PD_BIPHASIC = False 
			-- set p.PD_TRIPHASIC = True 

		-- Run
			>> python GenFigure5_synwtchng4mPDTrip.py OutputDirName
		OUTPUT
			-- GDFS will be saved under /BGcore/Simulations/Templates/GDFS
			-- images would be saved under /BGcore/Simulations/Templates/images

	-- Postprocessing
		MATLAB code 
		i. Input - /BGcore/Simulations/Templates/images
                    syn_range_trial_Exp.m 
                    OUTPUT- duration.txt and area.txt 
		ii. Input - duration.txt and area.txt 
		    Fig5.m
		    OUTPUT- Figure 5 
		iii.Input - duration.txt and area.txt 
                    Fig5_heatmap.m	

3. To generate Figure 6

	open  arv/BGcore/Simulations/Templates/template_15thFeb_dop840_poisson_SI_V7_restoration.py
	-- set/update 
		==> sys.path.insert(0, "/home/username/Documents/arv/BGcore/")
	-- set/update 
		==> RESULTSFolder = "/home/username/Documents/arv/BGcore/Simulations/Templates/GDFS/" + PDState +"Trial" + str(numTrials)

	-- Run
		>> python GenFigure6_restoration.py Figure6_Restoration
	-- Postprocessing   
		MATLAB code  i. Input- Directory of different restoration connection folders
                             Fig6.m
			     OUTPUT- - Feature Matrix
                             ii. Input - Feature Matrix
			     Fig6_restoration_polarplot.py 
									
	
