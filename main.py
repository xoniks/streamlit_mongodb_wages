import pymongo
from pymongo import MongoClient
import toml

secrets = toml.load('secrets.toml')

uri = secrets['mongodb']['connection_string']

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.get_database('all_wages')

wages_collection = db.wages

def calculate_wage( hours, rate):
    return hours * rate

def save_wage(name, hours, rate):
    wage = calculate_wage(hours, rate)
    wage_data = {
        'name':name,
        'time':hours,
        'rate':rate,
        'wage':wage
    }
    wages_collection.insert_one(wage_data)



name = 'Egezon'
hours = 10
rate = 20
save_wage(name,hours,rate)
print('Data saved to db.')