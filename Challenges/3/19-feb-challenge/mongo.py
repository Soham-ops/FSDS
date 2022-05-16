import pymongo
import csv
import logging as lg
import os

class Dbase:

    def __init__(self):

        try:
            #if log file exists continue writing
            if os.path.exists('mongo_database.log'):
                f = open('mongo_database.log','a')

                f.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                f.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                f.write('------------NEW OBJECT CREATED------------------\n')
                f.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                f.write("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

                f.close()

            #init log file
            lg.basicConfig(filename= 'mongo_database.log',level = lg.DEBUG,format = "%(asctime)s - %(message)s",
                               datefmt='%d/%m/%Y %I:%M:%S %p')

            print('Log file Created Successfully')

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))


    def initConnection(self,username,password):

        try:
            self.client_cloud = pymongo.MongoClient('soemthing from how to run .txt goes here')
            lg.info("Connection established")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def createDB(self,db_name):

        try:
            self.db = self.client_cloud['sample']
            lg.info("DB Created")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def createCollection(self,cname):

        try:
            self.collection_name = self.db[cname]
            lg.info('Collection created')

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()


    def read_csv_to_db(self):
        try:

            with open('carbon_nanotubes.csv', newline='') as csvfile:
                filereader = csv.reader(csvfile, delimiter=';')
                #skip the col names from being read
                next(filereader)
                #read 5 rows only
                cnt = 1
                for record in filereader:
                    #sample insert
                    # if cnt == 6:
                    #     break

                    self.insert_record(record,cnt)
                    cnt += 1

                lg.info(f"{cnt} records from file successfully inserted")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def insert_record(self,record,cnt):
        try:
            #define structure of the mongo document
            document = {
                '_id': -1,
                'Chiral indice n': '',
                'Chiral indice m': '',
                'Initial atomic coordinate u': '',
                'Initial atomic coordinate v': '',
                'Initial atomic coordinate w': '',
                'Calculated atomic coordinates u': '',
                'Calculated atomic coordinates v': '',
                'Calculated atomic coordinates w': ''
            }

            # load info
            document['_id'] = cnt
            document['Chiral indice n'] = record[0]
            document['Chiral indice m'] = record[1]
            document['Initial atomic coordinate u'] = record[2]
            document['Initial atomic coordinate v'] = record[3]
            document['Initial atomic coordinate w'] = record[4]
            document['Calculated atomic coordinates u'] = record[5]
            document['Calculated atomic coordinates v'] = record[6]
            document['Calculated atomic coordinates w'] = record[7]

            # print info
            #print(document)

            #insert into db
            inserted_record = self.collection_name.insert_one(document)
            lg.info(f"record {inserted_record.inserted_id} inserted ")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def update_record(self,db,cname,rno):
        try:

            updated_record = self.client_cloud[db][cname].update_one({"_id":rno},
                                                             {"$set":{"Chiral indice n":"some dummy value"}})
            lg.info(f"{updated_record.modified_count} records updated")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def delete_record(self,db,cname,condition):
        try:
            deleted_record = self.client_cloud[db][cname].delete_one(condition)
            lg.info(f"{deleted_record.deleted_count} records deleted")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    #find and filter question are clubbed together inside find_record
    def find_record(self,db,cname,condition):
        try:
            lg.info(f'finc condition being{condition} below records were found')
            for record in self.client_cloud[db][cname].find(condition):
                lg.info(record)
        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()



    def delete_collection(self,db,cname):
        try:
            self.client_cloud[db][cname].drop()
            lg.info("Collection Dropped")

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def delete_db(self,db):
        try:
            self.client_cloud.drop_database(db)
            lg.info('Database Dropped')
        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

    def close_connection(self):
        try:
            print('Program Run Success')
            self.client_cloud.close()
            lg.info('Connection Closed')

        except Exception as e:
            print(f"Something went wrong -> {e}")
            lg.exception(str(e))
            self.client_cloud.close()

obj = Dbase()

obj.initConnection('soemthing from how to run .txt goes here')

#Create and insert records
# obj.createDB('sample')
# obj.createCollection('carbon-nanotubes')
# obj.read_csv_to_db()

#update records
#obj.update_record('sample','carbon-nanotubes',20)

#delete records
# condition_for_deleting = {"Chiral indice n":"some dummy value"}
# obj.delete_record('sample','carbon-nanotubes',condition_for_deleting)

#find record
# find_condition = {"_id":{"$lte":3}}
# obj.find_record('sample','carbon-nanotubes',find_condition)

#Delete collection and DB (use only one)
# obj.delete_collection('sample','carbon_nanotubes')
# obj.delete_db('sample')

#release resources
obj.close_connection()