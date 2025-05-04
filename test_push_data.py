
from pymongo.mongo_client import MongoClient

# update your own password
uri = "mongodb+srv://ladiashrith:<password>@cluster0.mcmgb2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)