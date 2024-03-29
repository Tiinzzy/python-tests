import time

from model.customer.customer_dao import CustomerDao
from model.genre.genre_dao import GenreDao
from model.movies.movies_dao import MoviesDao
from model.subscription.subscription_dao import SubscriptionDao, EPrice, ESubscriptionType


def test_genre():
    genres = GenreDao.load_all()
    for genre in genres:
        print(f"{genre.get_oid()} - {genre.get_description()}")
    g = GenreDao(2)
    print(g.get_description())


def test_customer():
    customers = CustomerDao.load_all()
    for customer in customers:
        print(
            f"Oid: {customer.get_oid()}, Name: {customer.get_name()}, PhoneNo: {customer.get_phone_no()}, Email: {customer.get_email()}")
    cs = CustomerDao(3)
    print(f"\nOid: {cs.get_oid()}, Name: {cs.get_name()}, PhoneNo: {cs.get_phone_no()}, Email: {cs.get_email()}")


def test_movie():
    movies = MoviesDao.load_all()
    for m in movies:
        print(
            f"Oid: {m.get_oid()}, Title: {m.get_title()}, Release Date: {m.get_release_date()}, Rating: {m.get_rating()}")
    cs = CustomerDao(6)
    print(f"Oid: {m.get_oid()}, Title: {m.get_title()}, Release Date: {m.get_release_date()}, Rating: {m.get_rating()}")


def test_subscription():
    # sdo = SubscriptionDao(ESubscriptionType.ANNUALLY, EPrice.MULTI_4K, "2022-11-11", "2023-11-11")
    # sdo.save_to_table()

    subscriptions = SubscriptionDao.load_all()
    for sd in subscriptions:
        print(
            f"Oid: {sd.get_oid()}, Type: {sd.get_subscription_type()}, Price: {sd.get_price()}, Start Date: {sd.get_subscription_date()}, End Date: {sd.get_expiry_date()}")

    sd = SubscriptionDao(2)
    print(
        f"Oid: {sd.get_oid()}, Type: {sd.get_subscription_type()}, Price: {sd.get_price()}, Start Date: {sd.get_subscription_date()}, End Date: {sd.get_expiry_date()}")


if __name__ == "__main__":
    # test_genre()
    #
    # print()
    # test_customer()
    #
    # print()
    # test_movie()
    #
    # print()
    # test_subscription()

    sd = SubscriptionDao()
    print(sd.get_prices(e_price=EPrice.SINGLE_USER))

    # time.sleep(60)


