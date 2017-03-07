The Program can be used to automate attaching elastic IPs to instances in autoscaling group
The structure of the program is, autoscaling group calls SNS which calls Lambda
When SNS calls Lambda, SNS passes the details of the event which has just occured based on which Lambda attaches the free elastic IPs available to the instances
