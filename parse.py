...
Author:Ciaran Strutt
Date:09/02/2015
Description:Reads masscan .xml file and outputs the host, port and banner. I wrote
this at 5am so it was just a quick script to make masscans output easier to look at
...
import xml.etree.ElementTree as ET
import sys


def parseinfo(filename):
        tree = ET.parse(filename) #Create an element tree from the xml file
        root = tree.getroot() #Grab the root tag of the xml tree

        hosts = tree.iter('address') #Iterate the children of the tag address
        ports = tree.iter('port') #same as above
        banners = tree.iter('service') #same as above

        for ip in hosts: #print out each ip,port and banner
                try:
                        print "Host: " + hosts.next().attrib['addr']
                        print "Port: " + ports.next().attrib['portid']
                        print "Banner: " + banners.next().attrib['banner']
                except StopIteration: #Just means end of file has been reached
                        print "EOF"


def main():
        if(len(sys.argv) < 2):
                print "Usage python parse.py filename"
parseinfo(sys.argv[1])

if __name__ == '__main__':
        main()