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

<form action="index.cgi" method="get">
  Page: <input type="url" name="page" size=60 value="$page"/><br />
  <input type="submit" value="Submit" />
</form>

<ul>
<li><a href="index.cgi?page=http%3A%2F%2Fneon.webconverger.com%2F">Neon main</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fneon.webconverger.com%2Fcase-study%2F">Neon case study</a></li>
<li><a href="index.cgi?page=https%3A%2F%2Frvashow.appspot.com%2FViewer.html%3Ftype%3Ddisplay%26id%3D36e8dd70-34af-4faf-9c39-991d54a87259">Rise test card</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fwebconverger.com%2F">Webconverger</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fwww.gov.sg%2F">gov.sg</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fwww.smu.edu.sg%2F">SMU</a></li>
<li><a href="index.cgi?page=http%3A%2F%2F192.168.5.1%3A8080%2F%3Faction%3Dstream">webcam</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fwww.straitstimes.com%2F">Straits Times</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fwww.fish-co.com/menu/fish-bites">Menu demo</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fplay.renewchannel.com%2F">Renew demo</a></li>
<li><a href="index.cgi?page=http%3A%2F%2Fnews.bbc.co.uk%2F">BBC news</a></li>
</ul>

<p><a href="https://github.com/Webconverger/neondemo">Source code</a></p>

END

if ! test "$page"
then
	echo Missing page argument
	exit
fi

test "$(basename $0)" = "index.cgi" || exit

cat <<END > main.js
humane.remove()
var newNeonURL = "$page";
if (document.getElementById('i').src != newNeonURL) {
	document.getElementById('i').src = newNeonURL;
}
END

echo "<h1>$page updated on $(date)!</h1>"
