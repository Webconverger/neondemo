#!/bin/bash

exec 2>&1

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS

if test "${parm[0]}" == "mac"
then
	mac=$(/bin/busybox httpd -d "${parm[1]}")
fi

cat <<END
Cache-Control: no-cache
Content-Type: text/html

<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
<link id='theme' rel='stylesheet' href='bigbox.css'/> <!-- humane theme -->
<script src="humane.min.js"></script>
<script src="main.js"></script>
<style>
  div {border: 0; width: 100%; height: 100%; overflow:hidden}
  iframe {border: 0; width: 100%; height: 100%; overflow:hidden}
</style>
</head>
<body>

<script id="manage"></script>

<div>
<iframe id="i">Your browser doesn't support iFrames, get <a href="http://neon.webconverger.com/">Neon</a> that does.</iframe>
</div>


</body>

</html>
END

if test "$mac"
then
	mkdir -p $mac
	cp control.cgi $mac/index.cgi
fi
