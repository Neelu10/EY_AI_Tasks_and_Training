import pika
import time
import json
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

channel.queue_declare(queue='student_tasks')
def callback(ch, method, properties, body):
    task=json.loads(body)
    print('Received',task)
    time.sleep(2)
    print("task processed for student",task['student_id'])

channel.basic_consume(queue='student_tasks', on_message_callback=callback, auto_ack=True)
print('waiting for message.Press CTRL+C to exit.')
channel.start_consuming()
