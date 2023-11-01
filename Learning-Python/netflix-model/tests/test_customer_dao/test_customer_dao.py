import unittest
from model.customer.customer_dao import CustomerDao


class TestCustomerDao(unittest.TestCase):

    def test_save_to_table(self):
        customer = CustomerDao("Kiana", "4168795432", "kiana@email.com", )
        customer.save_to_table()

        self.assertTrue(customer.get_oid() > 0)
        self.assertEqual(customer.get_name(), "Kiana")
        self.assertEqual(customer.get_email(), "kiana@email.com")
        self.assertEqual(customer.get_phone_no(), "4168795432")

    def test_load_all(self):
        customers = CustomerDao.load_all()
        print(customers)
        self.assertTrue(len(customers) > 0)

    def test_add_and_delete(self):
        customer = CustomerDao("Lida", "09122066220", "lida@email.com")
        customer.save_to_table()

        self.assertTrue(customer.get_oid() > 0)
        self.assertEqual(customer.get_name(), "Lida")
        self.assertEqual(customer.get_email(), "lida@email.com")
        self.assertEqual(customer.get_phone_no(), "09122066220")

        customer_id = customer.get_oid()
        result = customer.delete(customer_id)
        self.assertEqual(result, None)

    def test_update(self):
        customer = CustomerDao(oid=107)
        customer.set_name("TINA JOON")
        customer.set_email("tina_joon@email.com")
        customer.set_phone_no("435346456634")
        customer.save_to_table()
        self.assertEqual(customer.get_name(), "TINA JOON")
        self.assertEqual(customer.get_email(), "tina_joon@email.com")
        self.assertEqual(customer.get_phone_no(), "435346456634")