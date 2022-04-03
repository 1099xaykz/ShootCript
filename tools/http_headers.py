from urllib2 import *
v2 = raw_input("Domain: ")
link = "http://api.hackertarget.com/httpheaders/?q=" + v2
yes = urlopen(link).read()
print(yes)