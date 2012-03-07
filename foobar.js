var newURL = "http://singapore.menulog.com/lawrys_the_prime_rib_singapore/menus?menuId=277150";
if (document.getElementById('i').src != newURL) {
	console.log(document.getElementById('i').src);
	console.log(newURL);
	document.getElementById('i').src = newURL;
}
