from model.customer.CustomerDao import CustomerDao
from model.genre.GenreDao import GenreDao


class Main:
    def test_genre(self):
        genres = GenreDao.load_all()
        for genre in genres:
            print(f"{genre.get_oid()} - {genre.get_description()}")

        g = GenreDao(2)
        print(g.get_description())

    def test_customer(self):
        customers = CustomerDao.load_all()
        for customer in customers:
            print(
                f"Oid: {customer.get_oid()}, Name: {customer.get_name()}, PhoneNo: {customer.get_phone_no()}, Email: {customer.get_email()}")

        cs = CustomerDao(3)
        print(f"\nOid: {cs.get_oid()}, Name: {cs.get_name()}, PhoneNo: {cs.get_phone_no()}, Email: {cs.get_email()}")


if __name__ == "__main__":
    m = Main()
    m.test_genre()

    print()

    m.test_customer()
