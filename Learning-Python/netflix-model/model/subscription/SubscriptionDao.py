from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class ESubscriptionType:
    MONTHLY = "MONTHLY"
    ANNUALLY = "ANNUALLY"
    NOT_DEFINED = "NOT_DEFINED"


class EPrice:
    SINGLE_USER = "SINGLE_USER"
    MULTI_USER = "MULTI_USER"
    MULTI_4K = "MULTI_4K"
    NOT_DEFINED = "NOT_DEFINED"


class SubscriptionDao:
    SUBSCRIPTION_COLLECTION = "subscription"

    def __init__(self, sub_type=None, price=None, sub_date=None, sub_expiry=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.sub_type = sub_type or ESubscriptionType.NOT_DEFINED
        self.sub_date = sub_date
        self.sub_expiry = sub_expiry
        self.price = price or EPrice.NOT_DEFINED
        self.db = Databases.NETFLIX

    @staticmethod
    def get_prices():
        enum_to_price = {
            EPrice.SINGLE_USER: 10.99,
            EPrice.MULTI_USER: 12.99,
            EPrice.MULTI_4K: 16.99
        }
        return enum_to_price

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "subscriptionType": self.sub_type,
            "subscriptionDate": self.sub_date,
            "expiryDate": self.sub_expiry,
            "price": self.price
        }
        self.db[self.SUBSCRIPTION_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_subscription_dao = []
        for doc in Databases.NETFLIX.subscription.find():
            sub = SubscriptionDao(oid=doc["oid"])
            sub.type = doc["subscriptionType"]
            sub.date = doc["subscriptionDate"]
            sub.expiry = doc["expiryDate"]
            sub.price = doc["price"]
            all_subscription_dao.append(sub)
        return all_subscription_dao

    def get_oid(self):
        return self.oid

    def get_subscription_type(self):
        return self.sub_type

    def get_subscription_date(self):
        return self.sub_date

    def get_expiry_date(self):
        return self.sub_expiry

    def get_price(self):
        return self.price
