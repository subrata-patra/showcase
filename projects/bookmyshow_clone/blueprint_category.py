from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time

category = Blueprint('category', __name__)

@category.route('/')
def category_home():
    return "Welcome to *Category* Home Page!"

### Create Category Details:
@category.route('/create', methods = ['POST'])
def category_details_create():
    iid = request.json['iid']
    category_name = request.json['category_name']
    auth_token = request.json['auth_token']
    dict1 = {}
    dict1['iid'] = iid
    dict1['category_name'] = category_name
   
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/category.csv', 'a') as file_wrap: 
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)        
        return json.dumps({'message':'category created'})
    else:
         return json.dumps({'message':'token invalid'})


### Get All Category Details:
@category.route('/details', methods = ['POST'])
def show_category_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/category.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            csv_mlist = list(csv_obj)
        return json.dumps({'categories': csv_mlist}) 
    else:
        return json.dumps({'message':'token invalid'})

### Searh for a Category by Category Name:
@category.route('/search', methods = ['POST'])
def category_search():
    category_name = request.json['category_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/category.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['category_name'] == category_name: 
                    return json.dumps({'category details': odict})
    else: 
        return json.dumps({'message':'token invalid'})
              
### Delete a Category Details:
@category.route('/delete', methods = ['DELETE'])
def category_delete():
    iid = request.json['iid']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/category.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for i in csv_obj:
                main_list.append(i)
     
        with open('data/category.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['iid'] != iid:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'category details deleted'})
    else:
        return json.dumps({'message':'token invalid'})
   

### Modity a Category Details:
@category.route('/modify_category', methods = ['PATCH'])
def category_modify():
    iid = request.json['iid']
    category_name_mod = request.json['category_name_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/category.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for odict in csv_obj:
                if odict['iid'] == iid:
                    odict['category_name'] = category_name_mod
                    main_list.append(odict)
                else:
                    main_list.append(odict)
                         
        with open('data/category.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for row in main_list:
                csv_template.writerow(row)
            
        return json.dumps({'message': 'category modified'})
    else:
        return json.dumps({'message':'invalid token'})
    