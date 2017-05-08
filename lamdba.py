import json
import boto3

def lambda_handler(event, context):
    name = event['sensorid'] + '.json'
    stats = readStats(name)
    updateStats(float(event['temperature']), stats)
    writeStats(name,stats)
    return True
    
    

def readStats(name):
    s3 = boto3.resource('s3')
    try:
        file = s3.Object('temperature-readings',name).get()
        jsonData = file['Body'].read().decode('utf-8')
        result = json.loads(jsonData)
    except:
	    # fill in zero values
	    result = {"last-value": 0, "sum": 0, "max-value": False, "mean-value": False, "min-value": False, "count": 0}
    return result
	
def writeStats(name,values):
    s3 = boto3.resource('s3')
    jsonData = json.dumps(values)
    s3.Bucket('temperature-readings').put_object(Key=name,Body=jsonData)
    return
	
	
def updateStats(latestReading,values):
    values['last-value'] = latestReading
    if values['max-value']==False or latestReading>values['max-value']:
        values['max-value']=latestReading
    if values['min-value']==False or latestReading<values['min-value']:
        values['min-value']=latestReading
    values['sum'] += latestReading
    values['count'] += 1
    values['mean-value'] = float(values['sum']) / values['count']
    return

