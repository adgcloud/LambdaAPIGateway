import boto3

#Create a variable to target the sqs service
sqs = boto3.resource('sqs')

sqsqueue = sqs.create_queue(QueueName='MySQSQueue')

print(sqsqueue)