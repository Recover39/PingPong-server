class Message:
    def __init__(self, sender=None, receiver=None, message_data=None):
        self.sender = sender
        self.receiver = receiver
        self.message_data = message_data

    def jsonify(self):
        return {'sender': self.sender, 'receiver': self.receiver, 'messageData': self.message_data}

    def __str__(self):
        return 'sender='+self.sender+', receiver='+self.receiver+', message_data='+self.message_data