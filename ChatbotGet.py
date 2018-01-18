import json

class ChatbotGet:

	def __init__(self):
		pass

	def _find_building(self,building_abbreviation):
		buildings_dict = json.load(open('buildings_dict.json'))
		message_json={
		 "messages": [
			 {"text": "Building not found"},
		 ]
		}
		for building in buildings_dict:
			if (building["abbreviation"] == building_abbreviation.upper()):
				message_json={
				 "messages": [
					 {"text": building["building"]},
					 {"text": building["address"]}
				 ]
				}
				break
		return message_json
		
	def return_message(self,request_id):
		request_message=request_id.split('/')
		script=request_message[0]
		file=request_message[1]
		if script == "building":
			return self._find_building(file)
