import unittest
from model.subscription.subscription_dao import SubscriptionDao, EPrice, ESubscriptionType


class TestSubscriptionDao(unittest.TestCase):

    def test_save_to_table(self):
        subscription = SubscriptionDao(ESubscriptionType.ANNUALLY, EPrice.MULTI_4K, "2023-10-10", "2024-10-10")
        subscription.save_to_table()

        self.assertTrue(subscription.get_oid() > 0)
        self.assertEqual(subscription.get_subscription_type(), ESubscriptionType.ANNUALLY)
        self.assertEqual(subscription.get_price(), EPrice.MULTI_4K)
        self.assertEqual(subscription.get_subscription_date(), "2023-10-10")
        self.assertEqual(subscription.get_expiry_date(), "2024-10-10")

    def test_load_all(self):
        subscribers = SubscriptionDao.load_all()
        print(subscribers)
        self.assertTrue(len(subscribers) > 0)

    def test_add_and_delete(self):
        subscription = SubscriptionDao(ESubscriptionType.MONTHLY, EPrice.SINGLE_USER, "2023-10-10", "2024-11-10")
        subscription.save_to_table()

        self.assertTrue(subscription.get_oid() > 0)
        self.assertEqual(subscription.get_subscription_type(), ESubscriptionType.MONTHLY)
        self.assertEqual(subscription.get_price(), EPrice.SINGLE_USER)
        self.assertEqual(subscription.get_subscription_date(), "2023-10-10")
        self.assertEqual(subscription.get_expiry_date(), "2024-11-10")

        customer_id = subscription.get_oid()
        result = subscription.delete(customer_id)
        self.assertEqual(result, None)

    def test_update(self):
        subscriber = SubscriptionDao(oid=121)
        subscriber.set_subscription_type(ESubscriptionType.ANNUALLY)
        subscriber.set_subscription_date("2025-10-10")
        subscriber.set_expiry_date("2026-10-10")
        subscriber.save_to_table()
        self.assertEqual(subscriber.get_subscription_type(), ESubscriptionType.ANNUALLY)
        self.assertEqual(subscriber.get_subscription_date(), "2025-10-10")
        self.assertEqual(subscriber.get_expiry_date(), "2026-10-10")


