#!/usr/bin/python2.7

import sys, datetime, os
import boto3

print "Initializing ..."
messenger = boto3.client('sns', 'ap-southeast-2')

def listAllTopics(client):
    return(client.list_topics())

def publishToTopic(client, topicarn, message, subject):
    print "Publishing to the topic %s"%(topicarn)
    print topicarn, message, subject
    try:
        client.publish(TopicArn=topicarn, Message=message, Subject=subject)
    except:
        print "There has been some problem in publishing"



allTopics = listAllTopics(messenger)
print allTopics

publishToTopic(messenger, 'arn:aws:sns:ap-southeast-2:657171319757:PushMessageTopicSydney', 'someMessage100', 'someSubject100')
