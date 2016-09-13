'''
Makes static Bokeh plots with JS9.
'''

#!/usr/bin/env python

from astropy.io import fits

from collections import OrderedDict
import numpy as np
import pandas as pd
import os

from bokeh.models import HoverTool, TapTool
from bokeh.models import Circle, Range1d, ColumnDataSource, Span, CustomJS
from bokeh.models.glyphs import Image, ImageURL
# from bokeh.models.mappers import LinearColorMapper
from bokeh.embed import components, file_html
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
mag_offset = [8, 6, 4, 2, 0]
#wavelength = [1.220, 1.630, 2.190, 3.550, 4.493]

df = pd.read_csv('../reworked_fitting_code/final_data_files/all_possible_photometry.csv')
df['logP'] = np.log10(df.per)
df['type_vowel'] = df.type.astype(str).str.replace('0','RRab').replace('1','RRc')
color = colormap(df.photfeh,RdYlBu11)
df['color'] = color

# reads in javascript callback
with open('callback.js') as callback_file:
    callback_js = callback_file.read()

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

# Assigns color to point based on redshift
logP = np.log10(df.per)
source = ColumnDataSource(data=df.astype(str).to_dict(orient='list'))
figure_dict = OrderedDict()
for i in range(5):
    p = figure(y_range=(14.6, 11.9), x_range=(-0.64, 0.06), plot_width=550)
    l = band_labels[i]
    source.add(list(df['mag_{}'.format(l)]-mag_offset[i]), name='mag__{}'.format(l))
    p.circle('logP', 'mag_{}'.format(l),color='color',
        source=source, size=7, line_color='black', name='pl',
        line_width=0.7, fill_alpha=0.7, line_alpha=0.7)
    hover = HoverTool(tooltips=OrderedDict([('ID','@id'),('Type','@type_vowel'),('Per','@per'),
                                            ('[Fe/H]','@photfeh')])) #,('RA','@ra'),('Dec','@dec')
    p.add_tools(hover)
    p.yaxis.axis_label = '{} mag'.format(band_names[i])
    if i == 0:
        p.xaxis.major_label_text_font_size = '0pt'
        p.plot_height = 180
    elif i == 4:
        p.plot_height = 190
    else:
        p.xaxis.major_label_text_font_size = '0pt'
        p.plot_height = 150
    figure_dict['p{}'.format(i)] = p
    if i > 0:
        figure_dict['p{}'.format(i)].x_range = figure_dict['p0'].x_range
        figure_dict['p{}'.format(i)].y_range = figure_dict['p0'].y_range
    renderer = p.select('pl')
    renderer.selection_glyph = selected
    renderer.nonselection_glyph = unselected
    callback = CustomJS(args=dict(source=renderer[0].data_source, filters = filters),
        code=callback_js)
    p.add_tools(TapTool(callback=callback))

figure_dict['p0'].title.text = 'Omega Cen RRL PL Relations'
figure_dict['p4'].xaxis.axis_label = 'log P (days)'
grid = gridplot(figure_dict.values(),ncols=1)


# renderers = [figure_dict['p{}'.format(i)].select(name="pl") for i in range(5)]
# for r in renderers:
#     r.selection_glyph = selected
#     r.nonselection_glyph = unselected

# for i in range(5):
#     plot = figure_dict['p{}'.format(i)]
#     renderer = plot.select('pl')
#     renderer.selection_glyph = selected
#     renderer.nonselection_glyph = unselected
#     callback = CustomJS(args=dict(source=renderer[0].data_source, filters = filters),
#         code=callback_js)
#     plot.add_tools(TapTool(callback=callback))

bokeh_script, bokeh_div = components(grid, CDN)


# # The main event
# def plot(df, palette=RdYlBu11):
#     logP = np.log10(df['per'])
#     # add color to thing
#     color = colormap(df['photfeh'],palette)
#     # make ColumnDataSource
#     source = ColumnDataSource(data=df.to_dict())
#     source.add(logP, name='logP')
#     source.add(color, name='color')
#     # set yrange values
    
