from urllib2 import *
ip = raw_input('IP: ')
link = "http://api.hackertarget.com/subnetcalc/?q=" + ip
yes = urlopen(link).read()
print(yes)
