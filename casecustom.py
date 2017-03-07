#!/usr/local/bin/python2.7

import sys, datetime, json
import boto3

global eip_eipid
eip_eipid = {
                    "13.55.30.191" : "eipalloc-faa0899f",
                    "52.63.108.151" : "eipalloc-7ea1881b"
            }



def eip_instanceid_map(eip_eipid):
    print eip_eipid

def parse_event_json():
    """This function would take the json coming from SNS and look out for the instance which is being deployed now"""

def is_instance_running():
    """This function will check for the instance state to change from 'starting' to 'running'"""

def associate_eip_instanceid():
    """Once instance come back to running state, add the instanceid to the elastic ip resource id"""


eip_instanceid_map(eip_eipid)
