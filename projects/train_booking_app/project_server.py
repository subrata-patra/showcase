from flask import Flask
from flask import request
import json
import csv

app = Flask(__name__)

### User Registration:
@app.route('/users/registration', methods = ['POST'])
def user_registration():
    id = request.json['id']
    username = request.json['username']
    password = request.json['password']
    contact_number = request.json['contact_number']
    address = request.json['address']
    dict1 = {}
    dict1['id'] = id
    dict1['username'] = username
    dict1['password'] = password
    dict1['contact_number'] = contact_number
    dict1['address'] = address

    with open('data/users.csv', 'a') as file_wrap1b: 
        headers1 = dict1.keys()
        csv_template1b = csv.DictWriter(file_wrap1b, fieldnames = headers1)
        csv_template1b.writerow(dict1)

    return json.dumps({'user registration': 'sucessful'})


### User Login:
@app.route('/users/login', methods = ['POST'])
def user_login():
    username = request.json['username']
    password = request.json['password']

    with open('data/users.csv', 'r') as file_wrap2:
        csv_obj = csv.DictReader(file_wrap2)
        csv_mlist = list(csv_obj)
    
    flag = False
    for row in csv_mlist:
        if row['username'] == username:
            if row['password'] == password:
                flag = True
                break
    if flag:
        return json.dumps({'login': 'sucessful'})
    else:
        return json.dumps({'login': 'not sucessful'})

### Modify Password:
@app.route('/users/modify/password', methods = ['PATCH'])
def modify_password():
    username = request.json['username']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/users.csv', 'r') as file_wrap3:
        csv_obj3 = csv.DictReader(file_wrap3)
        csv_mlist3 = []
        for row in csv_obj3:
            if row['username'] == username:
                if row['password'] == password:
                    row['password'] = password_mod
                    return json.dumps({'password': 'modified sucessfully'})
                elif row['password'] != password:
                    return json.dumps({'password mismatch': 'modification failed'}) 
                csv_mlist3.append(row)
            else:
                csv_mlist3.append(row)

    with open('data/users.csv', 'w') as file_wrap3b: 
        headers3 = csv_mlist3[0].keys()
        csv_template3b = csv.DictWriter(file_wrap3b, fieldnames = headers3)
        csv_template3b.writeheader()
        csv_template3b.writerows(csv_mlist3)


### Delete User:
@app.route('/users/delete/user', methods = ['DELETE'])
def delete_user():
    id4 = request.json['id']
    username = request.json['username']
    password = request.json['password']
    with open('data/users.csv', 'r') as file_wrap4:
        csv_obj4 = csv.DictReader(file_wrap4)
        csv_mlist4 = list(csv_obj4)
     
    with open('data/users.csv', 'w') as file_wrap4b:
        headers4 = csv_mlist4[0].keys()
        csv_template4 = csv.DictWriter(file_wrap4b, fieldnames = headers4)
        csv_template4.writeheader()
        for row in csv_mlist4:
            if row['id'] != id4:
                csv_template4.writerow(row)
            else:
                continue
    return json.dumps({'message': 'user details deleted'})


### Show All User Details:
@app.route('/users/show/details', methods = ['GET'])
def show_user_details():
    with open('data/users.csv', 'r') as file_wrap5:
        csv_obj5 = csv.DictReader(file_wrap5)
        csv_mlist5 = list(csv_obj5)
        return json.dumps({'users': csv_mlist5}) 

##**********************************************************
##**********************************************************

### Create Bus Details:
@app.route('/bus/create', methods = ['POST'])
def bus_details_create():
    id = request.json['id']
    bus_number = request.json['bus_number']
    departure_loc = request.json['departure_loc']
    arrival_loc = request.json['arrival_loc']
    journey_duration = request.json['journey_duration']
    fare = request.json['fare']
    username = request.json['username']
    password = request.json['password']
    dict1 = {}
    dict1['id'] = id
    dict1['bus_number'] = bus_number
    dict1['departure_loc'] = departure_loc
    dict1['arrival_loc'] = arrival_loc
    dict1['journey_duration'] = journey_duration
    dict1['fare'] = fare

    with open('data/users.csv', 'r') as file_wrap5:
        csv_obj5 = csv.DictReader(file_wrap5)
        main_list = []
        for i in csv_obj5:
            main_list.append(i)
    
                
    with open('data/buses.csv', 'a') as file_wrap1b: 
        headers1 = dict1.keys()
        csv_template1b = csv.DictWriter(file_wrap1b, fieldnames = headers1)
        for row in main_list:
            if (row['username'] == username) and (row['password'] == password):
                csv_template1b.writerow(dict1)
                return json.dumps({'bus details': 'created'})
            else:
                return json.dumps({'not a valid user': 'bus details not created'})
    

### Get All Bus Details:
@app.route('/bus/show/details', methods = ['GET'])
def show_bus_details():
    with open('data/buses.csv', 'r') as file_wrap5:
        csv_obj5 = csv.DictReader(file_wrap5)
        csv_mlist5 = list(csv_obj5)
        return json.dumps({'buses': csv_mlist5}) 

### Searh for a Bus using Bus Number:
@app.route('/bus/search', methods = ['POST'])
def bus_search():
    bus_number = request.json['bus_number']
    username = request.json['username']
    password = request.json['password']

    with open('data/users.csv', 'r') as file_wrap10:
        csv_obj10 = csv.DictReader(file_wrap10)
        main_list = []
        for i in csv_obj10:
            main_list.append(i)
        
    for row in main_list:
        if (row['username'] == username) and (row['password'] == password):
            with open('data/buses.csv', 'r') as file_wrap5:
                csv_obj5 = csv.DictReader(file_wrap5)
                for dict5 in csv_obj5:
                    if dict5['bus_number'] == bus_number:
                        return json.dumps(dict5)
        else:
            return json.dumps({'not a valid user': 'operation cannot be done'})
    

### Delete a Bus Details:
@app.route('/bus/delete', methods = ['DELETE'])
def bus_delete():
    id4 = request.json['id']
    #username = request.json['username']
    #password = request.json['password']
    with open('data/buses.csv', 'r') as file_wrap4:
        csv_obj4 = csv.DictReader(file_wrap4)
        csv_mlist4 = list(csv_obj4)
     
    with open('data/buses.csv', 'w') as file_wrap4b:
        headers4 = csv_mlist4[0].keys()
        csv_template4 = csv.DictWriter(file_wrap4b, fieldnames = headers4)
        csv_template4.writeheader()
        for row in csv_mlist4:
            if row['id'] != id4:
                csv_template4.writerow(row)
            else:
                continue
    return json.dumps({'message': 'bus details deleted'})

### Modity a Bus Details:
@app.route('/bus/modify', methods = ['PATCH'])
def bus_modify():
    id4 = request.json['id']
    fare_mod = request.json['fare']
    #username = request.json['username']
    #password = request.json['password']
    with open('data/buses.csv', 'r') as file_wrap4:
        csv_obj4 = csv.DictReader(file_wrap4)
        csv_mlist4 = []
        for dict4 in csv_obj4:
            if dict4['id'] == id4:
                dict4['fare'] = fare_mod
                csv_mlist4.append(dict4)
            else:
                csv_mlist4.append(dict4)            
     
    with open('data/buses.csv', 'w') as file_wrap4b:
        headers4 = csv_mlist4[0].keys()
        csv_template4 = csv.DictWriter(file_wrap4b, fieldnames = headers4)
        csv_template4.writeheader()
        for row in csv_mlist4:
            csv_template4.writerow(row)
            
    return json.dumps({'message': 'bus details modified'})


##**********************************************************
##**********************************************************