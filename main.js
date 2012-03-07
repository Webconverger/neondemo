setInterval(function() {
var nocache = Math.random();
document.getElementById('manage').src = "foobar.js?" + nocache;
}, 2000);
