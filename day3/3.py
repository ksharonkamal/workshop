#program to count the values associated in key in a dictionary.
# sample_data = [{'id': 1, 'success' : True, 'name' : 'Lary'},
#                {'id': 2, 'success' : False, 'name' : 'Rabi'},
#                {'id': 3, 'success' : True, 'name' : 'Alex'}]

sample_data = [{'id': 1, 'success' : True,  'name' : 'Lary'},
               {'id': 2, 'success' : False, 'name' : 'Rabi'},
               {'id': 3, 'success' : True,  'name' : 'Alex'}]
cnt = 0

for i in sample_data:
    if i['success'] == True:
        cnt+=1

print("cnt is ",cnt)

