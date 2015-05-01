
#Author:Ciaran Strutt
#Date:09/02/2015
#Description:Reads masscan .xml file and outputs the host, port and banner. I wrote
#this at 5am so it was just a quick script to make masscans output easier to look at

from lxml import etree as elementTree

fileName = ""

fileName = raw_input("Enter filename: ")

treeData = elementTree.parse(fileName)

root = treeData.getroot();


for singleElement in root.iter("address","service","port","state"):
        if singleElement.get("addr") !=  None:
                print "IP: %s" % singleElement.get("addr")
        if singleElement.get("portid") != None:
                print "Port: %s" % singleElement.get("portid")
        if singleElement.get("state") != None:
                print "State: %s" % singleElement.get("state")
        if singleElement.get("banner") !=  None:
                print "Banner: %s" % singleElement.get("banner")
