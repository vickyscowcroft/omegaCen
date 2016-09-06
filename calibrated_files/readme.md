omegaCen RR Lyrae cut sample
===
RR Lyrae matching and sample analysis done using matching_to_kaluzny.ipynb

Further documentation coming eventually - this summarises the main points.

* Matched the calibrated files to Kaluzny (2004) catalogues by positon - best match within a 10 pixel radius
* Examined image cutouts (+- 10 pixels in xy) and gloess fit light curves for each star to check quality
  - If good location match and good(ish) light curve then accepted
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
  
**Final Files**: 
--

The final files with the cut samples are as follows:

omegaCen_1_3p6um_rrl_matched_to_kaluzny.cut

omegaCen_1_4p5um_rrl_matched_to_kaluzny.cut

omegaCen_2_3p6um_rrl_matched_to_kaluzny.cut

omegaCen_2_4p5um_rrl_matched_to_kaluzny.cut

omegaCen_3_3p6um_rrl_matched_to_kaluzny.cut

omegaCen_3_4p5um_rrl_matched_to_kaluzny.cut
  

rematch function
---
The rematch function within the matching_to_kaluzny notebook works to accept and reject the original match stars right now, but the part of the function that allows the user to chose and alternative star is not yet functional. It does display the light curves and positions of the other nearby stars. It does what I need it to do. Feel free to try to implement this part. 


  
  