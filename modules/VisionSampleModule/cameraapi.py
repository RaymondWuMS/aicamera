import sys
#import vamengineapi
import utility
from contextlib import contextmanager
from ipcprovider import IpcProvider

class CameraClient():

    @staticmethod
    @contextmanager
    def Connect(connection=None):

        if connection is None:
            connection = IpcProvider()

        connection.connect()
        try:
            yield CameraClient(connection)
        finally:
            connection.logout()

    def __init__(self, connection):
        self.connection = connection

    def set_preview_mode(self, status):
        path = "/preview"
        payload = {'switchStatus' : status}
        response = self.connection.post(path, payload)
        if(response):
            #This starts a rtsp stream over a local area network
            # We are sending the rtsp address to iotedge device twin for user to copy and start streaming 
            rtsp_stream_addr = "rtsp://" + utility.getWlanIp() + ":8900/live"
            #utility.sendMsgToTwin(rtsp_stream_addr)
        return response

    def getPreviewInfo(self):
        path = "/preview"
        payload = '{ }'
        response = self.connection.post(path, payload)
        return response

    def getVAMInfo(self):
        path = "/vam"
        payload = '{ }'
        response = self.connection.post(path, payload)
        return response
    
    def loadVAM(self, text):
        payload = {"switchStatus" : True, "vamconfig" : text}
        path = "/vam"
        response = self.connection.post(path, payload)
        return response

    # def setVAM_Rule(self, status, rule ):
    #     url = "http://" + self.info['ip'] + ":" + self.info['port']
    #     if (status):
    #         path = '/vamconfig'
    #     else:
    #         path = '/vamremoveconfig'
    #     param = 'type=' + rule
    #     test = vamengineapi.FaceDetection(15)
    #     test.Status = 1 # setting to activate the Rule
    #     payload = 'camera_id=0&' + test.getVaMRule()
    #     response = self.connection.post(path, payload,param)
    #     return response


    def setOverlay(self, status):
        path = "/overlay"
        payload = {"switchStatus" : status }
        response = self.connection.post(path, payload)
        return response
        
    def configOverlayText(self, text):
        path = "/overlayconfig"
        payload ={"ov_type_SelectVal" : 0, "ov_position_SelectVal" : 0,"ov_color" : "869007615","ov_usertext": text,"ov_start_x":0,"ov_start_y":0,"ov_width":0,"ov_height":0}
        response = self.connection.post(path, payload)
        return response

    def LogoutHandler(self):
        path =  "/logout"											
        response = self.connection.post(path)
        return response
