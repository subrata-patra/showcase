from flask import Flask
from flask import request
import jwt
import csv
import json
import time
from blueprint_movies import movies
from blueprint_comments import comments
from blueprint_category import category

app = Flask(__name__)
app.register_blueprint(movies, url_prefix = '/movies')
app.register_blueprint(comments, url_prefix = '/comments')
app.register_blueprint(category, url_prefix = '/category')

@app.route('/registration', methods = ['POST'])
def user_registration():
    iid = request.json['iid']
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    contact_number = request.json['contact_number']
    address = request.json['address']
    
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['email'] = email
    dict1['password'] = password
    dict1['contact_number'] = contact_number
    dict1['address'] = address
    
   
    with open('data/user.csv', 'a') as file_wrap: 
        headers = dict1.keys()
        csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
        csv_template.writerow(dict1)
    payload = {'name': name, 'message': 'registered', 'expire': time.time()+3600}
    key = 'secret'
    encode_jwt = jwt.encode(payload, key)
    return {'auth_token': encode_jwt.decode(), 'message': 'you have been sucessfully registered'}

### User Login:
@app.route('/login', methods = ['POST'])
def user_login():
    name = request.json['name']
    password = request.json['password']

    with open('data/user.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        flag = False
        for odict in csv_obj:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
                    break
    if flag:
        payload = {'name': name, 'message': 'logged_in', 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 'message': 'you have sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}


### Modify Password:
@app.route('/modify/password', methods = ['PATCH'])
def modify_password():
    name = request.json['name']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/user.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        flag = False
        for odict in csv_obj:
            if odict['name'] == name:
                if odict['password'] == password:
                    odict['password'] = password_mod
                    main_list.append(odict)
                    flag = True
            else:
                main_list.append(odict)

    if flag:
        with open('data/user.csv', 'w') as file_wrap: 
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            csv_template.writerows(main_list)
        return json.dumps({'password': 'modified sucessfully'})
    else:
        return json.dumps({'password mismatch': 'modification failed'})


### Delete User:
@app.route('/delete/user', methods = ['DELETE'])
def delete_user():
    name = request.json['name']
    password = request.json['password']
    flag = False
    with open('data/user.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        for i in csv_obj:
            main_list.append(i)
        for odict in main_list:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
    
    if flag:
        with open('data/user.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['name'] != name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'user details deleted'})
    else:
        return json.dumps({'message': 'username or password incorrect'})

### Show All User Details:
@app.route('/show', methods = ['GET'])
def show_user_details():
    with open('data/user.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        csv_mlist = list(csv_obj)
    return json.dumps({'users': csv_mlist})
