import json

data = open('data.json').read()

messages = json.loads(data)

users = []
time_message = 0

#Allocating users
for message in messages:
    if message['user'] not in users:
        users.append(message['user'])
        locals()['user_%s' %message['user']] = []

#Separating messages by user
for message in messages:
    for user in users:
        if user == message['user']:
            locals()['user_%s' %user].append(message)

#Agrouping messages by difference of minutes
for user in users:
    locals()['messages_%s' %user] = {}
    time_last_message = 0
    for message in locals()['user_%s' %user]:
        time_message = (float(message['ts']))/60
        difference = time_message - time_last_message
        if difference > 2:
            locals()['messages_%s' %user][time_message] = []
            locals()['messages_%s' %user][time_message].append(message)
            time_last_message = time_message
        else:
            locals()['messages_%s' %user][time_last_message].append(message)

#Exporting files of each user containing messages agrouped by difference of minutes
for user in users:
    with open('%s.json' %user, 'w') as fl:
        json.dump(locals()['messages_%s' %user], fl, indent=4)
