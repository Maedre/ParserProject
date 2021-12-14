import json


class Register:
    registered_users = {}

    def __init__(self, input_files):
        # todo
        # implement error checks1
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
                    devices = devices if email not in self.registered_users\
                            else self.__merge_devices(self.registered_users[email]["devices"], devices)
                    # update the entry
                    self.registered_users[email]={"name"   : name,\
                                                  "ip"     : ip,\
                                                  "devices": devices}
    
    def __merge_devices(self, devices_i1, devices_i2):
        """private method for merging devices of user instances""" 
        return list(set(devices_i1) | set(devices_i2))

    def __is_key(self, key):
        # todo
        # implement
        # checks if the key exists in the registered user base
        return True

    def __is_ip(self, key):
        # todo
        # implement
        # checks if the registered IP of the key is a valid IPv4 address
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
            if self.__is_ip(key):
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

    def set_IP(self, key, IP):
        if self.__is_key(key):
            if self.__is_ip(key):
                self.registered_users[key]["ip"] = IP
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
