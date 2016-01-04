import os

from fishbowl import objects
from . import utils


class PartTest(utils.ObjectTest):
    xml_filename = os.path.join(os.path.dirname(__file__), 'part.xml')
    fishbowl_object = objects.Part
    expected = {
        'ActiveFlag': True,
        'Configurable': True,
        'Description': 'Custom Value Bike',
        'HasBOM': False,
        'Height': 0,
        'Len': 0,
        'Num': 'BB2005',
        'PartClassID': 0,
        'PartID': 60,
        'SerializedFlag': True,
        'StandardCost': '0',
        'TrackingFlag': True,
        'TypeID': 10,
        'Weight': 0,
        'Width': 0,
    }
