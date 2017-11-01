import urllib2
import json

import codecs
import sys

import os
path='C:\\Users\\
os.chdir(path)
# os.getcwd()

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link,about,posts&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "wehkamp.nl" # username or id
token = ""  # Access Token
page_data = get_page_data(page_id,token)


print "Page Name:"+ page_data['name']
print "Likes:"+ str(page_data['likes'])
print "Link:"+ page_data['link']
print "About:"+ page_data['about']
print page_data['posts']

#postobj = page_data['posts']

#print type(postobj)

#print postobj.keys()

#postobj2 = postobj['data']
#print 'postobj2' 
#print type(postobj2)

for i in range(1,len(postobj2)):
 # print "Posts:"+ postobj[i]
 print postobj2[i]

#print len(postobj2)
