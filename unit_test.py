import random
import unittest
from main import *

Register_test = Register(["users_1.json"])

class TestSequenceFunctions(unittest.TestCase):
    def test_GetIP(self):
        stored_ip = Register_test.get_IP("onurcirit@gmail.com")
        self.assertEqual(stored_ip, "131.116.31.131")

    def test_GetName(self):
        stored_name = Register_test.get_name("cansivri@gmail.com")
        self.assertEqual(stored_name, "Ahmet Can Sivri")

    def test_GetDevices(self):
        stored_devices = Register_test.get_devices("cansivri@gmail.com")
        self.assertEqual(stored_devices, ["desktop RDPN-8239"])

    def test_SetIp(self):
        Register_test.set_IP("cansivri@gmail.com","1.1.1.1")
        stored_set_ip = Register_test.get_IP("cansivri@gmail.com")
        self.assertEqual(stored_set_ip, "1.1.1.1")

    def test_SetDevice(self):
        Register_test.set_devices("onurcirit@gmail.com", ["RDPN-1 phone"])
        stored_set_device = Register_test.get_devices("onurcirit@gmail.com")
        self.assertEqual(stored_set_device, ["RDPN-1 phone"])

    def test_SetName(self):
        Register_test.set_name("cansivri@gmail.com", "Can Sivri")
        stored_set_name = Register_test.get_name("cansivri@gmail.com")
        self.assertEqual(stored_set_name, "Can Sivri")

    def test_is_key_true(self):
        stored_return = Register_test._is_key("cansivri@gmail.com")
        self.assertTrue(stored_return)
    
    def test_is_key_false(self):
        stored_return = Register_test._is_key("fernandomuslera@gmail.com")
        self.assertFalse(stored_return)

   # def test_get_item(self):
        
if __name__ == '__main__':
    unittest.main()