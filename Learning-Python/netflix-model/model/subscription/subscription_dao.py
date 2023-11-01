from utility.Databases import Databases
from utility.OidGenerator import OidGenerator
from enum import Enum


class ESubscriptionType(Enum):
    MONTHLY = "MONTHLY"
    ANNUALLY = "ANNUALLY"
    NOT_DEFINED = "NOT_DEFINED"


class EPrice(Enum):
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
    def get_prices(e_price=EPrice.NOT_DEFINED):
        enum_to_price = {
            EPrice.SINGLE_USER: 10.99,
            EPrice.MULTI_USER: 12.99,
            EPrice.MULTI_4K: 16.99
        }
        return enum_to_price if e_price == EPrice.NOT_DEFINED else enum_to_price[e_price]

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "subscriptionType": self.sub_type,
            "subscriptionDate": self.sub_date,
            "expiryDate": self.sub_expiry,
            "price": self.price
        }
        if SubscriptionDao.id_exist(self.oid):
            self.db[self.SUBSCRIPTION_COLLECTION].replace_one({"oid": self.oid}, document)
        else:
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
            all_subscription_dao.append({sub.oid: [sub.type, sub.date, sub.expiry, sub.price]})
        return all_subscription_dao

    def delete(self, oid):
        self.db[self.SUBSCRIPTION_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.genre.find():
            movie = SubscriptionDao(oid=doc["oid"])
            movie.oid = doc["oid"]
            all_ids.append(movie.oid)
        if oid in all_ids:
            return True
        else:
            return False

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

    def set_subscription_type(self, sub_type):
        self.sub_type = sub_type

    def set_subscription_date(self, sub_date):
        self.sub_date = sub_date

    def set_expiry_date(self, sub_expiry):
        self.sub_expiry = sub_expiry

    def set_price(self, price):
        self.price = price
