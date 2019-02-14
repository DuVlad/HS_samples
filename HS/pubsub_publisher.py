from google.cloud import pubsub_v1
import json
import os

def produce(topic, message):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/eduardo/personal_git/HS_samples/.settings/jsonfile.json"
    project = 'googlecloudproject'
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic)
    message = bytes(json.dumps(message))
    future = publisher.publish(topic_path, data=message)
    print('Published {} of message ID {}.'.format(message, future.result()))