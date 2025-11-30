import requests
from requests import Response
import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.DEBUG)

class AipHelper:

   def __init__(self,timeout):
       self.timeout = timeout

   def getCall(self,url,headers=None,params=None):
        return requests.get(url,headers=headers,params=params)

   def postCall(self,url,json=None,headers=None,params=None):
       return requests.post(url,json=json,headers=headers,params=params)

   def putCall(self,url,headers=None,params=None,json=None):
        return requests.put(url,headers=headers,json=json,params=params)


   def deletCall(self, url, headers=None, params=None, json=None):
       return  requests.delete(url, headers=headers, json=json, params=params)




   def getResponseAsText(self,responseObject):
       if type(responseObject) == Response:
           return responseObject.text
       return None


