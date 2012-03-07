setInterval(function() {
var nocache = Math.random();
var script = document.createElement('script')
script.src = "foobar.js?" + nocache;
document.body.appendChild(script)
}, 2000);
