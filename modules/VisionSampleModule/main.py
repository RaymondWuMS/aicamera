# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import time
import sys
#import iothub_client
import requests
import json
import os
import iot

#local modules
#import vamengineapi
from cameraapi import CameraClient
import utility

# Choose HTTP, AMQP or MQTT as transport protocol.  Currently only MQTT is supported.
#PROTOCOL = IoTHubTransportProvider.MQTT

def main(protocol=None):
    print ( "\nPython %s\n" % sys.version )
    print ( "IoT Hub Client for Python" )
    
    #generate a new folder based on time and then copy into that folder ....

    with CameraClient.Connect() as camera_client:        
        
        # starting camera (this starts the preview RTSP stream)
        camera_client.set_preview_mode(True)
        print("Start VLC Media player and watch the live rtsp stream for 60 secs") #need to extract the stream address and display here 
        #utility.transferdlc()
        #time.sleep(4)
        #Setting dlc file path 

        #Loading your model to hardware for inferencing and getting results

        #camera_client.setVAM_Rule(True,"FR")
        camera_client.loadVAM("MD") 

        print ( "The sample is now waiting for messages and will indefinitely.  Press ctrl-C to exit. ")
        time.sleep(10)

        hub_manager = iot.HubManager()
        while(True):
           #hub_manager.SendMsgToCloud("Hallo from module!!!")
            time.sleep(10)

if __name__ == '__main__':
    #main(PROTOCOL)
    main()
