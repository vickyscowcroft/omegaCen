
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format='retina'")
import numpy as np
import prettyplotlib as ppl
from astropy.stats import sigma_clip
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

f2 = open('all_data_samestars')
stars = np.loadtxt(f2)
f2.close()

stars[:,4] = np.zeros(len(stars)) + -1.58404580153 # photometric metallicity

# full data format:
# id, mag, mag err, bandpass number, metallicity, metallicity error, mode, period


# In[3]:

def pl_fit(params, per, feh): # coefficients, periods, metallicities
    fit = params[1]*per + params[0] + params[2]*(feh)
    return np.array(fit)

def fitfunc(dmod, params, per, feh, mag): # distance modulus as only free parameter
    fit = pl_fit(params, per, feh)
    return np.array(fit + dmod - mag)


# In[16]:

bands = ['J', 'H', 'K', '[3.6]', '[4.5]']
band_numbers = [-5, -1, -2, -3, -4]
plot_colors = [(0.718, 0, 0.718), (0.316, 0.316, 0.991),
               (0, 0.592, 0), (0.527, 0.527, 0), 
               (0.847, 0.057, 0.057)]
mag_offset = [8, 6, 4, 2, 0]
mode = [0,1,0,1,0,1,0,1,0,1]
wav = [1.220, 1.630, 2.190, 3.550, 4.493]

dist = []
fig = plt.figure(figsize=(7,8))
ax = fig.add_subplot(1,1,1)
residuals = []
ppl.errorbar([],[],yerr=[],fmt='o',color='k',label='FU')
ppl.errorbar([],[],yerr=[],fmt='^',color='k',label='FO')

for i in range(10):
    j = int(i/2)
    dat = stars[(stars[:,3] == band_numbers[j]) & (stars[:,6] == mode[i])]
    data = dat.T
    per = np.log10(data[7])
    mag = data[1]
    merr = data[2]
    feh = data[4]
    dmod_prior = 13
    dmod_out = leastsq(fitfunc, dmod_prior, args=(pl_param[i], per, feh, mag), full_output=True)
    dmod_new = dmod_out[0][0]
    dmod_err = dmod_out[1][0][0]
    
    xspace = np.linspace(np.min(per) - 0.03, np.max(per) + 0.03, 100)
    fehspace = np.linspace(np.min(feh), np.max(feh), 100)
    linfit = pl_param[i,1]*xspace + pl_param[i,0] + pl_param[i,2]*fehspace + dmod_new
    resid = (pl_param[i,1]*per + pl_param[i,0] + pl_param[i,2]*feh + dmod_new) - mag
    residuals.append([pl_param[i,4], pl_param[i,3], data[0], resid, merr])
    sig_resid = np.std(resid)
    
    print 'Band:', bands[j].ljust(5), '  Distance:', np.round(dmod_new, decimals=2), '+/-',
    np.round(dmod_err, decimals=2), '  Mode:', pl_param[i,3], '  # of RR Lyrae:', len(per),
    'Sigma of resid:', np.round(sig_resid, decimals=3)

    dist.append([wav[j], dmod_new, dmod_err, mode[i], sig_resid])

    ppl.plot(xspace, linfit - mag_offset[j], 'k--')
    
    if i % 2 == 0:
        ppl.errorbar(np.log10(data[7]), data[1] - mag_offset[j],
            yerr=data[2], color=plot_colors[j], fmt='o')
        ppl.errorbar([],[],yerr=[],color=plot_colors[j],fmt='o',
                     label='${} - {}$'.format(bands[j], mag_offset[j]))
    else:
        ppl.errorbar(np.log10(data[7]), data[1] - mag_offset[j], 
            yerr=data[2], color=plot_colors[j], fmt='^')

ax.set_ylim(15.9, 4.1)
ppl.legend(loc=4, prop={'size':14}, handlelength=1, numpoints=1, ncol=2)
ax.set_ylabel('Magnitude')
ax.set_xlabel(r'$\log P$')
ax.set_title(r'Multiwavelength $\omega$ Cen PL relations', fontsize=15)
fig.tight_layout()
fig.savefig('multiwavelength_PL_samestars_phot.pdf')
np.savetxt('distances_samestars_phot', dist, fmt='%s', delimiter=' ')



