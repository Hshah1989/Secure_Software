"""
Name: Hiren Shah
Class: SDEV 400
Date: 9/10/21
Purpose: Initializes database and creates Courses table and has a function to search 
by subject and catalognumber
"""

import logging
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
dynamodb = boto3.resource('dynamodb')


def initialize():
    """
    Function initializes database.
    """
    try:
        table = dynamodb.create_table(
            TableName='Courses',
                KeySchema=[
                    {
                    'AttributeName': 'CourseID',
                    'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                    'AttributeName': 'CourseID',
                    'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
        )
    except ClientError as err:
        logging.error(err)
        return False
    return table


def add_items(arrayofCourses):
    """
    Adds records to the database
    """
    try:
        table = dynamodb.Table('Courses')
        

        for item in arrayofCourses:
            courseId = item[0]
            subject = item[1]
            courseNum = item[2]
            title = item[3]
            numCredits = item[4]

            table.put_item(
                Item={
                    'CourseID': courseId,
                    'Subject': subject,
                    'CatalogNbr': courseNum,
                    'Title': title,
                    'NumCredits': numCredits
                }
        )
    except ClientError as err:
        logging.error(err)
        return False
    return True

def search(subject, cat_num):
    """
    Function lets user search DynamoDB database.
    Takes in 2 arguments: subject, and cat_num.
    """
    try:
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('Courses')


        response = table.scan(
            FilterExpression=Attr('Subject').eq(subject)
        )
        items = response['Items']
        # print(items)
    except ClientError as err:
        logging.error(err)
        raise ClientError()
    return items

def status():
    """
    Function checks status of database to see if it exists.
    """
    table = dynamodb.Table('Courses')
    return table.table_status
