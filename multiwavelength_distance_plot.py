
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format='retina'")
import numpy as np
import prettyplotlib as ppl
from scipy.optimize import leastsq
from matplotlib import pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman'], 'size':14})
rc('text', usetex=True)


# In[2]:

f1 = open('line_parameters')
pl_param = np.loadtxt(f1)
f1.close()

# parameters format: zeropoint, slope, metallicity, mode (0 = ab, 1 = c), bandpass number
# bandpass numbers: -1 = H, -2 = K, -3 = 3.6, -4 = 4.5, -5 = J

f2 = open('all_data')
full_data = np.loadtxt(f2)
f2.close()

# full data format:
# id, mag, mag err, bandpass number, metallicity, metallicity error, mode, period


# In[3]:

def pl_fit(params, per, feh): # coefficients, periods, metallicities
    fit = params[1]*per + params[0] + params[2]*(feh)
    return np.array(fit)

def fitfunc(dmod, params, per, feh, mag): # distance modulus as only free parameter
    fit = pl_fit(params, per, feh)
    return np.array(fit + dmod - mag)


# In[4]:

bands = ['J', 'H', 'K', '[3.6]', '[4.5]']
band_numbers = [-5, -1, -2, -3, -4]
plot_colors = [(0.718, 0, 0.718), (0.316, 0.316, 0.991),
               (0, 0.592, 0), (0.527, 0.527, 0), 
               (0.847, 0.057, 0.057)]
mag_offset = [9, 6.5, 4, 2, 0]
mode = [0,1,0,1,0,1,0,1,0,1]

fig = plt.figure(figsize=(7,8))
ax = fig.add_subplot(1,1,1)
for i in range(10):
    j = int(i/2)
    dat = full_data[(full_data[:,3] == band_numbers[int(i/2)]) & (full_data[:,6] == mode[i])]
    data = dat.T
    per = np.log10(data[7])
    mag = data[1]
    merr = data[2]
    feh = data[4]
    dmod_prior = 13
    dmod_out = leastsq(fitfunc, dmod_prior, args=(pl_param[i], per, feh, mag), full_output=True)
    dmod_new = dmod_out[0][0]
    dmod_err = dmod_out[1][0][0]
    print 'Band:', bands[j].ljust(5), '  Distance:', np.round(dmod_new, decimals=2), '+/-', \
    np.round(dmod_err, decimals=2), '  Mode:', pl_param[i,3], '  Number of RR Lyrae:', len(per)
    xspace = np.linspace(np.min(per) - 0.03, np.max(per) + 0.03, 100)
    fehspace = np.linspace(np.min(feh), np.max(feh), 100)
    linfit = pl_param[i,1]*xspace + pl_param[i,0] + pl_param[i,2]*fehspace + dmod_new
    ppl.errorbar(np.log10(data[7]), data[1] - mag_offset[j], \
    yerr=data[2], color=plot_colors[j], fmt='o', alpha=0.7)
    ppl.plot(xspace, linfit - mag_offset[j], 'k--')
    if i % 2 == 0:
        ppl.errorbar([],[],yerr=[],color=plot_colors[j],fmt='o',
                     label='${} - {}$'.format(bands[j], mag_offset[j]))
ax.set_ylim(15.9, 2.4)
ppl.legend(loc=4, prop={'size':14}, handlelength=1, numpoints=1, ncol=2)
ax.set_ylabel('Magnitude')
ax.set_xlabel('log P')
ax.set_title(r'Multiwavelength $\omega$ Cen PL relations', fontsize=15)
fig.tight_layout()
fig.savefig('multiwavelength_PL.pdf')


# In[ ]:



