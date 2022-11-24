
from purestorage import FlashArray
import warnings
warnings.filterwarnings("ignore")

# https://pure-storage-python-rest-client.readthedocs.io/en/stable/quick_start.html

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#  https://github.com/PureStorage-OpenConnect/rest-client/commit/30231639d7d700682c6ee054426c968c8cbbcfcb#r40240923


import configparser

token = ""



array = FlashArray("your_api",api_token=token)

# hepsi lnx değil bazıları windows ona dikkat etmek lazımdı....
IQN_STANDART = "iqn.xx.xx.com:lnx:"


with open("./pure-host-list","r",encoding="utf-8") as phl:
    lines = phl.readlines()
# print(lines[0])


lines = [ lineone.replace("\n","") for lineone in lines]
# print(lines)

IQN_STANDART_LIST = [IQN_STANDART + line for line in lines]

# print(IQN_STANDART_LIST)
print(IQN_STANDART_LIST[0] ==  "iqn.xx.xx.com:lnx:host01")

assert len(IQN_STANDART_LIST) == len(lines)
# print(len(IQN_STANDART_LIST) == len(lines))

for  hostname, iqnname in zip(lines, IQN_STANDART_LIST):
    print(hostname, iqnname)
    # print(isinstance(iqnname, str))
    print(isinstance(hostname, str))
    #array.create_host(hostname, iqnlist=[iqnname])

# session end
array.invalidate_cookie()
