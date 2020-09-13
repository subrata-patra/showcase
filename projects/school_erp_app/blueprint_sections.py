from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time

sections = Blueprint('sections', __name__)

@sections.route('/')
def sections_home():
    return "Welcome to *Sections* Home Page!"

### Create Section Details:
@sections.route('/create', methods = ['POST'])
def section_details_create():
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
            with open('data/sections.csv', 'a') as file_wrap: 
                headers = dict1.keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writerow(dict1)        
            return json.dumps({'message':'section details created'})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})

#-----------------------------------------------------------------------------


### Get All Section Details:
@sections.route('/details', methods = ['POST'])
def show_section_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/sections.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            csv_mlist = list(csv_obj)
        return json.dumps({'sections': csv_mlist}) 
    else:
        return json.dumps({'message':'token invalid'})


#-----------------------------------------------------------------------------

### Search for a Section using Teacher Name:
@sections.route('/search/teacher', methods = ['POST'])
def section_search_teacher():
    teacher_name = request.json['teacher_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/sections.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['teacher_name'] == teacher_name: 
                    return json.dumps({'section details': odict})
    else: 
        return json.dumps({'message':'token invalid'})

#-----------------------------------------------------------------------------

### Search for a Section using Student Name:
@sections.route('/search/student', methods = ['POST'])
def section_search_student():
    student_name = request.json['student_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/sections.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['student_name'] == student_name: 
                    return json.dumps({'section details': odict})
    else: 
        return json.dumps({'message':'token invalid'})

#-----------------------------------------------------------------------------


### Delete a Section Details:
@sections.route('/delete', methods = ['DELETE'])
def section_delete():
    name = request.json['name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/sections.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for i in csv_obj:
                    main_list.append(i)
     
            with open('data/sections.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writeheader()
                for odict in main_list:
                    if odict['name'] != name:
                        csv_template.writerow(odict)
            return json.dumps({'message': 'section details deleted'})
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})


#-----------------------------------------------------------------------------


### Modity a Section Details:
@sections.route('/modify_section', methods = ['PATCH'])
def section_modify_teacher():
    name = request.json['name']
    teacher_name_mod = request.json['teacher_name_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/sections.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for odict in csv_obj:
                    if odict['name'] == name:
                        odict['teacher_name'] = teacher_name_mod
                        main_list.append(odict)
                    else:
                        main_list.append(odict)
                         
            with open('data/sections.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writeheader()
                for row in main_list:
                    csv_template.writerow(row)
            
            return json.dumps({'message': 'section teacher modified'})
        else:
            return json.dumps({'message':'invalid token'})
    else:
        return json.dumps({'message':'not an admin (teacher)'})

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


