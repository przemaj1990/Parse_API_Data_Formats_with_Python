import re

class ConfigurationParser:
    deviceConfig = open('config.txt', 'r').read()

    # def parseCustomerName(self):
    #     customerNamePattern = r"ip vrf ([a-zA-Z_]+)\n"
    #     custmerNames = re.findall(customerNamePattern, self.deviceConfig)
    #     return custmerNames

    def parseCustomerName(self):
        intPattern = (
                r"interface GigabitEthernet0/0.([0-9]+)\n encapsulation "
                r"dot1Q [0-9]+\n ip vrf forwarding %s"
                % (customerName)
        )
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        return int(allCustomerSubinterfaces.group(1))