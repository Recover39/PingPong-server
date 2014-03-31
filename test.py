# -*- coding: utf-8 -*-
import requests
import json

# load = {"sender": "Namhoon", "receiver": "Sugarpoint", "messageData": "Let the game begin"}
load = {"sender": "Namhoon", "receiver": "Sugarpoint", "messageData": "Let the game begin"}
print(load)
r = requests.post('http://10.73.45.162:5000', data=json.dumps(load), headers={"Content-Type": "application/json"})
# r = requests.post('http://127.0.0.1:5000', data=json.dumps(load), headers={"Content-Type": "application/json"})
print(r.status_code)
print(r.text)




# from model.GCMMessage import Message
#
# message = Message(receiver='a', sender='b', message_data='hello')
# print (message)






# import traceback
# from gcm import GCM
#
# gcm = GCM('AIzaSyC3CwECHoUqHKNQXbndpRWPjgauYhXTUEI')
# import Contacts
# id = Contacts.ids['Sugarpoint']
# data = {'messageData': 'kkk'}
#
# try:
#     gcm.plaintext_request(registration_id=id, data=data)
# except:
#     traceback.print_exc()