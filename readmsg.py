ListofMessages = conn.receive_message(Queue, 10)
print(len(ListofMessages))
for message in ListofMessages:
	print(message.get_body())	
