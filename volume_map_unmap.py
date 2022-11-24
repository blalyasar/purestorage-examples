import warnings
warnings.filterwarnings("ignore")
import csv
from purestorage import FlashArray
from collections import defaultdict


# # from requests.packages.urllib3.exceptions import InsecureRequestWarning
# # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



import configparser
from configparser import ConfigParser
  
configur = ConfigParser()
configur.read('config.ini')

PURE_TOKEN_TEST_ESKI = configur.get("DEFAULT","pure_token_test_eski")
PURE_TOKEN_TEST_YENI = configur.get("DEFAULT","pure_token_test_yeni")
# print(PURE_TOKEN_TEST_ESKI)
# print(PURE_TOKEN_TEST_YENI)


array = FlashArray("yourip",
        api_token=PURE_TOKEN_TEST_ESKI)


with open('hosts.csv', 'r') as file: # 01 02 host aynı
    csv_reader = csv.reader(file)
    headers = next(csv_reader, None) # without name ....

    # for line in csv_reader:
    #     print(line[0])
    example_host = [row[0] for row in csv_reader]
# print(example_host) # sadece volume name
    



with open('volumes45.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader, None) # without name ....

    # for line in csv_reader:
    #     print(line[0])
    example_volume = [row[0] for row in csv_reader]
# print(example_volume) # sadece volume name



d = {x:[] for x in example_host}

# print(d) # {'xdev': [], 'xde': [], 'xmi01': [].....





def myfunction(example_volume):
    # print(example_volume)
    # print(type(example_volume))
    for i in example_volume:

        example_volume_to_host_name_pod = i.split(":")[2]
        example_volume_to_host_name = example_volume_to_host_name_pod.split('-')
    
        print(example_volume_to_host_name[0]) # xtbx01 02 ....
        try:
            d[example_volume_to_host_name[0]].append(i)
            print(d)
        except:
            print("Volume isminde host yok anti pattern :", i)

            continue
    return example_volume_to_host_name

myfunction(example_volume)

d_list = []
for host, value in  d.items():
#    print(  host, value)
   for vol_name in value:
        # print(host,vol_name)
        try:
            # array.connect_host(host, vol_name)
            # print(" Connected... ",host," ",vol_name)
            
            array.disconnect_host(host,vol_name)
            print(" DisConnected... ",host," ",vol_name)
            

        except:
            print(" Not Connected... ",host," ",vol_name)
            continue
# session end
array.invalidate_cookie()
