from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time

classes = Blueprint('classes', __name__)

@classes.route('/')
def classes_home():
    return "Welcome to *Classes* Home Page!"

### Create Class Details:
@classes.route('/create', methods = ['POST'])
def class_details_create():
    iid = request.json['iid']
    name = request.json['name']
    teacher_name = request.json['teacher_name']
    student_name = request.json['student_name']
    auth_token = request.json['auth_token']
    dict1 = {}
    dict1['iid'] = iid
    dict1['name'] = name
    dict1['teacher_name'] = teacher_name
    dict1['student_name'] = student_name
    
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/classes.csv', 'a') as file_wrap: 
                headers = dict1.keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writerow(dict1)        
            return json.dumps({'message':'class details created'})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})

#-----------------------------------------------------------------------------


### Get All Class Details:
@classes.route('/details', methods = ['POST'])
def show_class_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/classes.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            csv_mlist = list(csv_obj)
        return json.dumps({'classes': csv_mlist}) 
    else:
        return json.dumps({'message':'token invalid'})


#-----------------------------------------------------------------------------

### Search for a Class using Teacher Name:
@classes.route('/search/teacher', methods = ['POST'])
def class_search_teacher():
    teacher_name = request.json['teacher_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/classes.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['teacher_name'] == teacher_name: 
                    return json.dumps({'class details': odict})
    else: 
        return json.dumps({'message':'token invalid'})

#-----------------------------------------------------------------------------

### Search for a Class using Student Name:
@classes.route('/search/student', methods = ['POST'])
def class_search_student():
    student_name = request.json['student_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/classes.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['student_name'] == student_name: 
                    return json.dumps({'class details': odict})
    else: 
        return json.dumps({'message':'token invalid'})

#-----------------------------------------------------------------------------


### Delete a Class Details:
@classes.route('/delete', methods = ['DELETE'])
def class_delete():
    name = request.json['name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/classes.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for i in csv_obj:
                    main_list.append(i)
     
            with open('data/classes.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writeheader()
                for odict in main_list:
                    if odict['name'] != name:
                        csv_template.writerow(odict)
            return json.dumps({'message': 'class details deleted'})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})


#-----------------------------------------------------------------------------


### Modity a Class Details:
@classes.route('/modify_class', methods = ['PATCH'])
def class_modify_teacher():
    name = request.json['name']
    teacher_name_mod = request.json['teacher_name_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/classes.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for odict in csv_obj:
                    if odict['name'] == name:
                        odict['teacher_name'] = teacher_name_mod
                        main_list.append(odict)
                    else:
                        main_list.append(odict)
                         
            with open('data/classes.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writeheader()
                for row in main_list:
                    csv_template.writerow(row)
            
            return json.dumps({'message': 'class teacher modified'})
        else:
            return json.dumps({'message':'invalid token'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


