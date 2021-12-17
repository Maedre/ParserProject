import json
import re


class Register:

    def __init__(self, input_files):
        # todo
        # optional: run json parsers in parallel
        self.registered_users = {}
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
                    if not self._is_IP(ip):
                        print(f"Invalid IP address for the user {name}.")
                        continue    # skip the user with corrupted IP address
                    if not self._is_email(email):
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
        device_list = list(set(devices_i1) | set(devices_i2))
        device_list.sort()
        return device_list

    def _is_key(self, key):
        # checks if the key exists in the registered user base
        if(self.registered_users.get(key)):
            return True
        else:
            return False

    def _is_IP(self, ip):
        # checks if the IP is a valid IPv4 address
        IPv4Pattern = r'^([\d]{1,3}.){3}[\d]{1,3}$'
        if re.match(IPv4Pattern, ip) is None:
            return False
        else:
            return True

    def _is_email(self, email):
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
            if self._is_IP(value["ip"]) or self._is_email(value["email"]):
                self.registered_users[key] = value
            else:
                print(f"Invalid IP or e-mail address for the user {self.get_name(key)}.")
        else:
            print(f"Invalid user key. Check the e-mail address \"{key}\".")
        

    def __add__(self, other):
        Req=dict()
        out_register = Register([])
        Req|=self.registered_users | other.registered_users
        out_register.registered_users = Req
        return out_register

    def __mul__(self, other):
        new_reg = dict()
        out_register = Register([])
        common_users = self.registered_users.keys() & other.registered_users.keys()
        # merge devices of common users
        for key in common_users:
            devices = self._merge_devices(self.registered_users[key]["devices"],other.registered_users[key]["devices"])
            new_reg.update({key: self.registered_users[key]})
            new_reg[key]["devices"] = devices
        out_register.registered_users = new_reg
        return out_register

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
            if self._is_IP(ip):
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
    dct_json = dict()
    counter = 0
    files = os.listdir(".")
    for file in files:
        if ".json" in file:
            counter += 1
            dct_json[str(counter)] = file
    if len(dct_json.keys()) == 0:
        print("No User Data in project folder!!\n")
        print("Program ended...\n")
    else:
        print(f"{len(dct_json.keys())} user data found in project folder.\n")
        lst_selec = ["g","s", "u", "m", "q"]
        usr_inp = input(
            f"Press G to get user register info\nPress S to set user to user register\nPress U to have union of 2 user register\nPress M to have intersection of two register\nPress Q to exit\n")
        usr_inp = usr_inp.lower()
        while not (usr_inp in lst_selec):
            print("Invalid Character!!!\n")
            usr_inp = input(
                f"Press G to get user register info\nPress S to set info to user register\nPress U to have union of 2 user register\nPress M to have intersection of two register\nPress Q to exit\n")
            usr_inp = usr_inp.lower()
        if usr_inp == "q":
            print("Program ended...\n")
        elif usr_inp == "g":
            data_inp= input(f"Press select user data from 1 to {len(dct_json.keys())}\n")
            while not( data_inp in dct_json.keys()):
                print("Invalid Character!!!\n")
                data_inp = input(f"Press select user data from 1 to {len(dct_json.keys())}\n")
            lst_opt=["a","s"]
            opt_inp=(input(f"Do want to show all info in register (A)  or info for individual user(S)?")).lower()
            while not (opt_inp in lst_opt):
                print("Invalid Character!!!\n")
                opt_inp = (input(f"Do want to show all info in register (A)  or info for individual user(S)?")).lower(g)
            Req = Register([dct_json[data_inp]])
            if opt_inp =="a":
                print(Req)
            else:
                inp_add=input("Enter user mail address\n")
                Info_Req=Req[inp_add]
                while Info_Req==None:
                    inp_add = input("Enter user mail address\n")
                    Info_Req = Req[inp_add]
                print(f"Name: {Req.get_name(inp_add)}")
                print(f"IP Address: {Req.get_IP(inp_add)}")
                print(f"Devices: {Req.get_devices(inp_add)}")
        elif usr_inp=="s":
            data_inp= input(f"Press select user data from 1 to {len(dct_json.keys())}\n")
            while not( data_inp in dct_json.keys()):
                print("Invalid Character!!!\n")
                data_inp = input(f"Press select user data from 1 to {len(dct_json.keys())}\n")
            Req = Register([dct_json[data_inp]])
            inp_add = input("Enter user mail address\n")
            Info_Req = Req[inp_add]
            while Info_Req == None:
                inp_add = input("Enter user mail address\n")
                Info_Req = Req[inp_add]
            inp_name=input("Set a name to user\n")
            Req.set_name(inp_add,inp_name)
            inp_IP=input("Set an IP to user\n")
            Req.set_IP(inp_add,inp_IP)
            inp_devices=input("Set a device to user\n")
            Req.set_devices(inp_add,inp_devices)
            print(f"Name: {Req.get_name(inp_add)}")
            print(f"IP Address: {Req.get_IP(inp_add)}")
            print(f"Devices: {Req.get_devices(inp_add)}")
        elif usr_inp=="u":
            input_1=input("For union; *.Register?")
            while not (input_1 in dct_json.keys()):
                print("Invalid number!!!")
                input_1 = input("For union; *.Register?")
            input_2 = input("For union; *.Register?")
            while not (input_2 in dct_json.keys()):
                print("Invalid number!!!")
                input_2 = input("For union; *.Register?")
            Req1=Register([dct_json[input_1]])
            Req2=Register([dct_json[input_2]])
            Req3=Req1+Req2
            print(Req3)
        else:
            input_1=input("For intersection; *.Register?")
            while not (input_1 in dct_json.keys()):
                print("Invalid number!!!")
                input_1 = input("For intersection; *.Register?")
            input_2 = input("For intersection; *.Register?")
            while not (input_2 in dct_json.keys()):
                print("Invalid number!!!")
                input_2 = input("For intersection; *.Register?")
            Req1=Register([dct_json[input_1]])
            Req2=Register([dct_json[input_2]])
            Req3=Req1*Req2
            print(Req3)

