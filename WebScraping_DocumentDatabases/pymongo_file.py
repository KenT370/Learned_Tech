''' Capturing User Input and storing the data into a MongoDB 
    Database '''

import pymongo
import datetime

# Connecting to MongoDB
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.fruits_db

collection = db.fruits

answer = 'Yes'
while answer.lower() == 'yes':
    
    # Asking the user for their input
    vendor = input('Enter the name of the vendor: ')
    fruit = input('Enter the name of the fruit: ')
    num = int(input('Enter the number of fruits received: '))
    rating = input('Enter the rating for the vendor: ')
    
    # Capturing the current date and time 
    now = datetime.datetime.now()
    date = f'{now.month}/{now.day}/{now.year}'
    time = f'{now.hour}:{now.minute}'
    
    # Inserting the User's Answer's and Date/Time into MongoDB Fruit Database
    db.fruits.insert_one(
        {
            'vendor_name':'place 1',
            'fruit_type':'banana',
            'received':25,
            'rating':2,
            'date': date,
            'time': time
            })
    
    # Asking the user if they would like to enter more information
    answer = input("Would you like to enter another instance (yes/no): ")
    
# Printing all the Data in the DataBase
for val in db.fruits.find():
    print(val)
    print('-'*20))
