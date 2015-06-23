# masscan-parser

Reads masscan .xml file and outputs the host, port and banner. I wrote
this at 5am so it was just a quick script to make masscans output easier to look at.

Usage example

./masscan/bin/masscan -p 80 --banners 78.0.0.0/8 --rate=5000 --excludefile masscan/data/exclude.conf --open --source-port 60000 -oX ~/scanoutput.xml

python parse.py

Sample Output
IP: 78.0.105.136
Port: 80
State: open
Banner: HTTP/1.1 401 Unauthorized\x0d\x0aConnection: close\x0d\x0aContent-Type: text/html; charset=ISO-8859-1\x0d\x0aWWW-Authenticate: Basic realm=\x22server\x0d\x0aContent-Length: 166\x0d\x0a\x0d



