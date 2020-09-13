from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time


properties = Blueprint('properties', __name__)


@properties.route('/')
def properties_home():
    return "Welcome to *Properties* Home Page!"


# Create Property Details: Only Owner or Admin can add a property
@properties.route('/create', methods = ['POST'])
def properties_details_create():
    iid = request.json['iid']
    sqft = request.json['sqft']
    bedrooms = request.json['bedrooms']
    amenities = request.json['amenities']
    furnishing = request.json['furnishing']
    locality = request.json['locality']
    owner_name = request.json['owner_name']
    owner_id = request.json['owner_id']
    auth_token = request.json['auth_token']

    if isinstance(iid, (str, bool)):
        raise TypeError('Give int type in JSON')

    dict1 = {}
    dict1['iid'] = iid
    dict1['sqft'] = sqft
    dict1['bedrooms'] = bedrooms
    dict1['amenities'] = amenities
    dict1['furnishing'] = furnishing
    dict1['locality'] = locality
    dict1['owner_name'] = owner_name
    dict1['owner_id'] = owner_id
    
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin' or data['role'] == 'owner':
        if data['expire'] >= time.time():
            try:
                with open('data/properties.csv', 'a') as file_wrap: 
                    headers = dict1.keys()
                    csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                    csv_template.writerow(dict1)        
                return json.dumps({'message':'properties details created'})
            except FileNotFoundError as err:
                print(err)
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin or owner'})


# -------------------------------------


# Get All Properties Details: Only Admin can access
@properties.route('/details', methods = ['POST'])
def show_properties_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['role'] == 'admin':
        if data['expire'] >= time.time():
            with open('data/properties.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                csv_mlist = list(csv_obj)
            return json.dumps({'properties': csv_mlist}) 
        else:
            return json.dumps({'message':'token invalid'})
    else:
        return json.dumps({'message':'not an admin'})


# -------------------------------------


# Search for Properties by Locality: User or Owner or Admin can access
@properties.route('/search/locality', methods = ['POST'])
def properties_search_locality():
    locality = request.json['locality']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/properties.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            properties_locality = []
            for odict in csv_obj:
                if odict['locality'] == locality: 
                    properties_locality.append(odict)
            return json.dumps({'properties by locality': properties_locality})
    else: 
        return json.dumps({'message':'token invalid'})


# -------------------------------------


# Search for Properties by Bedrooms: User or Owner or Admin can access 
@properties.route('/search/bedrooms', methods = ['POST'])
def properties_search_bedrooms():
    bedrooms = request.json['bedrooms']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/properties.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            properties_bedrooms = []
            for odict in csv_obj:
                if odict['bedrooms'] == bedrooms:
                    properties_bedrooms.append(odict)
            return json.dumps({'properties by bedrooms': properties_bedrooms})
    else: 
        return json.dumps({'message':'token invalid'})


# -------------------------------------


# Delete a Property: Only Admin or Valid Owner can access
@properties.route('/delete', methods=['DELETE'])
def property_delete():
    iid = request.json['iid']       # propety id
    auth_token = request.headers.get['auth_token']
    key = 'secret'
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'

    if data['expire'] >= time.time(): 
        try:
            flag = False
            with open('data/properties.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for i in csv_obj:
                    main_list.append(i)
                for odict in main_list:
                    if odict['iid'] == iid:
                        if odict['owner_id'] == data['owner_pri_id']:
                            flag = True
                            break
        except FileNotFoundError as err:
            print(err)

        if data['role'] == 'admin' or flag == True:
            with open('data/properties.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames=headers)
                csv_template.writeheader()
                for odict in main_list:
                    if odict['iid'] != iid:
                        csv_template.writerow(odict)
            return json.dumps({'message': 'property deleted'})
        else:
            return json.dumps({'message':'not valid owner or admin'})
    else:
        return json.dumps({'message':'timeout, login again'})


# -------------------------------------


# Modity a Property: Only Admin or Owner can access
@properties.route('/modify_properties', methods = ['PATCH'])
def property_modify_furnishing():
    iid = request.json['iid']
    furnishing_mod = request.json['furnishing_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['role'] == 'admin' or data['role'] == 'owner':
        if data['expire'] >= time.time():
            with open('data/properties.csv', 'r') as file_wrap:
                csv_obj = csv.DictReader(file_wrap)
                main_list = []
                for odict in csv_obj:
                    if odict['iid'] == iid:
                        odict['furnishing'] = furnishing_mod
                        main_list.append(odict)
                    else:
                        main_list.append(odict)
                         
            with open('data/properties.csv', 'w') as file_wrap:
                headers = main_list[0].keys()
                csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
                csv_template.writeheader()
                for row in main_list:
                    csv_template.writerow(row)
            
            return json.dumps({'message': 'property furnishing modified'})
        else:
            return json.dumps({'message':'invalid token'})
    else:
        return json.dumps({'message':'not an admin or owner'})


# ----------------End of File---------------
# ------------------------------------------
