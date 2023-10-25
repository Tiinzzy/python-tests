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
        self.db[self.CUSTOMER_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_customer_dao = []
        for doc in Databases.NETFLIX.customer.find():
            customer = CustomerDao(oid=doc["oid"])
            customer.name = doc["name"]
            customer.phone_no = doc["phoneNo"]
            customer.email = doc["email"]
            all_customer_dao.append(customer)
        return all_customer_dao

    def get_oid(self):
        return self.oid

    def get_name(self):
        return self.name

    def get_phone_no(self):
        return self.phone_no

    def get_email(self):
        return self.email
