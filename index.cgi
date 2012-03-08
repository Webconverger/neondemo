#!/bin/bash

exec 2>&1

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS

if test "${parm[0]}" == "macid"
then
	macid=$(/bin/busybox httpd -d "${parm[1]}")
fi

cat <<END
Cache-Control: no-cache
Content-Type: text/html

<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
</head>

<script id="manage"></script>

<iframe id="i" style="border: 0; width: 100%; height: 100%">Your browser doesn't support iFrames.</iframe>

<script src="main.js"></script>

</html>
END

if test "$macid"
then
	mkdir -p $macid
	cp control.cgi $macid/index.cgi
fi
