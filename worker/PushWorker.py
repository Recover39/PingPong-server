import threading
import Queue
import traceback
import time
from model.GCMMessage import Message
from gcm import GCM
import Contacts


class PushThread(threading.Thread):
    def __init__(self):
        super(PushThread, self).__init__()
        self.gcm = GCM('AIzaSyC3CwECHoUqHKNQXbndpRWPjgauYhXTUEI')
        self.message_queue = Queue.Queue()
        self._break = False

    def stop_thread(self):
        self._break = True

    def run(self):
        print 'worker is running...'
        while not self._break:
            if not self.message_queue.empty():
                message = self.message_queue.get()

                try:
                    print 'worker does his job: ' + message.__str__()
                    reg_id=Contacts.ids[str(message.receiver)]
                    data = message.jsonify()
                    print data
                    self.gcm.plaintext_request(registration_id=reg_id, data=data)
                except:
                    traceback.print_exc()
            else:
                time.sleep(5)
        print 'worker got off the work'

    def put_message(self, gcm_message):
        if isinstance(gcm_message, Message):
            self.message_queue.put(gcm_message)
        else:
            print 'put_message error'
