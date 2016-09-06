omegaCen RR Lyrae cut sample
----
* RR Lyrae matching and sample analysis done using matching_to_kaluzny.ipynb
* Futher documentation coming eventually - this summarises the main points.
* Matched the calibrated files to Kaluzny (2004) catalogues by positon - best match within a 10 pixel radius
* Examined image cutouts (+- 10 pixels in xy) and gloess fit light curves for each star to check quality
  - If good location match and lightcurve then accepted
  - If not good then went to second stage of light curve analysis
* 2nd stage analysis:
  - Look in more detail at gloess fitted light curve - can problem be resolve by rejecting single most discrepant point?
  - Plot light curves for all stars within +- 10 pixels (x and y) of predicted position from wcs transformation of Kaluzny coordinates to reference image
  - Look at mean mag, amplitude of star, position with respect to other stars on PL relation
* Criteria for rejection:
  - Star appears blended from light curve or position on PL
  - Bright neighbours within 4 pixel radius
  - Poor quality light curve
  - Close to edge of frame or bad regions on image
  
  