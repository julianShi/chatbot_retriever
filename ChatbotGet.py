import json

class ChatbotGet:

	def __init__(self):
		pass

	def return_message(self,request_id):
		buildings_dict = json.load(open('buildings_dict.json'))
		message_json={
		 "messages": [
			 {"text": buildings_dict[0]["building"]},
			 {"text": buildings_dict[0]["address"]}
		 ]
		}
		return message_json
