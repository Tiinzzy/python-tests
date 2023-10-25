import time

from model.customer.CustomerDao import CustomerDao
from model.genre.GenreDao import GenreDao
from model.movies.MoviesDao import MoviesDao


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


if __name__ == "__main__":
    test_genre()

    print()
    test_customer()

    print()
    test_movie()
    # time.sleep(60)
