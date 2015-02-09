# masscan-parser

Reads masscan .xml file and outputs the host, port and banner. I wrote
this at 5am so it was just a quick script to make masscans output easier to look at.

Usage example
./masscan -p 80 10.0.0.0/8 --source-port 60000 --rate 1000 --banners -oB banners

./masscan --open --banners --readscan banners -oX banner_plot

python parse.py banner_plot

Then enjoy the output :)
