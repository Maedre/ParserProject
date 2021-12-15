import json
import re


class Register:
    registered_users = {}

    def __init__(self, input_files):
        # todo
        # implement error checks1
        # e-mail validity and ip address validity: discard if format is not correct
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
                    # merge devices if the email exist in registered user base
                    if email in self.registered_users:
                        devices = self.__merge_devices(self.registered_users[email]["devices"], devices) 
                    # update the entry
                    self.registered_users[email]={"name"   : name,\
                                                  "ip"     : ip,\
                                                  "devices": devices}
    
    def __merge_devices(self, devices_i1, devices_i2):
        """private method for merging devices of user instances""" 
        return list(set(devices_i1) | set(devices_i2))

    def __is_key(self, key):
        # checks if the key exists in the registered user base
        if(self.registered_users.get(key)):
            return True
        else:
            return False

    def __is_IP(self, ip):
        # checks if the registered IP of the key is a valid IPv4 address
        IPv4Pattern = r'^([\d]{1,3}.){3}[\d]{1,3}$'
        if re.match(IPv4Pattern, ip) is None:
            return False
        else:
            return True

    # overloaded methods
    def __len__(self):
        return len(self.registered_users)

    def __getitem__(self, key):
        if self.__is_key(key):
            return self.registered_users[key]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def __setitem__(self, key, value):
        if self.__is_key(key):
            if self.__is_IP(value["ip"]):
                self.registered_users[key] = value
            else:
                print(f"Invalid IP address for the user {self.get_name(key)}.")
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")
        

    def __add__(self, other):
        # todo
        pass

    def __mul__(self, other):
        # todo
        pass

    def get_name(self, key):
        if self.__is_key(key):
            return self.registered_users[key]["name"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")
        

    def get_IP(self, key):
        if self.__is_key(key):
            return self.registered_users[key]["ip"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def get_devices(self, key):
        if self.__is_key(key):
            return self.registered_users[key]["devices"]
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_name(self, key, name):
        if self.__is_key(key):
            self.registered_users[key]["name"] = name
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_IP(self, key, ip):
        if self.__is_key(key):
            if self.__is_IP(ip):
                self.registered_users[key]["ip"] = ip
            else:
                print(f"Invalid IP address for the user {self.get_name(key)}.")
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

    def set_devices(self, key, devices):
        if self.__is_key(key):
            self.registered_users[key]["devices"] = devices
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")

if __name__ == "__main__":
    Register1 = Register(["users_1.json"])
    print(len(Register1))
    print(Register1["onurcirit@gmail.com"])
    Register1["onurcirit@gmail.com"]={"name"    : "Mehmet Onur Cirit",\
                                      "ip"      : "192.168.0.1",\
                                      "devices": ["phone", "PC"] }
    print(Register1["onurcirit@gmail.com"])
    print(Register1.get_name("onurcirit@gmail.com"))
    print(Register1.get_IP("onurcirit@gmail.com"))
    print(Register1.get_devices("onurcirit@gmail.com"))
    Register1.set_IP("onurcirit@gmail.com","1.1.1.1")
    print(Register1.get_IP("onurcirit@gmail.com"))
    Register1.set_devices("onurcirit@gmail.com", ["RDPN-1 phone"])
    print(Register1.get_devices("onurcirit@gmail.com"))