#     p = figure(y_range=(ymax, ymin), plot_width=600, plot_height=750)
#     hover = HoverTool(tooltips=OrderedDict([('ID','@id'),('Type','@type'),('Per','@per'),
#                                             ('[Fe/H]','@photfeh'),('Zphot','@zphot')
#                                             ('RA','@RAdeg{1.11111}'),('Dec','@DECdeg{1.11111}')]))
#     p.add_tools(hover)
    
#     p.circle('logP', 'mag_j', source=source, size=7, fill_color='color',
#              line_color='black', line_width=0.4, fill_alpha=0.7, line_alpha=0.7, name='pls')
    
#     #custom glyphs for selected + unselected points
#     selected = Circle(size=7, fill_color='color', line_color='black',
#                       line_width=0.4, fill_alpha=1.0, line_alpha=1.0)
#     unselected = Circle(size=7, fill_color='color', line_color='black',
#                          line_width=0.4, fill_alpha=0.1, line_alpha=0.5)
#     renderer = p.select(name="pls")
#     renderer.selection_glyph = selected
#     renderer.nonselection_glyph = unselected

#     # other plot junk
#     p.title = 'Omega Cen PL Relations'
#     p.xaxis.axis_label = 'log P (days)'
#     p.yaxis.axis_label = 'Apparent Magnitude'
#     p.title_text_font_size='14pt'
#     p.xaxis.axis_label_text_font_size = '12pt'
#     p.yaxis.axis_label_text_font_size = '12pt'
#     # return plot object
#     return p

# catalog_path = "../merged_catalogs/"
# filter_list = ['F435W', 'F606W', 'F775W', 'F850LP', 'F105W', 'F125W', 'F160W']

# # reads in javascript callback
# with open('callback.js') as callback_file:
#     callback_js = callback_file.read()

# # reads in HTML that goes before plot
# with open('before.html') as before_file:
#     before_html = before_file.read()

# # reads in HTML that goes after plot
# with open('after.html') as after_file:
#     after_html = after_file.read()

# # makes the file
# def make_file(emission_line, field, target_filter, z):
#     filter_num = filter_list.index(target_filter)
#     left_filter = filter_list[filter_num - 1]
#     right_filter = filter_list[filter_num + 1]

#     used_filters = [left_filter, target_filter, right_filter]

#     column_list = [get_fluxcol(filt) for filt in used_filters]
#     column_list += [get_fluxcol(filt) + 'ERR' for filt in used_filters]
#     column_list += ['zphot', 'ID', 'RAdeg', 'DECdeg', 'PhotFlag']

#     tab = Table.read(os.path.join(catalog_path,'{}.hdf5'.format(field)),path=field)
#     if field == 'gdn':
#         tab.rename_column('Photo_z_median_best','zphot')
#     tab.keep_columns(column_list)
#     selection = (tab['PhotFlag'] == 0)
#     tab_cut = tab[selection]

#     filt1, filt2, filt3, filt4 = choose_fourth_filter(filter_num, filter_list)
#     filters = ColumnDataSource({'image1':filt1,'image2':filt2,'image3':filt3,'image4':filt4})

#     p0 = make_cmd(tab_cut, z, left_filter, target_filter, right_filter, emission_line, field)

#     callback = CustomJS(args=dict(source=p0.select(dict(name="pls"))[0].data_source, filters = filters),
#         code=callback_js % (field))

#     p0.add_tools(TapTool(callback=callback))

#     bokeh_script, bokeh_div = components(p0)
#     output_dir = 'html_plots'
#     output_file = '{}_z{}_{}.html'.format(emission_line, z, field)
#     print 'Writing to file: {}'.format(output_file)


#output_dir = 'cutouts'
output_file = 'test.html'

with open(output_file, 'w') as f:
    f.write(before_html) #% (emission_line, z, field[-1].upper()))
    f.write(bokeh_div)
    f.write(bokeh_script)
    f.write(after_html)#% (filt1, filt2, filt3, filt4))

# emission_line = 'OIII'
# fields = ['gds', 'gdn']

# z_filt = [(0.4, 'F606W'), (1.1, 'F105W'), (1.7, 'F125W')]

# actually do the thing
# for field in fields:
#     for z, filt in z_filt:
#         make_file(emission_line, field, filt, z)

