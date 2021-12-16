import random
import unittest
from main import *

Register_test = Register(["users_1.json", "users_2.json", "users_3.json", "users_4.json"])

class TestSequenceFunctions(unittest.TestCase):
    def test_get_IP(self):
        stored_ip = Register_test.get_IP("onurcirit@gmail.com")
        self.assertEqual(stored_ip, "131.116.31.131")

    def test_get_IP_false(self):
        stored_ip = Register_test.get_IP("cirit@gmail.com")
        self.assertEqual(stored_ip, None)

    def test_get_name(self):
        stored_name = Register_test.get_name("cansivri@gmail.com")
        self.assertEqual(stored_name, "Ahmet Can Sivri")

    def test_get_name_false(self):
        stored_name = Register_test.get_name("sivri@gmail.com")
        self.assertEqual(stored_name, None)

    def test_get_devices(self):
        stored_devices = Register_test.get_devices("cansivri@gmail.com")
        self.assertEqual(stored_devices, ["desktop RDPN-8239"])

    def test_get_devices_false(self):
        stored_devices = Register_test.get_devices("sivri@gmail.com")
        self.assertEqual(stored_devices, None)

    def test_set_IP(self):
        Register_test.set_IP("cansivri@gmail.com","1.1.1.1")
        stored_set_ip = Register_test.get_IP("cansivri@gmail.com")
        self.assertEqual(stored_set_ip, "1.1.1.1")
        Register_test.set_IP("cansivri@gmail.com","245.14.240.222")

    def test_set_IP_false_key(self):
        stored_set_ip = Register_test.set_IP("sivri@gmail.com","1.1.1.1")
        self.assertEqual(stored_set_ip, None)

    def test_set_IP_false_ip(self):
        stored_set_ip = Register_test.set_IP("cansivri@gmail.com","1.1.1.&")
        self.assertEqual(stored_set_ip, None)

    def test_set_devices(self):
        Register_test.set_devices("onurcirit@gmail.com", ["RDPN-1 phone"])
        stored_set_device = Register_test.get_devices("onurcirit@gmail.com")
        self.assertEqual(stored_set_device, ["RDPN-1 phone"])

    def test_set_devices_false_key(self):
        stored_set_device = Register_test.set_devices("cirit@gmail.com", ["RDPN-1 phone"])
        self.assertEqual(stored_set_device, None)

    def test_set_name(self):
        Register_test.set_name("cansivri@gmail.com", "Can Sivri")
        stored_set_name = Register_test.get_name("cansivri@gmail.com")
        self.assertEqual(stored_set_name, "Can Sivri")
        Register_test.set_name("cansivri@gmail.com", "Ahmet Can Sivri")

    def test_set_name_false_key(self):
        stored_set_name = Register_test.set_name("sivri@gmail.com", "Can Sivri")
        self.assertEqual(stored_set_name, None)

    def test_is_key_true(self):
        stored_return = Register_test._is_key("cansivri@gmail.com")
        self.assertTrue(stored_return)
    
    def test_is_key_false(self):
        stored_return = Register_test._is_key("fernandomuslera@gmail.com")
        self.assertFalse(stored_return)

    def test__getitem__(self):
        stored_user = Register_test.__getitem__("cansivri@gmail.com")    
        self.assertDictEqual(stored_user, Register_test.registered_users["cansivri@gmail.com"])

    def test__getitem__false_key(self):
        stored_user = Register_test.__getitem__("sivri@gmail.com")    
        self.assertEqual(stored_user, None)

    def test__merge_devices(self):
        stored_device = Register_test._merge_devices(Register_test.registered_users["bradpitt@gmail.com"]["devices"], ["Panasonic"])
        Register_test.set_devices("bradpitt@gmail.com", stored_device)
        self.assertEqual(stored_device, Register_test.registered_users["bradpitt@gmail.com"]["devices"])

    def test__len__(self):
        stored_length = Register_test.__len__()
        self.assertEqual(stored_length, len(Register_test.registered_users))

    # def test__str__(self):
    #     stored_str = Register_test.__str__()
    #     self.assertEqual(stored_str, Register_test.registered_users)

    def test__is_email_true(self):
        stored_email_true = Register_test._is_email("cansivri@gmail.com")
        self.assertEqual(stored_email_true, True)

    def test__is_email_false(self):
        stored_email_false = Register_test._is_email("%&cansivri@gmail.com")
        self.assertEqual(stored_email_false, False)

    def test_is_IP_true(self):
        stored_ip_true = Register_test._is_IP("157.164.4.56")
        self.assertEqual(stored_ip_true, True)

    def test_is_IP_false(self):
        stored_ip_false = Register_test._is_IP("157.164.4.abc")
        self.assertEqual(stored_ip_false, False)

    # def test__set__item_true(self):
    #     stored_set_item = Register_test.__setitem__("cansivri@gmail.com", "154.12.15.47")
    #     self.assertEqual(stored_set_item, Register_test.registered_users("cansivri@gmail.com"))


    #__setitem__
    #__add__
    #__mul__




if __name__ == '__main__':
    unittest.main()