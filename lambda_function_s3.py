import json
import boto3

def lambda_handler(event, context):
    key = event['sensorid'] + '.json'
    writeToS3(key, event['temperature'])
    return True
	
def writeToS3(key,value):
    s3 = boto3.resource('s3')
    jsonData = json.dumps( { "temperature":value } )
    s3.Bucket('temperature-readings').put_object(Key=key,Body=jsonData)
    return
