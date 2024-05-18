import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
.venv\Scripts\activate
python listen_for_messages.py
listen_for_messages.py
pika
python -m pip install -r requirements.txt
python util_about.py
python util_aboutenv.py
python util_aboutrabbit.py
pip list
python v1_emit_message.py
python v1_listen_for_messages.py
python v1_emit_message.py
import pika

message = "New Message"

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body=message)
print(f" [x] Sent '{message}'")
connection.close()
python util_about.py
python util_aboutenv.py
python util_aboutrabbit.py
pip list
