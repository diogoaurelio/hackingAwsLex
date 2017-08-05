# this took all afternoon


import boto3
import json
from datetime import datetime as dt

def dispatcher(current_intent,context_param):
    session_attributes = current_intent['sessionAttributes'] if current_intent['sessionAttributes'] is not None else {}
    temp_dict = {'Name': current_intent.get('currentIntent').get('slots').get('completeName'),
                 'Age': current_intent.get('currentIntent').get('slots').get('age'),
                 'skills': current_intent.get('currentIntent').get('slots').get('skills')
                 }

    closing_message = {
        'contentType': 'PlainText',
        'content': 'Thank you'
    }

    write_to_s3(temp_dict)
    return close(session_attributes,'Fulfilled', closing_message)


def write_to_s3(new_dict):
    s3 = boto3.resource('s3')
    object = s3.Object('hackaton-aug-17', 'test_folder/test'+str(dt.now())+'.json')
    data = json.dumps(new_dict)
    object.put(Body=str(data))


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response