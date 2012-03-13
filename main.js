function getQueryVariable(variable) {
	var query = window.location.search.substring(1);
	var vars = query.split("&");
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split("=");
		if (pair[0] == variable) {
			return unescape(pair[1]);
		}
	}
}

uniqueID = getQueryVariable("mac");
humane.timeout = 0;
if (uniqueID) {
humane.info("Control this demo by scanning <br> <img src=\"https://chart.googleapis.com/chart?chs=547x547&cht=qr&chl=http://" + window.location.hostname + "/" + uniqueID + "&choe=UTF-8\">");
setInterval(function() {
var nocache = Math.random();
var script = document.createElement('script')
script.src = uniqueID + "/main.js?" + nocache;
document.body.appendChild(script)
}, 1000);
} else {
humane.error("Please specify a /?mac= query");
}
