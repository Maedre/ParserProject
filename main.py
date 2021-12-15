import json
import re


class Register:
    registered_users = {}

    def __init__(self, input_files):
        # todo
        # optional: run json parsers in parallel
        for input_file in input_files:
            with open(input_file) as f:
                users = json.load(f)

                for user in users:
                    # save user data for better readibility
                    name    = user["name"]
                    email   = user["email"]
                    ip      = user["ip"]
                    devices = user["devices"]
                    # check validity of IP and e-mail addresses
                    if not self.__is_IP(ip):
                        print(f"Invalid IP address for the user {name}.")
                        continue    # skip the user with corrupted IP address
                    if not self.__is_email(email):
                        print(f"E-mail address {email} is not valid.")
                        continue    # skip the user with corrupted e-mail address

                    # merge devices if the email exist in registered user base
                    if email in self.registered_users:
                        devices = self._merge_devices(self.registered_users[email]["devices"], devices) 
                    # update the entry
                    self.registered_users[email]={"name"   : name,\
                                                  "ip"     : ip,\
                                                  "devices": devices}

    def _merge_devices(self, devices_i1, devices_i2):
        """private method for merging devices of user instances""" 
        return list(set(devices_i1) | set(devices_i2))

    def _is_key(self, key):
        # checks if the key exists in the registered user base
        if(self.registered_users.get(key)):
            return True
        else:
            return False

    def __is_IP(self, ip):
        # checks if the IP is a valid IPv4 address
        IPv4Pattern = r'^([\d]{1,3}.){3}[\d]{1,3}$'
        if re.match(IPv4Pattern, ip) is None:
            return False
        else:
            return True

    def __is_email(self, email):
        # checks if the e-mail address is valid
        re_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(re_email, email) is None:
            return False
        else:
            return True

    # overloaded methods
    def __str__(self):
        str_out = ""
        for user in self.registered_users:
            str_out += f'{user}:\
                           [name: {self.registered_users[user]["name"]}]\
                           [IP: {self.registered_users[user]["ip"]}]\
                           [devices: {self.registered_users[user]["devices"]}]\n'
        return str_out


    def __len__(self):
        return len(self.registered_users)

    def __getitem__(self, key):
        if self._is_key(key):
            return self.registered_users[key]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def __setitem__(self, key, value):
        if self._is_key(key):
            if self.__is_IP(value["ip"]) or self.__is_email(value["email"]):
                self.registered_users[key] = value
            else:
                print(f"Invalid IP or e-mail address for the user {self.get_name(key)}.")
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")
        

    def __add__(self, other):
        # todo
        pass

    def __mul__(self, other):
        # todo
        pass

    def get_name(self, key):
        if self._is_key(key):
            return self.registered_users[key]["name"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")
        

    def get_IP(self, key):
        if self._is_key(key):
            return self.registered_users[key]["ip"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def get_devices(self, key):
        if self._is_key(key):
            return self.registered_users[key]["devices"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_name(self, key, name):
        if self._is_key(key):
            self.registered_users[key]["name"] = name
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_IP(self, key, ip):
        if self._is_key(key):
            if self.__is_IP(ip):
                self.registered_users[key]["ip"] = ip
            else:
                print(f"Invalid IP address for the user {self.get_name(key)}.")
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_devices(self, key, devices):
        if self._is_key(key):
            self.registered_users[key]["devices"] = devices
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

if __name__ == "__main__":
    # Demo
    demo_register1 = Register(["users_3.json", "users_4.json"])
    # accessing user register content (__str__, __len__)
    print(f"The length of the register is {len(demo_register1)}")
    print(demo_register1)
    # accessing individual users (__getitem__, __set_item__)
    print(demo_register1["bradpitt@gmail.com"])
    demo_register1["bradpitt@gmail.com"]={"name"    : "William Bradley Pitt",\
                                          "ip"      : "192.168.0.1",\
                                          "devices": ["Phone-Bradley", "DESKTOP-BRADLEY"]}              
    print(demo_register1["bradpitt@gmail.com"])
    # accessing attributes of a user (getter and setter methods)
    print(demo_register1.get_name("bradpitt@gmail.com"))
    print(demo_register1.get_IP("bradpitt@gmail.com"))
    print(demo_register1.get_devices("bradpitt@gmail.com"))
    demo_register1.set_name("bradpitt@gmail.com","Brad Pitt")
    print(demo_register1.get_name("bradpitt@gmail.com"))
    demo_register1.set_IP("bradpitt@gmail.com","1.1.1.1")
    print(demo_register1.get_IP("bradpitt@gmail.com"))
    demo_register1.set_devices("bradpitt@gmail.com", ["RDPN-1 phone"])
    print(demo_register1.get_devices("bradpitt@gmail.com"))