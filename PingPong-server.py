from flask import Flask, jsonify, request
from Contacts import check_id
from model.GCMMessage import Message
from worker import PushWorker

print 'server init'
app = Flask(__name__)
push_worker = PushWorker.PushThread()
push_worker.start()


@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    sender = request_data['sender']
    receiver = request_data['receiver']
    message_data = request_data['messageData']
    print 'Message accepted: sender=' + sender + ', receiver=' + receiver + ', messageData=' + message_data
    push_worker.put_message(Message(sender=sender, receiver=receiver, message_data=message_data))

    if not check_id(receiver):
        return jsonify(result=False, error_message='no receiver user found: '+receiver)

    return jsonify(result=True)

if __name__ == '__main__':
    app.run()
