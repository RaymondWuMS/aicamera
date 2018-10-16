import requests
import json
import traceback
import sys
import logging
import utility

def convert(obj):
    if isinstance(obj, bool):
        return str(obj).lower()
    if isinstance(obj, (list, tuple)):
        return [convert(item) for item in obj]
    if isinstance(obj, dict):
        return {convert(key):convert(value) for key, value in obj.items()}
    return obj   	

class IpcProvider():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.disabled = False

    def __init__(self, ip_address=None, port=None, username=None, password=None, session_token=None):
        if ip_address is None:
            #ip_address = '127.0.0.1'
            ip_address = utility.getWlanIp()
            #ip_address = '172.17.0.1'

        if port is None:
            port = '1080'

        if username is None:
            username = 'admin'

        if password is None:
            password = 'admin'

        self.username = username
        self.password = password
        self.ip_address = ip_address
        self.port = port
        self.session_token = session_token

    def showError(self, errMsg):
        self.logger.error(errMsg)

    def get_function_name(self):
        return traceback.extract_stack(None, 2)[0][2]

    def buildUrl(self,path,params=None):
            return "http://" + self.ip_address + ":" + self.port + path

    def post(self,path,payload=None,param=None,returnresponse=False):
        try:    
            with requests.session() as mysession:
                
                url = self.buildUrl(path)
                payload_data = json.dumps(payload)
                #payload_data = json.dumps(convert(payload))
                self.logger.info("API: " + url + ",data:" + payload_data)
                headers = {'Cookie': self.session_token}
                if(param == None) :
                    response = mysession.post(url, data=payload_data, headers=headers)
                else :
                    response = mysession.post(url, data=payload_data, param=param, headers=headers)

                self.logger.info("RESPONSE: " + response.text)
                
                #returning repsonse as is 
                if(returnresponse):
                    return response
                #need to add check for response if not 200 or 201 then fail and send False back...
                return True
            return False
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Exceptions raised in %s ',self.get_function_name(),exc_info=True)
            self.showError("Got Exception in function name :: " + self.get_function_name() + ", try again")
            raise
    
    def connect(self):
            with requests.session() as mysession:
                try:
                    payload = "{\"username\": \"%s\", \"userpwd\": \"%s\"}" % (self.username, self.password)
                    url = "http://" + self.ip_address + ":" + self.port + "/login"
                    #self.logger.info("API: " + url + ",data: " + json.dumps(payload,sort_keys=True))
                    print("URL: " + url + " data: " + payload)
                    #response = mysession.post(url, data=json.dumps(payload, sort_keys= True))
                    response = mysession.post(url,data=payload)
                    self.logger.info("LOGIN RESPONSE: " + response.text)
                    jsonResp = json.loads(response.text)
                    if jsonResp['status']:
                        self.session_token = response.headers['Set-Cookie']
                        print("connection established with session token: [%s]" % self.session_token)
                        return True
                    else:
                        raise ConnectionError("Failed to connect. Server returned status=False")

                except requests.exceptions.Timeout:
                    # TODO: user should have a way to figure out if required services are running or not? maybe some simple URL
                    self.showError("Timeout: Please check that the device is up and running and the IPC service is available")
                    raise
                except requests.exceptions.RequestException as e:
                    self.logger.exception(e.strerror)
                    raise

    def logout(self):
        try:
            path =  "/logout"
            self.post(path)
        except:
            print("failed to logout gracefully")
