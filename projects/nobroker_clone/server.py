from flask import Flask
from flask import request
import jwt
import csv
import json
import time
from blueprint_properties import properties


app = Flask(__name__)
app.register_blueprint(properties, url_prefix='/properties')


# Admin, Owner, and User routes are here (server.py)
# Property routes are in blueprint_properties.py

# Admin Registration: 
@app.route('/admin/registration', methods=['POST'])
def admin_registration():
    iid = request.json['iid']
    name = request.json['name']
    mobile = request.json['mobile']
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']

    if isinstance(iid, (str, bool)):
        raise TypeError('Give int type in JSON')

    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['mobile'] = mobile
    dict1['email'] = email
    dict1['password'] = password
    dict1['role'] = role

    try:
        with open('data/admin.csv', 'a') as file_wrap:
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)
        payload = {'name': name, 'role': role, 'message': 'registered',
                 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(),
                'message': 'sucessfully registered'}
    except FileNotFoundError as err:
        print(err)


# ------------------------------------------


# Admin Login: 
@app.route('/admin/login', methods = ['POST'])
def admin_login():
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']

    with open('data/admin.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        flag = False
        for odict in csv_obj:
            if odict['name'] == name:
                if odict['password'] == password:
                    if odict['role'] == role:
                        flag = True
                        break
    if flag:
        payload = {'name': name, 'password': password, 'role': role,
                 'message': 'logged_in', 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 
               'message': 'sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}


# ------------------------------------------


# Modify Password (Admin): Only Admin can access
@app.route('/admin/modify/password', methods = ['PATCH'])
def admin_modify_password():
    name = request.json['name']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/admin.csv', 'r') as file_wrap:
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
        with open('data/admin.csv', 'w') as file_wrap: 
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            csv_template.writerows(main_list)
        return json.dumps({'password': 'modified sucessfully'})
    else:
        return json.dumps({'password mismatch': 'modification failed'})


# ------------------------------------------


# Delete Admin: Only Admin can access
@app.route('/delete/admin', methods = ['DELETE'])
def delete_admin():
    name = request.json['name']
    password = request.json['password']
    flag = False
    with open('data/admin.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        for i in csv_obj:
            main_list.append(i)
        for odict in main_list:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
    
    if flag:
        with open('data/admin.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['name'] != name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'admin details deleted'})
    else:
        return json.dumps({'message': 'username or password incorrect'})


# ------------------------------------------


# Show All Admins Details: Only Admin can access
@app.route('/show/admins', methods = ['POST'])
def show_admin_details():
    auth_token = request.json['auth_token']     # Only admin access 
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/admin.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                csv_mlist = list(csv_obj)
            return json.dumps({'admins': csv_mlist})
        else:
            return json.dumps({'message': 'token invalid'})
    else:
        return json.dumps({'message': 'not an admin'})


# ------------------------------------------
# ------------------------------------------


# Owner Registration
@app.route('/owner/registration', methods = ['POST'])
def owner_registration():
    iid = request.json['iid']
    name = request.json['name']
    mobile = request.json['mobile']
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']

    if isinstance(iid, (str, bool)):
        raise TypeError('Give int type in JSON')
    
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['mobile'] = mobile
    dict1['email'] = email
    dict1['password'] = password
    dict1['role'] = role
    
    try:
        with open('data/owner.csv', 'a') as file_wrap: 
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)
        payload = {'name': name, 'role': role, 'message': 'registered', 
                 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 
                'message': 'sucessfully registered'}
    except FileNotFoundError as err:
        print(err)


# ------------------------------------------


# Owner Login:
@app.route('/owner/login', methods = ['POST'])
def owner_login():
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']

    with open('data/owner.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        flag = False
        for odict in csv_obj:
            if odict['name'] == name:
                if odict['password'] == password:
                    if odict['role'] == role:
                        flag = True
                        owner_pri_id = odict['iid']
                        break
    if flag:
        payload = {'name': name, 'role': role, 'owner_pri_id': owner_pri_id, 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 'message': 'sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}


# ------------------------------------------


# Modify Password (Owner):
@app.route('/owner/modify/password', methods = ['PATCH'])
def owner_modify_password():
    name = request.json['name']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/owner.csv', 'r') as file_wrap:
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
        with open('data/owner.csv', 'w') as file_wrap: 
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            csv_template.writerows(main_list)
        return json.dumps({'password': 'modified sucessfully'})
    else:
        return json.dumps({'password mismatch': 'modification failed'})


# ------------------------------------------


# Delete Owner:
@app.route('/delete/owner', methods = ['DELETE'])
def delete_owner():
    name = request.json['name']
    password = request.json['password']
    flag = False
    with open('data/owner.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        for i in csv_obj:
            main_list.append(i)
        for odict in main_list:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
    
    if flag:
        with open('data/owner.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['name'] != name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'owner details deleted'})
    else:
        return json.dumps({'message': 'username or password incorrect'})


# ------------------------------------------


# Show All Owners Details: Only Admin can access
@app.route('/show/owners', methods = ['POST'])
def show_owner_details():
    auth_token = request.json['auth_token']     # Only admin access 
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/owner.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                csv_mlist = list(csv_obj)
            return json.dumps({'owners': csv_mlist})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin'})


# ------------------------------------------
# ------------------------------------------


# User Registration
@app.route('/user/registration', methods = ['POST'])
def user_registration():
    iid = request.json['iid']
    name = request.json['name']
    mobile = request.json['mobile']
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']

    if isinstance(iid, (str, bool)):
        raise TypeError('Give int type in JSON')
    
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['mobile'] = mobile
    dict1['email'] = email
    dict1['password'] = password
    dict1['role'] = role
    
    try:
        with open('data/user.csv', 'a') as file_wrap: 
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)
        payload = {'name': name, 'role': role, 'message': 'registered', 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 'message': 'sucessfully registered'}
    except FileNotFoundError as err:
        print(err)


# ------------------------------------------


# User Login:
@app.route('/user/login', methods = ['POST'])
def user_login():
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']

    with open('data/user.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        flag = False
        for odict in csv_obj:
            if odict['name'] == name:
                if odict['password'] == password:
                    if odict['role'] == role:
                        flag = True
                        break
    if flag:
        payload = {'name': name, 'role': role, 'message': 'logged_in', 'expire': time.time()+3600}
        key = 'secret'
        encode_jwt = jwt.encode(payload, key)
        return {'auth_token': encode_jwt.decode(), 'message': 'sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}


# ------------------------------------------


# Modify Password (User):
@app.route('/user/modify/password', methods = ['PATCH'])
def user_modify_password():
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


# ------------------------------------------


# Delete User:
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


# ------------------------------------------


# Show All Users Details: Only Admin can access
@app.route('/show/users', methods = ['POST'])
def show_user_details():
    auth_token = request.json['auth_token']     # Only admin access 
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/user.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                csv_mlist = list(csv_obj)
            return json.dumps({'users': csv_mlist})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin'})


# ----------------End of File---------------
# ------------------------------------------
