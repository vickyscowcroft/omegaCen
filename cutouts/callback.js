var indx = cb_obj.get('selected')['1d'].indices[0];
var data = source.get('data');
var filts = filters.get('data');
var id = data['id'][indx];
var type = data['type_vowel'][indx];
var per = data['per'][indx];
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
var band_labels = ['j','h','k','3','4'];
var band_names = ['J','H','K_s','[3.6]','[4.5]'];
var infostr = type + ', P = ' + Number(per).toFixed(3) + ' d<br>';
infostr = infostr + '(' + ra + ', ' + dec + ')';
infostr = infostr + '[Fe/H]: ' + feh + ' +/- ' + feh_err + ' dex<br>';
for (var i=0; i<=4; i++) {
	var l = band_labels[i];
	var lc_phase = lc_data[id + '_' + l + '_phase'];
	var lc_mags = lc_data[id + '_' + l + '_mags'];
	for (var j=0; j<12; j++) {
		if (typeof lc_phase !== "undefined") {
			lc_data['phase_' + l][j] = lc_phase[j];
			lc_data['mags_' + l][j] = lc_mags[j];
			lc_data['color'][j] = color;
		} else {
			lc_data['phase_' + l][j] = 'NaN';
			lc_data['mags_' + l][j] = 'NaN';
		}
	}
	lc_source.trigger('change');
	// lc_data['phase_' + l] = lc_phase;
	// lc_data['mags_' + l] = lc_mags;
	var mag = Number(data['mag_' + l][indx]).toFixed(3);
	var merr = Number(data['merr_' + l][indx]).toFixed(3);
    infostr = infostr + band_names[i] + ' mag: ' + mag + ' +/- ' + merr + '<br>';
}
document.getElementById('mags').innerHTML = infostr;

JS9.RemoveRegions({display:"fullfield"});
id1 = JS9.AddRegions('circle(' + ra + ',' + dec + ',20");', {display:"fullfield"});
// id2 = JS9.AddRegions('text(' + ra + ',' + dec + ',' + id + ');', {display:"fullfield"});

