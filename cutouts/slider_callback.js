var indx = source.get('selected')['1d'].indices[0];
if (typeof indx !== "undefined") {
	var data = source.get('data');
	var lc_data = lc_source.get('data');
	var scale_factor = cb_obj.get('value');
	var per = data['per'][indx];
	var id = data['id'][indx];
	var new_per = Number(per) + Number(scale_factor);
	var band_labels = ['j','h','k','3','4'];
	var min_mjd = 56422.0;
	data['new_per'][indx] = new_per;
	data['logP'][indx] = Math.log10(new_per);
	for (var i=0; i<=4; i++) {
		var l = band_labels[i];
		var lc_mjd = lc_data[id + '_' + l + '_mjds'];
		for (var j=0; j<12; j++) {
			if (typeof lc_mjd !== "undefined") {
				var phased = (Number(lc_mjd[j]) - min_mjd) / new_per;
				phased = phased - Math.floor(phased);
				lc_data['phase_' + l + '_1'][j] = phased;
				lc_data['phase_' + l + '_2'][j] = phased+1;
				lc_data['phase_' + l + '_3'][j] = phased+2;
			} else {
				lc_data['phase_' + l + '_1'][j] = 'NaN';
				lc_data['phase_' + l + '_2'][j] = 'NaN';
				lc_data['phase_' + l + '_3'][j] = 'NaN';
			}
		}
	}
	lc_source.trigger('change');
	source.trigger('change');

	document.getElementById('rephased').innerHTML = 'Rephased period = ' + new_per.toFixed(3) + ' d';
}