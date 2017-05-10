# AWS IoT - Lambda - S3 demo for RasPiZW

Demonstration of Raspberry Pi Zero W with Dallas DS18B20 1-wire temperature sensor sending data
to Amazon AWS-IOT where the data can be fed into AWS Lambda and used to update a JSON store on 
Amazon S3.

Youtube video:  TBA


## Files

- add-to-aws-sdk.py	  - code fragment for the Raspberry Pi to read the DS18B20 temperature sensor
- lambda.py			  - early version of the script that does some calculations and updates the JSON file
- lambda_function_s3.py - version of code from the video that simply writes to the S3 bucket
- 28_000*.json		  - JSON file that was written to S3 while testing the lambda


