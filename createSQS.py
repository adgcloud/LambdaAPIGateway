import boto3

#Create a variable to target the sqs service
sqs = boto3.resource('sqs')

#Using the Boto3 commands, create a sqs queue and call it 'MySQSQueue' and store it in a variable
sqsqueue = sqs.create_queue(QueueName='MySQSQueue')

#Print the atttributes of the newly created Queue
print(sqsqueue)