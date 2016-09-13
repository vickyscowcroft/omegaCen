function setscale() {
    var smin;
    var smax;
    var smin_str = document.getElementById("scalemin").value;
    var smax_str = document.getElementById("scalemax").value;
    if (smin_str.length == 0) {
        smin = JS9.GetScale({display:"image1"}).scalemin;
    } else {
        smin = parseFloat(smin_str);
    }
    if (smax_str.length == 0) {
        smax = JS9.GetScale({display:"image1"}).scalemax;
    } else {
        smax = parseFloat(smax_str);
    }
    JS9.SetScale(smin, smax, {display: "image1"});
    JS9.SetScale(smin, smax, {display: "image2"});
    JS9.SetScale(smin, smax, {display: "image3"});
    JS9.SetScale(smin, smax, {display: "image4"});
    JS9.SetScale(smin, smax, {display: "image5"});
    JS9.SetScale(smin, smax, {display: "image6"});
    return false;
};
