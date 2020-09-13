from flask import Flask
from flask import request
import jwt
import csv
import json
import time
from blueprint_classes import classes
from blueprint_sections import sections

##########    GENERAL NOTES:    ###########
### This file server.py contains ALL STUDENT routes and TEACHER routes.
### CLASSE routes and SECTION routes are in the respective Blueprint files. 
### blueprint_classes.py and blueprint_sections.py.

app = Flask(__name__)
app.register_blueprint(classes, url_prefix = '/classes')
app.register_blueprint(sections, url_prefix = '/sections')

@app.route('/student/registration', methods = ['POST'])
def student_registration():
    iid = request.json['iid']
    name = request.json['name']
    email = request.json['email']
    gender = request.json['gender']
    password = request.json['password']
    contact_number = request.json['contact_number']
    address = request.json['address']
    father_name = request.json['father_name']
    mother_name = request.json['mother_name']
    role = request.json['role']
    
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['email'] = email
    dict1['gender'] = gender
    dict1['password'] = password
    dict1['contact_number'] = contact_number
    dict1['address'] = address
    dict1['father_name'] = father_name
    dict1['mother_name'] = mother_name
    dict1['role'] = role
    
   
    with open('data/students.csv', 'a') as file_wrap: 
        headers = dict1.keys()
        csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
        csv_template.writerow(dict1)
    payload = {'name': name, 'role': role, 'message': 'registered', 'expire': time.time()+3600}
    key = 'secret'
    encode_jwt = jwt.encode(payload, key)
    return {'auth_token': encode_jwt.decode(), 'message': 'you have been sucessfully registered'}

#-----------------------------------------------------------------------------

### Student Login:
@app.route('/student/login', methods = ['POST'])
def student_login():
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']

    with open('data/students.csv', 'r') as file_wrap:
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
        return {'auth_token': encode_jwt.decode(), 'message': 'you have sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}

#-----------------------------------------------------------------------------

### Modify Password (Student):
@app.route('/student/modify/password', methods = ['PATCH'])
def student_modify_password():
    name = request.json['name']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/students.csv', 'r') as file_wrap:
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
        with open('data/students.csv', 'w') as file_wrap: 
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            csv_template.writerows(main_list)
        return json.dumps({'password': 'modified sucessfully'})
    else:
        return json.dumps({'password mismatch': 'modification failed'})


#-----------------------------------------------------------------------------

### Delete Student:
@app.route('/delete/student', methods = ['DELETE'])
def delete_student():
    name = request.json['name']
    password = request.json['password']
    flag = False
    with open('data/students.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        for i in csv_obj:
            main_list.append(i)
        for odict in main_list:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
    
    if flag:
        with open('data/students.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['name'] != name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'student details deleted'})
    else:
        return json.dumps({'message': 'username or password incorrect'})

#-----------------------------------------------------------------------------

### Show All Student Details:
@app.route('/show/students', methods = ['GET'])
def show_student_details():
    with open('data/students.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        csv_mlist = list(csv_obj)
    return json.dumps({'students': csv_mlist})

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


@app.route('/teacher/registration', methods = ['POST'])
def teacher_registration():
    iid = request.json['iid']
    name = request.json['name']
    password = request.json['password']
    subject = request.json['subject']
    years_of_experience = request.json['years_of_experience']
    role = request.json['role']
    
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['password'] = password
    dict1['subject'] = subject
    dict1['years_of_experience'] = years_of_experience
    dict1['role'] = role
    
   
    with open('data/teachers.csv', 'a') as file_wrap: 
        headers = dict1.keys()
        csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
        csv_template.writerow(dict1)
    payload = {'name': name, 'role': role, 'message': 'registered', 'expire': time.time()+3600}
    key = 'secret'
    encode_jwt = jwt.encode(payload, key)
    return {'auth_token': encode_jwt.decode(), 'message': 'you have been sucessfully registered'}

#-----------------------------------------------------------------------------

### Teacher Login:
@app.route('/teacher/login', methods = ['POST'])
def teacher_login():
    name = request.json['name']
    password = request.json['password']
    role = request.json['role']

    with open('data/teachers.csv', 'r') as file_wrap:
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
        return {'auth_token': encode_jwt.decode(), 'message': 'you have sucessfully logged in'}
    else:
        return {'message': 'username or password incorrect'}

#-----------------------------------------------------------------------------

### Modify Password (Teacher):
@app.route('/teacher/modify/password', methods = ['PATCH'])
def teacher_modify_password():
    name = request.json['name']
    password = request.json['password']
    password_mod = request.json['password_mod']

    with open('data/teachers.csv', 'r') as file_wrap:
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
        with open('data/teachers.csv', 'w') as file_wrap: 
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            csv_template.writerows(main_list)
        return json.dumps({'password': 'modified sucessfully'})
    else:
        return json.dumps({'password mismatch': 'modification failed'})


#-----------------------------------------------------------------------------

### Delete Teacher:
@app.route('/delete/teacher', methods = ['DELETE'])
def delete_teacher():
    name = request.json['name']
    password = request.json['password']
    flag = False
    with open('data/teachers.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        main_list = []
        for i in csv_obj:
            main_list.append(i)
        for odict in main_list:
            if odict['name'] == name:
                if odict['password'] == password:
                    flag = True
    
    if flag:
        with open('data/teachers.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['name'] != name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'student details deleted'})
    else:
        return json.dumps({'message': 'username or password incorrect'})

#-----------------------------------------------------------------------------

### Show All Teacher Details:
@app.route('/show/teachers', methods = ['GET'])
def show_teacher_details():
    with open('data/teachers.csv', 'r') as file_wrap:
        csv_obj = csv.DictReader(file_wrap)
        csv_mlist = list(csv_obj)
    return json.dumps({'teachers': csv_mlist})


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


