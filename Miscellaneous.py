import urllib2

def checkInetConnection():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError: return False