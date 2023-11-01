from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class CustomerDao:
    CUSTOMER_COLLECTION = "customer"

    def __init__(self, name=None, phone_no=None, email=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "name": self.name,
            "phoneNo": self.phone_no,
            "email": self.email
        }
        if CustomerDao.id_exist(self.oid):
            self.db[self.CUSTOMER_COLLECTION].replace_one({"oid": self.oid}, document)
        else:    
            self.db[self.CUSTOMER_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_customer_dao = []
        for doc in Databases.NETFLIX.customer.find():
            customer = CustomerDao(oid=doc["oid"])
            customer.name = doc["name"]
            customer.phone_no = doc["phoneNo"]
            customer.email = doc["email"]
            all_customer_dao.append({customer.oid:[customer.name,customer.phone_no,customer.email]})
        return all_customer_dao
    

    def delete(self, oid):
        self.db[self.CUSTOMER_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.genre.find():
            customer = CustomerDao(oid=doc["oid"])
            customer.oid = doc["oid"]
            all_ids.append(customer.oid)
        if oid in all_ids:
            return True
        else:
            return False

    def get_oid(self):
        return self.oid

    def get_name(self):
        return self.name

    def get_phone_no(self):
        return self.phone_no

    def get_email(self):
        return self.email
    
    def set_name(self, name):
        self.name = name

    def set_phone_no(self, phone_no):
        self.phone_no = phone_no

    def set_email(self, email):
        self.email = email
