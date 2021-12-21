# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 02:57:36 2021

@author: Sangheeta
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 00:19:16 2021

@author: Sangheeta
"""

#29.8578  26.1070 30.1692 29.0840 30.0324 28.7025


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import ast
from pylab import *

plot_index = 3;
plot_name = ['D1-SNr', 'D2-TI', 'STN-TI LOOP', 'TA-TI collaterals']
basal_FR  = [30.1692, 29.0840, 30.0324, 28.7025];

dfs_raw = pd.read_excel("restoration_feature_sentCopy.xlsx")
print(dfs_raw.head(10))
for col in dfs_raw.columns:
    print(col)
 

eeL =  '  L'+ r'$^\mathbf{EE}$'; 
eiL =  ' L'+ r'$^\mathbf{EI}$' ; 
leL =  ' L'+ r'$^\mathbf{LE}$' ;
liL =  ' L'+ r'$^\mathbf{LI}$';

eeD =  '  D'+ r'$^\mathbf{EE}$' ; 
eiD =  '  D'+ r'$^\mathbf{EI}$' ; 
leD =  '  D'+ r'$^\mathbf{LE}$' ;
liD =  ' D'+ r'$^\mathbf{LI}$'+'   ';

eeA =  'A'+ r'$^\mathbf{EE}$'+'   ' ; 
eiA =  'A'+ r'$^\mathbf{EI}$' +'  '; 
leA =  'A'+ r'$^\mathbf{LE}$'+'  ' ;
liA =  'A'+ r'$^\mathbf{LI}$'+ '  ';

#muu =  r'$\mathbf{\mu}$'    
submuu = r'$^\mathbf{EE}_\mathbf{\mu}$'
eem =  'H'+ r'$^\mathbf{EE}_\mathbf{\mu}$' +'  '; 
eim =  'H'+ r'$^\mathbf{EI}_\mathbf{\mu}$' +'  '; 
lem =  'H'+ r'$^\mathbf{LE}_\mathbf{\mu}$' +'  ';
lim =  'H'+ r'$^\mathbf{LI}_\mathbf{\mu}$' +'  ';


#sigmaa = r'$\mathbf{\sigma}$'  
sigmaa = r'$^\mathbf{EE}_\mathbf{\sigma}$'
ees =  'H'+ r'$^\mathbf{EE}_\mathbf{\sigma}$' +'  ' ; 
eis =  'H'+ r'$^\mathbf{EI}_\mathbf{\sigma}$' +'  '; 
les =  'H'+ r'$^\mathbf{LE}_\mathbf{\sigma}$' +'  ';
lis =  '  H'+ r'$^\mathbf{LI}_\mathbf{\sigma}$' + '  ';

maxzone = r'$_\mathbf{\max}$'

eemax =  '    H'+ r'$^\mathbf{EE}_\mathbf{max}$' + ' '; 
eimin =  '    H'+ r'$^\mathbf{EI}_\mathbf{min}$' +' '; 
lemax =  '    H'+ r'$^\mathbf{LE}_\mathbf{max}$'+ ' ' ;
limin =  '    H'+ r'$^\mathbf{LI}_\mathbf{min}$'+' ';


theta = np.linspace(-3.1416, 3.1416, num=24, endpoint=True)

plottitle = plot_name [plot_index];#"D1GPI"


ee_hmax =  dfs_raw.iloc [:,20] 
ei_hmax = dfs_raw.iloc [:,20] 
ei_hmin = basal_FR[plot_index] - dfs_raw.iloc [:,21] 
li_hmin = basal_FR[plot_index] - dfs_raw.iloc [:,23]

A1 =  dfs_raw.iloc [:,0:20]
#dfs = pd.concat([A1, ee_hmax], verify_integrity=True)
dfs = pd.concat([A1, ee_hmax, ei_hmin, ei_hmax, li_hmin], axis=1)


normal  = dfs.iloc[0]
Pdtriphasic  = dfs.iloc[1]
D1GPI  = dfs.iloc[2]
D2TI  = dfs.iloc[3]
STNTILOOP  = dfs.iloc[4]
TATIAll  = dfs.iloc[5]

number_of_subplots= 1
y_r = [0., 1., 2., 3., 4.]

for i,v in enumerate(range(number_of_subplots)):
    v = v+1
    ax = subplot(1, number_of_subplots, v, projection='polar')   
    if (plot_index ==0):

        ax.plot(theta, Pdtriphasic.values/normal.values, 'r', linewidth=3,label='PD'), 
        ax.plot(theta, D1GPI.values/normal.values, 'b', linewidth=3, label= plottitle),
        ax.plot(theta, normal.values/normal.values, 'g',linewidth=3, label='Normal')    
        ax.set_rmax(5)
        ax.set_rticks([0, 1, 2, 3, 4, 5])  # less radial ticks
        ax.set_rlim(0., 5, 1.)
        ax.set_rlabel_position(227)
        ax.yaxis.grid(True)
  
        #ax.set_rgrids(rtick_locs, rtick_labels, fontsize=16)
    
    if (plot_index ==1):    
        ax.plot(theta, Pdtriphasic.values/normal.values, 'r', linewidth=3, label='PD'), 
        ax.plot(theta, D2TI.values/normal.values, 'b', linewidth=3, label=plottitle),
        ax.plot(theta, normal.values/normal.values, 'g',linewidth=3, label='Normal')
        ax.set_rmax(5)
        ax.set_rticks([0, 1, 2, 3, 4, 5])  # less radial ticks
        ax.set_rlim(0., 5, 1.)
        ax.set_rlabel_position(227) 
        ax.yaxis.grid(True)     

    if (plot_index ==2):      
        ax.plot(theta, Pdtriphasic.values/normal.values, 'r',linewidth=3,  label='PD'), 
        ax.plot(theta, STNTILOOP.values/normal.values, 'b', linewidth=3, label=plottitle),
        ax.plot(theta, normal.values/normal.values, 'g',linewidth=3, label='Normal')
        ax.set_rmax(5)
        ax.set_rticks([0, 1, 2, 3, 4, 5])  # less radial ticks
        ax.set_rlim(0., 5, 1.)  
        ax.set_rlabel_position(227) 
        ax.yaxis.grid(True)         
  
    if (plot_index ==3):     
        ax.plot(theta, Pdtriphasic.values/normal.values, 'r',linewidth=3, label='PD'), 
        ax.plot(theta, TATIAll.values/normal.values, 'b', linewidth=3, label=plottitle),
        ax.plot(theta, normal.values/normal.values, 'g',linewidth=3, label='Normal')
        ax.set_rmax(5)
        ax.set_rticks([0, 1, 2, 3, 4, 5])  # less radial ticks
        ax.set_rlim(0., 5, 1.)    
        ax.set_rlabel_position(227)    
        ax.yaxis.grid(True)      
  


    
    thetatick_locs = np.linspace(0.,360.,num=24, endpoint=False)
    #thetatick_locs_label = ["EE-L", "EI-L","LE-L","LI-L","EE-D","EI-D", "LE-D","LI-D","EE-A","EI-A","LE-A","LI-A"," EE-H_µ    "," EI-H_µ    ","LE-H_µ","LI-H_µ","EE-H_σ  ","EI-H_σ  ","LE-H_σ  ","   LI-H_σ   ","         EE-H_max  ","        EI-H_min  ", "          LE-H_max  ","          LI-H_min    "]
    thetatick_locs_label = [eeL, eiL, leL, liL, eeD, eiD, leD, liD, eeA, eiA, leA, liA, eem, eim, lem, lim, ees, eis,les,lis, eemax, eimin, lemax, limin]
 
    x_label = list(thetatick_locs_label)
    
    #thetatick_labels = [u'%i\u00b0'%np.round(x) for x in thetatick_locs]
    #ax.set_thetagrids(thetatick_locs, thetatick_labels, fontsize=16)
    
    thetatick_labels = [u'%i\u00b0'%np.round(x) for x in thetatick_locs]
    ax.set_thetagrids(thetatick_locs, x_label, fontsize=10)
    
    #plt.show()
    
    plt.gcf().canvas.draw()
    angles = np.linspace(0,2*np.pi,len(ax.get_xticklabels())+1)
    angles[np.cos(angles) < 0] = angles[np.cos(angles) < 0] + np.pi
    angles = np.rad2deg(angles)
    labels = []
    for label, angle in zip(ax.get_xticklabels(), angles):
        x,y = label.get_position()
        lab = ax.text(x,y, label.get_text(), transform=label.get_transform(),
                      ha=label.get_ha(), va=label.get_va(), fontsize=20, fontweight='bold')
        lab.set_rotation(angle)
        labels.append(lab)
    ax.set_xticklabels([])
    

    ax.set_title(plottitle, va='bottom', pad=45, fontsize=24, fontweight='bold')
    #ax.set_title("D2TI", va='bottom', pad=20)
    #ax.set_title("STNTI", va='bottom', pad=20)    
    #ax.set_title("TATIAll", va='bottom', pad=20)    

    #plt.show()
    #ax.figure.savefig('file.png')
    
#f.tight_layout()
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
#          fancybox=True, shadow=True, ncol=3)

#plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
#                mode="expand", borderaxespad=0, ncol=3, labelspacing = 15)

#plt.legend(bbox_to_anchor=(0,1.3,1,0.2), loc="lower left",
#                mode="expand", borderaxespad=0, ncol=3, fontsize = 20, labelspacing=8.5)
#legend.get_frame().set_facecolor('C0')

#plt.savefig(plottitle +'.png')
plt.show()
#f.savefig('my_figure.png')
#f.savefig('D2TI.pdf')
#f.savefig('STNTI.pdf')
#f.savefig('TATIAll.pdf')







"""
for i  in range(3):

    plt.figure()

    ax = plt.subplot(121, projection='polar')
    ax.plot(theta, Pdtriphasic.values/normal.values, 'r'), 
    ax.plot(theta, D1GPI.values/normal.values, 'b', linewidth=3),
    ax.plot(theta, normal.values/normal.values, 'g',linewidth=3)
    ax.set_rmax(4)
    ax.set_rlim(0., 5., 1.)
    
    
    #ax.set_rticks([]) 
    # set the size of theta ticklabels (works)
    
    thetatick_locs = np.linspace(0.,360.,num=24, endpoint=False)
    thetatick_locs_label = ["EE-L", "EI-L","LE-L","LI-L","EE-D","EI-D", "LE-D","LI-D","EE-A","EI-A","LE-A","LI-A"," EE-H_mu    "," EI-H_mu    ","LE-H_mu","LI-H_mu","EE-H_std  ","EI-H_std  ","LE-H_std  ","   LI-H_std   ","     EE-H_max  ","    EI-H_min  ", "      LE-H_max  ","      LI-H_min    "]
    x_label = list(thetatick_locs_label)
    
    #thetatick_labels = [u'%i\u00b0'%np.round(x) for x in thetatick_locs]
    #ax.set_thetagrids(thetatick_locs, thetatick_labels, fontsize=16)
    
    thetatick_labels = [u'%i\u00b0'%np.round(x) for x in thetatick_locs]
    ax.set_thetagrids(thetatick_locs, x_label, fontsize=8)
    
    #plt.show()
    
    plt.gcf().canvas.draw()
    angles = np.linspace(0,2*np.pi,len(ax.get_xticklabels())+1)
    angles[np.cos(angles) < 0] = angles[np.cos(angles) < 0] + np.pi
    angles = np.rad2deg(angles)
    labels = []
    for label, angle in zip(ax.get_xticklabels(), angles):
        x,y = label.get_position()
        lab = ax.text(x,y, label.get_text(), transform=label.get_transform(),
                      ha=label.get_ha(), va=label.get_va(), fontsize=8)
        lab.set_rotation(angle)
        labels.append(lab)
    ax.set_xticklabels([])
    
    
    ax.set_title("Example", va='bottom')
    plt.show()
"""