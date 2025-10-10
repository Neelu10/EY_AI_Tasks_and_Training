import pika
import json
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.queue_declare(queue='student_tasks')
tasks={
    'student_id':101,
    'action':'generate_certificate',
    'email': 'jisoo@example.com'
}

channel.basic_publish(exchange='',
                      routing_key='student_tasks',
                      body=json.dumps(tasks))
print('Task sent to queue:', tasks)

connection.close()
