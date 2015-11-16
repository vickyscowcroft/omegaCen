
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')
#get_ipython().magic(u"config InlineBackend.figure_format='retina'")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import glob
#import brewer2mpl
#set2 = brewer2mpl.get_map('Dark2', 'qualitative', 8).mpl_colors
from reddening_laws import *
import prettyplotlib as ppl
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman'], 'size':14})
rc('text', usetex=True)
#mycolors = ['red', 'gold', 'green', 'blue', 'purple']
#rc('axes', color_cycle=mycolors)
#from scipy.optimize import leastsq


# In[2]:

f = open('final_data_files/distances_allstars_phot')
distances = np.loadtxt(f)
f.close()

dist_ab = distances[distances[:,3] == 0.]
dist_c = distances[distances[:,3] == 1.]
len_all = float(len(distances))


# In[3]:

dist_mean = (dist_ab[:,1] * len(dist_ab)/len_all) + (dist_c[:,1] * len(dist_c)/len_all)
err_mean = np.sqrt((dist_ab[:,2] * len(dist_ab)/len_all)**2 +
                   (dist_c[:,2] * len(dist_c)/len_all)**2) #/ np.sqrt(len_all)


# In[4]:

dist_mean_all = np.concatenate(([0,0,0,0], dist_mean))
err_mean_all = np.concatenate(([0,0,0,0], err_mean))

fit_reddening_args = np.asarray(list(dist_mean_all) + list(err_mean_all))


# In[5]:

reddening_stuff = fit_reddening(*fit_reddening_args)
#print reddening_stuff
tru_dist = reddening_stuff[0]
tru_dist_stdev = reddening_stuff[2]
Av = reddening_stuff[1]
Av_err = reddening_stuff[3]

print 'Distance: {} +/- {}'.format(tru_dist, tru_dist_stdev)
print 'Av: {} +/- {}'.format(Av, Av_err)
print 'E(B-V): {} +/- {}'.format(Av/3.1, Av_err/3.1)



# In[6]:

nearir_x = np.linspace(1/0.875,1.5,50)
midir_x = np.linspace(1.5,8.,100)

Rv = 3.1
Ak = ccm_nearir(2.164,Rv)

nearir_y = ccm_nearir(nearir_x,Rv)
midir_y = indebetouw_ir(midir_x) * Ak


# In[7]:
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1)
ax2 = ax.twiny()
x = np.linspace(0.,1,20)
y = x * 0 + tru_dist
ppl.errorbar(ax, 1/dist_ab[:,0], dist_mean, yerr=err_mean,
             color='k', mfc='k', fmt='o', label=r'$\mu$ (uncorrected)', zorder=10)
ppl.plot(ax, x, y, 'k-', lw=2, label=r'$\mu_0 = {:.3f}\pm {:.3f}$'.format(tru_dist,tru_dist_stdev))
ppl.plot(ax, x, y + tru_dist_stdev, 'k--')#, label=r'$\pm 1\sigma,\ \sigma = {:.3f}$'.format(tru_dist_stdev))
ppl.plot(ax, x, y - tru_dist_stdev, 'k--')
#ppl.plot(ax, 1/opt_x, opt_y*Av + tru_dist, 'k-')
ppl.plot(ax, 1/nearir_x, nearir_y*Av + tru_dist, 'k-', label='Reddening curve')
ppl.plot(ax, 1/midir_x, midir_y*Av + tru_dist, 'k-')
#ppl.plot(ax, [], [], alpha=0, label='$A_V = {:.3f}$'.format(Av))
ppl.legend(ax, loc=4, prop={'size':14}, numpoints=1, handlelength=1.5)
ax.set_xlim(1/8.,0.875)
ax2.set_xlim(ax.get_xlim()[0], ax.get_xlim()[1])
ax2.xaxis.set_ticks_position('none')
ax2.set_xticks(1/dist_ab[:,0])
ax2.set_xticklabels(['$J$', '$H$',  '$K$', '[3.6]', '[4.5]'])
ax.set_ylim(13.48,14.02)
ax.text(ax.get_xlim()[1]-0.025,ax.get_ylim()[1]-0.03,
        '$E(B-V) = {:.3f}\pm{:.3f}$'.format(Av/3.1,Av_err/3.1), ha='right',va='top')
ax.set_xlabel(r'$1/\lambda\ (\mu\mathrm{m}^{-1})$')
ax.set_ylabel(r'$\mu$')
fig.tight_layout()
fig.savefig('final_plots/multiwavelength_distance_allstars_phot.pdf', dpi=300)


# In[ ]:




# In[ ]:



