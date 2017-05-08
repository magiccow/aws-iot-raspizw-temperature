import re
import json

def readTemp(sensorName):
  if sensorName:
    dir = '/sys/bus/w1/devices/%s/w1_slave' % sensorName
    with open(dir,'r') as f:
      lines = f.readlines()
      f.close()

      if 'YES' in lines[0]:
        match = re.search('t=(\d+)$',lines[1])
        if match:
          temp = float( match.group(1) ) / 1000
          return temp

  return 'unknown'






sensors = [ '28-000005a1fbf8', '28-000005a28f03']
while True:
  sensorName = sensors[ loopCount % 2 ]
  t = readTemp(sensorName)
  messageObject = { "temperature":t, "sensorid":sensorName  }
  message = json.dumps( messageObject )
  myAWSIoTMQTTClient.publish("temperature/%s" % sensorName, message, 1)
  loopCount += 1
  time.sleep(5)

