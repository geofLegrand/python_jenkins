
import boto3
from pprint import pprint


ec2 = boto3.client('ec2',region_name='us-east-1')

def lambda_handler(event="",context=""):
    try:
        des = ec2.describe_instances()
        print(len(des["Reservations"]))
        pprint(des["Reservations"][0]["Instances"][0]["InstanceId"])
        return des["Reservations"][0]["Instances"][0]["InstanceId"]

    except:
        print("Erreur")



    

def stop_instance(id_instance):
    try:

        response = ec2.stop_instances(InstanceIds=[id_instance])

        return {
            'statusCode': 200,
            'body': f"EC2 instance {id_instance} stopped successfully !"
        }
    except Exception as e :
    
     return {
        'statusCode': 500,
        'body': f"Failed to start EC2 instance {id_instance}"
    }




def start_instance(id_instance):
    try:
        response = ec2.start_instances(InstanceIds=[id_instance])
        return {
            'statusCode': 200,
            'body': f"EC2 instance {id_instance} stated successfully !"
        }
        
    except Exception as e:
        print(e)

    return {
        'statusCode': 500,
        'body': f"Failed to start EC2 instance {id_instance}"
    }


id = lambda_handler()

stop_instance(id)