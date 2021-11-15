"""
Author: Hiren Shah
filename: dynamo_show_records
Purpose: Program uses function to return all
records in a DynamoDB database.
"""


import logging
import boto3
from botocore.exceptions import ClientError



def show_all():
    """
    Function returns all records in database.
    """
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ShoppingItems')

        response = table.scan()

        data = []
        data = response['Items']
        # print(data)

    except ClientError as err:
        logging.error(err)
        return False
    return data