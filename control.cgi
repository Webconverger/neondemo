#!/bin/bash

exec 2>&1

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS

if test "${parm[0]}" == "page"
then
	page=$(/bin/busybox httpd -d "${parm[1]}")
fi

cat <<END
Cache-Control: no-cache
Content-Type: text/html

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>$page</title>
    </head>
<body>

<form action="/control.cgi" method="get">
  Page: <input type="url" name="page" size=50 value="$page"/><br />
  <input type="submit" value="Submit" />
</form>

<ul>
<li><a href="http://sg.webconverger.com/control.cgi?page=http%3A%2F%2Fsingapore.menulog.com%2Flawrys_the_prime_rib_singapore%2Fmenus%3FmenuId%3D277150">Menu demo</a></li>
<li><a href="http://sg.webconverger.com/control.cgi?page=http%3A%2F%2Fplay.renewchannel.com%2F">Renew demo</a></li>
<li><a href="http://sg.webconverger.com/control.cgi?page=http%3A%2F%2Fnews.bbc.co.uk%2F">BBC news</a></li>
</ul>


END

if ! test "$page"
then
	echo Missing page argument
	exit
fi

cat <<END > foobar.js
var newURL = "$page";
if (document.getElementById('i').src != newURL) {
	console.log(document.getElementById('i').src);
	console.log(newURL);
	document.getElementById('i').src = newURL;
}
END

echo "<h1>$page updated on $(date)!</h1>"
