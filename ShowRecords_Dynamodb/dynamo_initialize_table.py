"""
Author: Hiren Shah
Filename: dynamo_initialize_table.py
Purpose: Program uses functions to create a DynamoDB
database, enter records into the database, and
check the status of the database.
"""


import logging
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def initialize():
    """
    Function initializes database.
    """
    try:
        table = dynamodb.create_table(
            TableName='ShoppingItems',
                KeySchema=[
                    {
                    'AttributeName': 'ProductID',
                    'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                    'AttributeName': 'ProductID',
                    'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
        )
    except ClientError:
        return False
    return table


def add_items():
    """
    This function adds items to the database
    """

    try:
        table = dynamodb.Table('ShoppingItems')
        # Table attributes:
        # ProductID (String) – Serves as the Hash Key. (e.g. 43001)
        # ProductName (String) – (e.g. Toothpaste)
        # Category (String) – (e.g. Bathroom)
        # Price (Number) - (e.g. 19.99)
        items_array = [['67655','Hot Dogs', 'Food', '8.00'],
            ['34565','Toothpaste', 'Bathroom', '7.99'],
            ['75463','Controller', 'Electronics', '45.99'],
            ['23156','Kale', 'Food', '4.99'],
            ['02455','Sneakers, mens', 'Footwear', '99.99'],
            ['09878','DSLR camera', 'Electronics', '1458.00'],
            ['21234','Canned soup', 'Food', '.99'],
            ['12353','Shampoo', 'Bathroom', '6.99'],
            ['45675','IPhone', 'Electronics', '999.00'],
            ['12564','Toothpaste', 'Bathroom', '9.99'],
            ['78689','PS5', 'Electronics', '479.99'],
            ['32454','Socks, white', 'Footwear', '4.99'],
            ['15365','Dog food', 'Pets', '2.99'],
            ['19583','Tent', 'Camping', '149.99'],
            ['23423','Polo, mens', 'Clothing', '30.00'],
            ['17445','Skirt, womens', 'Clothing', '89.75'],
            ['44545','Jacket', 'Clothing', '89.50'],
            ['23435','Tortilla chips', 'Food', '5.75'],
            ['67567','Lighter', 'Other', '5.99'],
            ['33435','Patio chair', 'Outdoor', '14.75'],
            ['26465','Plush toy', 'Kids', '90.0'],
            ['89765','Patio umbrella', 'Outdoor', '124.00'],
            ['03435','Electric toothbrush', 'Bathroom', '150.00'],
            ['23467','Shower head', 'Bathroom', '88.99'],
            ['73945','Sponge', 'Kitchen', '43.00'],
            ['24883','Knife', 'Kitchen', '7.00'],
            ['19835','Spatula', 'Kitchen', '8.99'],
            ['39576','Xbox', 'Electronics', '245.99'],
            ['29456','Oven', 'Kitchen', '457.98'],
            ['44667','Lights', 'Outdoor', '25.75'],
            ['12334','Flip flops', 'Footwear', '25.99'],
            ['54889','Scarf', 'Clothing', '19.99'],
            ['99876','desk', 'Office', '548.00'],
            ['36445','Dumbells', 'Fitness', '40.00']]

        for item in items_array:
            pid = item[0]
            pnm = item[1]
            cat = item[2]
            prc = item[3]

            table.put_item(
                Item={
                    'ProductID': pid,
                    'ProductName': pnm,
                    'Category': cat,
                    'Price': prc
                }
        )
    except ClientError as err:
        logging.error(err)
        return False
    return True


def status():
    """
    Function checks status of database to see if it exists.
    """
    table = dynamodb.Table('ShoppingItems')
    return table.table_status