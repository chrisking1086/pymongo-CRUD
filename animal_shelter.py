from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password,hostname, port, db, col):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = hostname
        PORT = port
        DB = database
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# C - Creates a new document in the animals collection
    def create(self, new_animal):
        # verify dict was passed
        if isinstance(new_animal, dict) and new_animal:
            try:
                self.database.animals.insert_one(new_animal)
                return True # Return true if successfully created
            except Exception as e:
                print(f"Insert error: {e}")
                return False # return false if exception was thrown
        else:
            raise ValueError("Invalid data format. Expected a non-empty dictionary")
        
# R - Reads the collection and outups the result
    def read(self, search_data):
        # verify dict was passed
        if not isinstance(search_data, dict):
            raise ValueError("Query must be a dictionary.")
            
        try:
            # return results as a list
            results = list(self.database.animals.find(search_data))
            return results if results else [] # return list or empty list if non were found
        except Exception as e:
            print(f"Query error: {e}") # return empty list if exception was thrown
            return []
        
# U - Updates the document
    def update(self, update_selection, update_filter, update_data):
        # verify int was passed      
        if not isinstance(update_selection, int):
            raise ValueError("Update Selection must be an integer")
            
        # verify dict was passed
        if not isinstance(update_filter,dict) and not isinstance(update_data, dict):
            raise ValueError("Query must be a dictionary.")

        # update one if update_selection is 1
        if update_selection == 1:
            try:
                results = self.database.animals.update_one(update_filter, update_data)
                # filter for no records found
                if results.modified_count == 0:
                    print("No record found")
                    return print("Number of documents updated: ", results.modified_count) # print modified count
                else:
                    return print("Number of documents updated: ", results.modified_count) # print modified count
            except Exception as e:
                print(f"Query error: {e}") # return empty list if exception was thrown
                return []
        # update many if update_selection is not 1
        else:
            try:
                results = self.database.animals.update_many(update_filter, update_data)
                # filter for no records found
                if results.modified_count == 0:
                    print("No record found")
                    return print("Number of documents updated: ", results.modified_count) # print modified count
                else:
                    return print("Number of documents updated: ", results.modified_count) # print modified count
            except Exception as e:
                print(f"Query error: {e}") # return empty list if exception was thrown
                return []
        
# D - Deletes the document 
    def delete(self, deletion_selection, deletion_data): 
        # verify int was passed      
        if not isinstance(deletion_selection, int):
            raise ValueError("Deletion Selection must be an integer")
            
        # verify dict was passed
        if not isinstance(deletion_data, dict):
            raise ValueError("Query must be a dictionary.")
            
        # delete one if deletion_selection is 1
        if deletion_selection == 1:
            try:
                results = self.database.animals.delete_one(deletion_data)
                # filter for no records found
                if results.deleted_count == 0:
                    print("No record found")
                    print("Number of documents deleted: ", results.deleted_count) # print deleted count
                else:
                    print("Number of documents deleted: ", results.deleted_count) # print deleted count
            except Exception as e:
                print(f"Query error: {e}") # return empty list if exception was thrown
                return []
        else:
            try:
                results = self.database.animals.delete_many(deletion_data)
                # filter for no records found
                if results.deleted_count == 0:
                    print("No record found")
                    print("Number of documents deleted: ", results.deleted_count) # print deleted count
                else:
                    print("Number of documents deleted: ", results.deleted_count) # print deleted count
            except Exception as e:
                print(f"Query error: {e}") # return empty list if exception was thrown
                return []