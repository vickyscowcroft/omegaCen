'''
Makes static Bokeh plots with JS9.
'''

#!/usr/bin/env python

from collections import OrderedDict
import numpy as np
import pandas as pd

from bokeh.models import HoverTool, TapTool, Slider
from bokeh.models import Circle, ColumnDataSource, CustomJS
from bokeh.embed import components
from bokeh.palettes import RdYlBu11
from bokeh.plotting import gridplot, figure
from bokeh.resources import CDN

def colormap(col, palette):
    n,bins = np.histogram(col[np.isfinite(col)],bins=len(palette) - 1)
    color = col.copy().astype(str)
    binsize = bins[1] - bins[0]
    for num, val in enumerate(bins):
        cond = (col > val - binsize) & (col <= val)
        color[cond] = palette[num]
    color[color=='nan'] = '#cccccc'
    return color

band_labels = ['j', 'h', 'k', '3', '4']
band_names = ['J', 'H', 'Ks', '3p6', '4p5']
band_names2 = ['J', 'H', 'Ks', '[3.6]', '[4.5]']
mag_offset = [8, 6, 4, 2, 0]
#wavelength = [1.220, 1.630, 2.190, 3.550, 4.493]

df = pd.read_csv('../reworked_fitting_code/final_data_files/all_possible_photometry.csv')
df['logP'] = np.log10(df.per)
df['new_per'] = df.per
df['type_vowel'] = df.type.astype(str).str.replace('0','RRab').replace('1','RRc')
color = colormap(df.photfeh,RdYlBu11)
df['color'] = color
lc_df = pd.read_csv('../reworked_fitting_code/final_data_files/lightcurves.csv')

# reads in javascript callbacks
with open('callback.js') as callback_file:
    callback_js = callback_file.read()
with open('slider_callback.js') as slider_file:
    slider_js = slider_file.read()

# reads in HTML that goes before plot
with open('before.html') as before_file:
    before_html = before_file.read()

# reads in HTML that goes after plot
with open('after.html') as after_file:
    after_html = after_file.read()

selected = Circle(size=7, fill_color='color', line_color='black',
                  line_width=0.7, fill_alpha=1.0, line_alpha=1.0)
unselected = Circle(size=7, fill_color='color', line_color='black',
                     line_width=0.7, fill_alpha=0.1, line_alpha=0.5)

filters = ColumnDataSource({'image{}'.format(i+1):[band_names[i]] for i in range(5)})

source = ColumnDataSource(data=df.astype(str).to_dict(orient='list'))
lc_source = ColumnDataSource(data=lc_df.astype(str).to_dict(orient='list'))
lc_source.add([],name='color')
lc_source.add([],name='per')
lc_source.add([],name='id')
figure_dict = OrderedDict()

slider_callback = CustomJS(args=dict(source=source, lc_source=lc_source),
        code=slider_js)

slider = Slider(start=-0.5, end=0.5, value=0, step=0.01, title="Adjust period (days)", callback=slider_callback,
    callback_policy='throttle', callback_throttle=100., width=500)

for i in range(5):
    p = figure(y_range=(14.6, 11.9), x_range=(-0.64, 0.06), plot_width=540)
    l = band_labels[i]
    lc_source.add([],name='phase_{}_1'.format(l))
    lc_source.add([],name='phase_{}_2'.format(l))
    lc_source.add([],name='phase_{}_3'.format(l))
    lc_source.add([],name='mags_{}'.format(l))
    p.circle('logP', 'mag_{}'.format(l),color='color', name='pl',
        source=source, size=7, line_color='black',
        line_width=0.7, fill_alpha=0.7, line_alpha=0.7)
    hover = HoverTool(tooltips=OrderedDict([('ID','@id'),('Type','@type_vowel'),('Per','@per'),
                                            ('[Fe/H]','@photfeh')])) # ('RA','@ra'),('Dec','@dec')
    p.add_tools(hover)
    p.yaxis.axis_label = '{} mag'.format(band_names2[i])
    
    p1 = figure(x_range=(-0.1,3.1), plot_width=240)
    p1.yaxis.visible = False
    
    p1.circle('phase_{}_1'.format(l),'mags_{}'.format(l),source=lc_source,
        color='color', size=7, line_color='black',
        line_width=0.7)
    p1.circle('phase_{}_2'.format(l),'mags_{}'.format(l),source=lc_source,
        color='color', size=7, line_color='black',
        line_width=0.7)
    p1.circle('phase_{}_3'.format(l),'mags_{}'.format(l),source=lc_source,
        color='color', size=7, line_color='black',
        line_width=0.7)

    if i == 0:
        p.xaxis.major_label_text_font_size = '0pt'
        p1.xaxis.major_label_text_font_size = '0pt'
        p.plot_height = 180
        p1.plot_height = 180
    elif i == 4:
        p.plot_height = 190
        p1.plot_height = 190
    else:
        p.xaxis.major_label_text_font_size = '0pt'
        p1.xaxis.major_label_text_font_size = '0pt'
        p.plot_height = 150
        p1.plot_height = 150
    figure_dict['p{}'.format(i)] = p
    figure_dict['p{}'.format(i+5)] = p1
    if i > 0:
        figure_dict['p{}'.format(i)].x_range = figure_dict['p0'].x_range
        figure_dict['p{}'.format(i)].y_range = figure_dict['p0'].y_range
        figure_dict['p{}'.format(i+5)].x_range = figure_dict['p5'].x_range
    figure_dict['p{}'.format(i+5)].y_range = figure_dict['p0'].y_range

    renderer = p.select('pl')
    renderer.selection_glyph = selected
    renderer.nonselection_glyph = unselected
    callback = CustomJS(args=dict(filters = filters, lc_source=lc_source, slider=slider),
        code=callback_js)
    p.add_tools(TapTool(callback=callback))


figure_dict['p0'].title.text = 'Omega Cen RRL PL Relations'
figure_dict['p5'].title.text = 'Selected RRL light curve'
figure_dict['p4'].xaxis.axis_label = 'log P (days)'
figure_dict['p9'].xaxis.axis_label = 'Phase'
grid = gridplot(figure_dict.values() + [slider],ncols=2)

bokeh_script, bokeh_div = components(grid, CDN)

#output_dir = 'cutouts'
output_file = 'index.html'

with open(output_file, 'w') as f:
    f.write(before_html)
    f.write(bokeh_div)
    f.write(bokeh_script)
    f.write(after_html)

