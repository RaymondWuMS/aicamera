import time
import os
import subprocess as sp
import sys
import shutil
import socket
import iot
import logging

#import iothub_client
#from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult, IoTHubError

# pylint: disable=E0611
#from iothub_client import IoTHubModuleClient, IoTHubClientError, IoTHubTransportProvider
#from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError

# messageTimeout - the maximum time in milliseconds until a message times out.
# The timeout period starts at IoTHubModuleClient.send_event_async.
# By default, messages do not expire.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.disabled = False
iot_msg_handler = iot.sendip_info_to_portal()

src = "./dlcHomePath/"
dst = "./Data/dlcFiles"
   
def getWlanIp():
    #if(os.name == "nt") :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        print("Ip address detected is :: " + IP )
        
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    #else :
        #wlanip = os.system("ifconfig wlan0 | grep \"inet\\ addr\" | cut -d: -f2 | cut -d\" \" -f1")
            #command::ifconfig br0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1
        # response,result = sp.getstatusoutput("ping -c1 -w2" + str(wlanip))
        # if(response == 0):
        #     return wlanip
        # else :
        #     print("Issue getting ip address try again please...outpt was :: %s",result)
        #     sys.exit()
        #return str(wlanip)
        #return "192.168.1.132"
def sendMsgToTwin(rtsp_stream_addr):
        # sending the rtsp stream to cloud iodedge as a device reported property as https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-python-twin-getstarted
        iot_msg_handler.iothub_client_sample_run(rtsp_stream_addr)

def sendMsgToCloud(message):
    try : 
        #hub_manger.forward_event_to_output("output1", message, 0)
        myhub_manager = iot.HubManager()
        myhub_manager.SendSimulationData(message)
        time.sleep(5)
    except Exception: 
        logger.exception("exception occured!!")
        pass

        
def transferdlc():
        files = os.listdir(src)
        for filename in files:
            print("transfering file :: " + filename)
            shutil.move(os.path.join(src,filename),os.path.join(dst,filename))
        #ToDO
            #add verification for file transfer and rteurn true or flase ...

        #need to improve this might be a good idea from heer one idea below but requires an addiotinal package netifaces...

        """import netifaces as ni 
            ni.ifaddresses('eth0')
            ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            print(ip)
        """




