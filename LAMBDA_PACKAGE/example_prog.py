#!/usr/local/bin/python2.7

import boto3
import json, re
import ast

"""
The function lambda_handler is the entry point of the Lambda function.
"client" is the object of the class boto3.client to be used to call ec2 APIs
eip_map = Return function value which would create a json with "eip", "instanceid" and "allocationid"
instanceid = Return function value after parsing the json from SNS
attach_free_eip_with_instance = function to attach the newly created instance ( with instance id instanceid ) with the free elastic ip ( obtained from eip_map dictionary)
"""

def lambda_handler(event, context):
    client = boto3.client('ec2', 'ap-southeast-2')
    eip_map = eip_instanceid_map(client)
    print eip_map
    instance_id = parse_event_json(event)
    print instance_id
    attach_free_eip_with_instance(client, instance_id, eip_map)


def eip_instanceid_map(client):
    "Defining the dictionary with elastic ip, allocationid and instanceid"
    eip_map = {}
    eip_map_list = []

    eip_eipid = client.describe_addresses()
    for address in eip_eipid['Addresses']:
        if 'PublicIp' in address.keys() and address['PublicIp'] in { 'YY.YY.YY.YY', 'XX.XX.XX.XX' }:
""" Key in the elastic Ips you have configured to be used on the instances  ^  and        ^ """
            eip_map['eipaddress'] = address['PublicIp']
            eip_map['allocationid'] = address['AllocationId']
            if 'InstanceId' in address:
                eip_map['instanceid'] = address['InstanceId']
            else:
                eip_map['instanceid'] = ''
            if bool(eip_map):
                eip_map_list.append(eip_map)
                eip_map = {}

    print eip_map_list
    return(eip_map_list)

def parse_event_json(event):
    import ast
    for element in event:
        for record in event[element]:
            for key, item in record.items():
                if key == 'Sns':
                    message_dict = ast.literal_eval(item['Message'])
                    for message_topic, message_details in message_dict.items():
                        return(message_dict['EC2InstanceId'])

def attach_free_eip_with_instance(client, instance_id, eip_map_list):
    for item in eip_map_list:
        if item['instanceid'] == '':
            print item['instanceid']
            print item['allocationid']
            client.associate_address(InstanceId=instance_id, AllocationId=item['allocationid'])
