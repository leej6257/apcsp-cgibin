#!/bin/bash


echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Status: $rpi10</h1>"

echo "<pre>$(./rpisalive)</pre>"
