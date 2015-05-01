# masscan-parser

Reads masscan .xml file and outputs the host, port and banner. I wrote
this at 5am so it was just a quick script to make masscans output easier to look at.

Usage example

./masscan/bin/masscan -p 80,21,22,23 --banners 78.0.0.0/8 --rate=5000 --excludefile masscan/data/exclude.conf --open --source-port 60000 -oX ~/scanoutput.xml

python parse.py

Then enjoy the output :)

I decided what I am going to do with this script, I am planning on using it to parse masscan output then insert it into a mysql DB and then build some php to make it searchable from a browser.
