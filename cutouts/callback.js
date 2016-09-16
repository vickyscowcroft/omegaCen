var indx = cb_obj.get('selected')['1d'].indices[0];
var data = cb_obj.get('data');
var filts = filters.get('data');
var id = data['id'][indx];
var type = data['type_vowel'][indx];
var per = Number(data['per'][indx]);
var new_per = Number(data['new_per'][indx]);
var ra = data['ra'][indx];
var dec = data['dec'][indx];
var feh = data['photfeh'][indx];
var feh_err = data['photfeh_err'][indx];
var color = data['color'][indx];
for (var i=3; i <= 5; i++) {
    var fitsfile = 'cutouts/' + id.toString() + '_' + filts['image'+i.toString()] + '.fits';
    JS9.Load(fitsfile, {zoom:'toFit', scale:'asinh', scaleclipping:'dataminmax'}, {display:'image'+i.toString()});
}
var idstr = 'RRL ID ' + id;
document.getElementById('starinfo').innerHTML = idstr;

var lc_data = lc_source.get('data');
lc_data['per'] = per;
lc_data['id'] = Number(id);
var band_labels = ['j','h','k','3','4'];
var band_names = ['J','H','K_s','[3.6]','[4.5]'];
var infostr = type + ', P = ' + per.toFixed(3) + ' d<br>';
infostr = infostr + '(' + ra + ', ' + dec + ')';
infostr = infostr + '[Fe/H]: ' + feh + ' +/- ' + feh_err + ' dex<br>';
for (var i=0; i<=4; i++) {
	var l = band_labels[i];
	var lc_phase = lc_data[id + '_' + l + '_phase'];
	var lc_mags = lc_data[id + '_' + l + '_mags'];
	for (var j=0; j<12; j++) {
		if (typeof lc_phase !== "undefined") {
			lc_data['phase_' + l + '_1'][j] = Number(lc_phase[j]);
			lc_data['phase_' + l + '_2'][j] = Number(lc_phase[j])+1;
			lc_data['phase_' + l + '_3'][j] = Number(lc_phase[j])+2;
			lc_data['mags_' + l][j] = lc_mags[j];
			lc_data['color'][j] = color;
		} else {
			lc_data['phase_' + l + '_1'][j] = 'NaN';
			lc_data['phase_' + l + '_2'][j] = 'NaN';
			lc_data['phase_' + l + '_3'][j] = 'NaN';
			lc_data['mags_' + l][j] = 'NaN';
		}
	}
	var mag = Number(data['mag_' + l][indx]).toFixed(3);
	var merr = Number(data['merr_' + l][indx]).toFixed(3);
    infostr = infostr + band_names[i] + ' mag: ' + mag + ' +/- ' + merr + '<br>';
}
lc_source.trigger('change');
document.getElementById('mags').innerHTML = infostr;

JS9.RemoveRegions('star', {display:"fullfield"});
JS9.AddRegions('circle(' + ra + ',' + dec + ',20")', {tags: 'star', color: 'magenta', width: '2'}, {display:"fullfield"});
JS9.AddRegions('text(' + ra + ',' + dec + ',"' + id + '")', {tags: 'star', dy: '10', color: 'magenta', width: '2'}, {display:"fullfield"});

function reset_phasing(cb_obj) {
	var indx = cb_obj.get('selected')['1d'].indices[0];
	var data = cb_obj.get('data');
	var per = Number(data['per'][indx]);
	var new_per = Number(data['new_per'][indx]);
	var per_diff = new_per - per;
	if (per != new_per) {
		document.getElementById('rephased').innerHTML = 'Rephased period = ' + new_per.toFixed(3) + ' d';
	} else {
		document.getElementById('rephased').innerHTML = '&nbsp;';
	}
	slider.set('value', per_diff);
	var left = 50 + per_diff * 100;
	var handle = document.getElementsByClassName("bk-ui-slider-handle")[0];
	handle.style.left = left.toFixed(0) + '%';
}

cb_obj.on('change', reset_phasing(cb_obj));

