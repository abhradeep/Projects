#!/usr/local/bin/python2.7

import json


event = {u'Records': [{u'EventVersion': u'1.0', u'EventSubscriptionArn': u'arn:aws:sns:ap-southeast-2:657171319757:casecustomtopic:1fe8a0b8-f44a-43ac-b737-89e346f3169b', u'EventSource': u'aws:sns', u'Sns': {u'SignatureVersion': u'1', u'Timestamp': u'2017-03-04T01:17:31.991Z', u'Signature': u'DgtZLX+h+vd+pTzDpNdktfaMcApEQcJ/KNreCTvYyXw7q+eI4K+ZuPv8SpcXOyN6QQuHXtcUwiIY3DEJ4hhOVhXNuJLCaEEwuVVM3ZXvsRnyO0JAgFKVFbL5ZluFofNR0TC6mbtjMqVvso2UGGZ6OLexefFh6d7OwRDs1aqKJ7QzZcCtU2ysHXqkreGfJnWPLYhs1t13Bht/l1swmz2bAz72RbboLsUZFpGUu9sv5rEe+q+HaYm9PEtKI9pka52/N6rq1MdiBVOerTf4BTxK7T8FZ1rr+qUmjQaUrFEOJL48SgD+3vKw6RSUSoEzRX6+ly3yQ4IRen09UnJvlXykng==', u'SigningCertUrl': u'https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-b95095beb82e8f6a046b3aafc7f4149a.pem', u'MessageId': u'ca6260ba-2e29-5d02-9392-318e39c28386', u'Message': u'{"Progress":50,"AccountId":"657171319757","Description":"Launching a new EC2 instance: i-0d0d8057463572455","RequestId":"5b2a195e-3211-4c56-9c10-3d32a35fa0f8","EndTime":"2017-03-04T01:17:31.945Z","AutoScalingGroupARN":"arn:aws:autoscaling:ap-southeast-2:657171319757:autoScalingGroup:6fb71ecb-6081-41f3-a793-0040458f7181:autoScalingGroupName/casecustomasg","ActivityId":"5b2a195e-3211-4c56-9c10-3d32a35fa0f8","StartTime":"2017-03-04T01:16:59.486Z","Service":"AWS Auto Scaling","Time":"2017-03-04T01:17:31.945Z","EC2InstanceId":"i-0d0d8057463572455","StatusCode":"InProgress","StatusMessage":"","Details":{"Subnet ID":"subnet-9c0f90ea","Availability Zone":"ap-southeast-2b"},"AutoScalingGroupName":"casecustomasg","Cause":"At 2017-03-04T01:16:57Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 1 to 2.","Event":"autoscaling:EC2_INSTANCE_LAUNCH"}', u'MessageAttributes': {}, u'Type': u'Notification', u'UnsubscribeUrl': u'https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:657171319757:casecustomtopic:1fe8a0b8-f44a-43ac-b737-89e346f3169b', u'TopicArn': u'arn:aws:sns:ap-southeast-2:657171319757:casecustomtopic', u'Subject': u'Auto Scaling: launch for group "casecustomasg"'}}]}

for element in event:
    """print record
    print event[record]
    print type(event[record])
    print event[record][0]
    print type(event[record][0])"""
    for record in event[element]:
        for key, item in record.items():
            if key == 'Sns':
                print "printing sns message type"
                print type(item['Message'])
                print item['Message']
                for i in item['Message'].dict():
                    print i

                #if item['Message']['EC2InstanceId'] == 'autoscaling:EC2_INSTANCE_LAUNCH':
                #    instanceid = item['Message']['EC2InstanceId']


                #print instanceid

                '''
                for topic, details in item.items():
                    print "+++++++++++++"
                    if topic == 'Message':
                        print item[topic]
                        type(item[topic])
                        """for message_topic, message_details in item[topic].items():
                            pass"""
                '''





    """
    for record in event_from_sns['Records']:
        for item in record[0]:
            if item == 'Sns':
                sns_event = record[0]['Sns']

    for key, item in sns_enent.items():
        if key == 'Message':
            for message_topic, message_details in sns_enent['Message'].items():
                if message_details == 'autoscaling:EC2_INSTANCE_LAUNCH':
                    instanceId = sns_event['Message']['EC2InstanceId']
                print instanceId
    """
