"""
Name: Hiren Shah
Professor: Waithe
Date:10.11.21
Purpose: Program provides a command-line driven interface
that lets a user do online shopping from a selection of
items written to a DynamoDB database. It has 6 options
When the user checks the items out of their shopping cart, 
the items are written to a file in S3. It's like your very own
cached online shopping cart.
"""

import boto3
import time
import dynamo_initialize_table
import dynamo_show_records


def main():
    """
    Main method that generates an interface for the user to 
    execute different filtering
    """

    # initialize to True
    program_running = True

    print('Starting Hirens Online Shopping App...')
    dynamo_initialize_table.initialize()
    counter = 0
    # wait until db is created before adding records
    while dynamo_initialize_table.status() != 'ACTIVE':
        time.sleep(0.5)
        counter += 1
        if counter > 40:  # times out after 20 seconds
            print('Timed Out....')
            print('App initialization taking longer than expected. Program forced to quit.')
            program_running = False
    print('Retrieving database...')
    dynamo_initialize_table.add_items()
    print('Launching program!\n')

    print('******** Welcome You to Hirens Online Shopping Interface ********')

    shopcart = []  # start with empty shopcart
    
    def append_to_cart_challenge(record):
        # ask if user wants to add item to shopcart
        while True:
            print('\nAdd item to shopcart? (y or n)')
            add_shopcart = input('>> ')
            if add_shopcart == 'y':
                shopcart.append(record['ProductID'])
                shopcart.append(record['ProductName'])
                shopcart.append(record['Category'])
                shopcart.append(record['Price'])
                print('*** shopcart UPDATED ***\n')
            elif add_shopcart == 'n':
                pass
            else:
                print('Invalid entry!\n')
                continue
            break
    
    # method that can be called to add to shopping cart in s3
    def add_to_shopcart(shopcart_string):
        s3 = boto3.resource('s3')
        object = s3.Object('shopping-cart-hw4', 'shop-cart-hw4.txt')
        object.put(Body=shopcart_string)

    while program_running:
        print('\nPlease choose from the following options:')
        print('a. View shopping shopcart.')
        print('b. Search for item by ProductName.')
        print('c. Search for item by ProductID.')
        print('d. Browse by Category.')
        print('e. Empty shopping shopcart.')
        print('f. Exit the program.')
        choice = input('>> ')

        # View shopping shopcart
        if choice == 'a':
            print('Hirens shopcart:\n')
            out = ""
            counter = 1
            for i in shopcart:
                out += str(i) + " "
                if counter == 4:
                    print(out + "\n")
                    out = ""
                    counter = 0
                counter += 1

            if not shopcart:  # check out only if the shopcart has household items
                continue
            while True:
                print('\nWould you like to check out? (y or n)')
                checkout = input('>> ')

                if checkout == 'y':
                    shopcart_string = ''
                    counter = 0
                    for item in shopcart:
                        if counter == len(shopcart) - 1: 
                            shopcart_string += item + '\n'
                            counter = 0
                            continue
                        shopcart_string += item + ', '
                        counter += 1

                    add_to_shopcart(shopcart_string)
                    print('Items checked out:')
                    print(shopcart_string)
                elif checkout == 'n':
                    pass
                else:
                    print('Invalid entry!\n')
                    continue
                break

        # Search for item by ProductName
        elif choice == 'b':
            data = dynamo_show_records.show_all()  # get records from DynamoDB table

            search_name = input('Enter a product name: ')
            item_found = False
            for record in data:
                if search_name.lower() == record['ProductName'].lower():
                    print('Found')
                    print('|==========|====================|============|=========|')
                    print('|ProductID |ProductName         |Category    |Price    |')
                    print('|==========|====================|============|=========|')
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                    print('|==========|====================|============|=========|')
                    item_found = True
                    
                    append_to_cart_challenge(record)
                    
            if item_found is False:
                print('Item not found!')

        # Search for item by ProductID
        elif choice == 'c':
            data = dynamo_show_records.show_all()  # get records from DynamoDB table

            search_id = input('Enter a product ID: ')
            item_found = False
            for record in data:
                if search_id == record['ProductID']:
                    print('Found')
                    print('|==========|====================|============|=========|')
                    print('|ProductID |ProductName         |Category    |Price    |')
                    print('|==========|====================|============|=========|')
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                    print('|==========|====================|============|=========|')
                    item_found = True
                    
                    # calls method to ask user if they want to add to 
                    append_to_cart_challenge(record)
                   
            if item_found is False:
                print('Item not found!')

        # Browse by Category
        elif choice == 'd':
            categories = []
            data = dynamo_show_records.show_all()  # get records from DynamoDB table
            for record in data:
                categories.append(record['Category'])
            categories = set(categories)  # cast to set to get only unique category values
            print('Choose from one of the following categories:')
            print(categories)
            print("Type in name of category and press 'Enter'")
            cat_choice = input('>>> ')

            if cat_choice.capitalize() in categories:
                print(f'All products from {cat_choice.capitalize()} category:\n')
                print('|==========|====================|============|=========|')
                print('|ProductID |ProductName         |Category    |Price    |')
                print('|==========|====================|============|=========|')
                for record in data:
                    if cat_choice.capitalize() != record["Category"]:
                        continue
                    # setup variables to create empty space after ProductName text
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                print('|==========|====================|============|=========|')

                # ask if user wants to add item to shopcart
                while True:
                    print('\nAdd item to shopcart? (y or n)')
                    add_shopcart = input('>>> ')
                    if add_shopcart == 'y':
                        item_choice = input('Enter ProductID: ')
                        item_found = False
                        for record in data:
                            if item_choice == record['ProductID']:
                                shopcart.append(record['ProductID'])
                                shopcart.append(record['ProductName'])
                                shopcart.append(record['Category'])
                                shopcart.append(record['Price'])
                                item_found = True
                                print('*** shopcart UPDATED ***\n')
                        if item_found is False:
                            print('Item not found!')
                    elif add_shopcart == 'n':
                        pass
                    else:
                        print('Invalid entry!\n')
                        continue
                    break
            else:
                print('Category NOT found!')

        # Empty shopping shopcart
        elif choice == 'e':
            print('**********************************')
            print('Shopping cart emptied! Next Time!!')
            print('**********************************')
            shopcart = []
            s3 = boto3.resource('s3')
            object = s3.Object('shopping-cart-hw4', 'shop-cart-hw4.txt')
            object.put(Body='')

        # Exit the program
        elif choice == 'f':
            print('\n\n\n\n******** THANK YOU FOR USING Hirens SHOPPING PROGRAM AND HAPPY COLUMBUS DAY! ********')
            program_running = False

        else:
            print('\n\n\n\nInvalid response!')

if __name__ == '__main__':
    main()