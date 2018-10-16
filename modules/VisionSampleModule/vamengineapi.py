""" 
import json
import logging
from collections import OrderedDict

class FaceDetection():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.disabled = False
    """
"""Face detection analytics engine
    Attribute:
        version :: version of VAM engine
        ??         ARE THESE NEED TO BE APRT OF THSI CALL
        Vam_id :: Unique Identification ID of VAM Engine
        atomic_rule_id :: unique id for rule 
        Event_Type :: Determines the VAM engine to be executed based on event type specified here for ex event type 8 loads face recognition as per published VAM engine devloped quide
        Rule_Name :: Assigns a name to the rule, can be any name that you want 
        Status – Enables (1) or disables (0) a VAM engine
        Sensitivity – Takes a value between 0 and 100 that determines how strictly a VAM engine is applied to a video sample. For example, in object tracking, low values result in objects needing to move substantially to be detected. High values cause the engine to detect slight movements, but may produce false positives
        myCustomParam – Differs based on event:
            eg. Loitering – The first reserve value specifies how long (in sec) an object must remain in a zone to trigger an event. The remaining four values should be 0.
        Zones – Allows for the definition of up to five zones to apply to a video sample
    """
    """
     #??Do they belong outsode this class as these will be same for all clsasses 
    version = "1.0"
    Vam_id = 'dcb25648-dd00-4613-a6a8-ee2388205318'
    atomic_rule_id = 'dcb25648-dd00-4613-a6a8-ee2388205318'
    Event_Type = 8 #change this to event type deifined by VAM engine
    Rule_Name = "Rule_Name"
    Status = 1 #need to find where will it go 
    def __init__(self, Sensitivity= None, myCustomParam= None):
        self.Sensitivity = Sensitivity
        self.Reserve = myCustomParam
       
    def getVaMRule(self):
        #jsonTxt = 'camera_id=0&vam_config={"version":"1.0","id":"dcb25648-dd00-4613-a6a8-ee2388205318","atomic_rules":[{"id" : "aee36598-4314-43bd-bf5e-dccad6391aa9","event_type":8,"name":"FR Rule","status":1,"sensitivity":15}]}'
        vam_config ={"version" : self.version, "id" : self.Vam_id, "atomic_rules" : [{"id" : self.atomic_rule_id, "event_type" : self.Event_Type, "name" : self.Rule_Name, "status" : self.Status, "sensitivity" : self.Sensitivity}]}
        myvam_config = OrderedDict(vam_config)
        vam_config = "vam_config=" + json.dumps(myvam_config)
        self.logger.info(vam_config)
        return vam_config
 """