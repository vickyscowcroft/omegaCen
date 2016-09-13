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
for (var i=3; i <= 5; i++) {
    var fitsfile = 'cutouts/' + id.toString() + '_' + filts['image'+i.toString()] + '.fits';
    JS9.Load(fitsfile, {zoom:'toFit', scale:'log', scaleclipping:'dataminmax'}, {display:'image'+i.toString()});
}
var idstr = 'RRL ID ' + id;
// <span style="font-size:10pt">' + type + ', P = ' + Number(per).toFixed(3) + ' d';
// infostr = infostr + ', [Fe/H] = ' + feh + ' +/- ' + feh_err + ' dex</span>';
document.getElementById('starinfo').innerHTML = idstr;

var band_labels = ['j','h','k','3','4'];
var band_names = ['J','H','K_s','[3.6]','[4.5]'];
var infostr = type + ', P = ' + Number(per).toFixed(3) + ' d<br>';
// infostr = infostr + '(' + ra + ', ' + dec + ')';
infostr = infostr + '[Fe/H]: ' + feh + ' +/- ' + feh_err + ' dex<br>';
for (var i=0; i <= 4; i++) {
	var mag = Number(data['mag_' + band_labels[i]][indx]).toFixed(3);
	var merr = Number(data['merr_' + band_labels[i]][indx]).toFixed(3);
    infostr = infostr + band_names[i] + ' mag: ' + mag + ' +/- ' + merr + '<br>';
}
document.getElementById('mags').innerHTML = infostr;

