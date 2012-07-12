#!/bin/sh
cat <<END
Cache-Control: no-cache
Content-Type: text/plain

END

for i in */index.cgi
do
	if test $i = '*/index.cgi'
	then
		echo Already cleaned up.
		continue
	fi
	rm -vrf $(dirname $i)
done
