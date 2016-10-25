#!/usr/bin/env python
# Check to validate rabbitmq connectivity
# This is an alternative to the management plugin and rabbitmqadmin
# Note rabbitmqadmin is available from http://<rabbitmq>:15672/cli/
# and should be saved in /usr/local/bin
#
# Usage: check_rabbit.py --host myhost --port 5672 --user myuser --password mypassword --vhost /
# Usage: check_rabbit.py --host myhost --port 5672 --user myuser --password mypassword --vhost / --ssl True

import socket
from kombu import Connection
import argparse
host = ""
port = ""
user = ""
password = ""
vhost = ""
use_ssl = ""

parser = argparse.ArgumentParser(description='RabbitMQ Connection Check (check_rabbit.py')
parser.add_argument('--host', help='RabbitMQ Host Name',required=True)
parser.add_argument('--port', help='RabbitMQ Port',required=True)
parser.add_argument('--user', help='RabbitMQ User',required=True)
parser.add_argument('--password', help='RabbitMQ Password',required=True)
parser.add_argument('--vhost', help='RabbitMQ Virtual Host',required=True)
parser.add_argument('--ssl', help='RabbitMQ Use SSL',required=False)
args = parser.parse_args()

host = args.host
port = args.port
user = args.user
password = args.password
vhost = args.vhost
use_ssl = args.ssl

if use_ssl == "":
    use_ssl = False

if str(use_ssl).lower() == "true":
    use_ssl = True
else:
    use_ssl = False

url = 'amqp://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, vhost)
with Connection(url,ssl=use_ssl) as c:
    try:
        c.connect()
    except socket.error:
        raise ValueError("Received socket.error, "
                         "rabbitmq server probably isn't running")
    except IOError:
        raise ValueError("Received IOError, probably bad credentials")
    else:
        print "Credentials are valid"
        c.release()


