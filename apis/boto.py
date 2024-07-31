import boto3
from pprint import pprint

ec2 = boto3.client('ec2',region_name='us-east-1')
response = ec2.describe_instances()
print(type(response))
pprint(response)