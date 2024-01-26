import requests

url = 'http://127.0.0.1:5000'
r = requests.get("https://api.stumbleguys.com/shared")
api = "kitkabackend.eastus.cloudapp.azure.com:5010"
auth = '{"DeviceId":"steam_76561199466894005","GoogleId":"","FacebookId":"","Token":"14000000697967261F700BFDB552CD590100100107313664180000000100000002000000FC9C27373332155BFCED270005000000B20000003200000004000000B552CD5901001001AC991900561E655E0138A8C00000000080DA2E64008A4A64010012C40A0000000000406A964FFC0B57266B40D838FE1F5B55ECD35356F901D124E33B62AE8196841B86CC0C86D726731D7BDA065B5AC1212D2A2A51C1D28B8C3C252C27B39615B12CA9EC37DD325EAC8D9E54D82B7E4E0DF7CA123D67DACB17735B8E92EC2D64E429EED3F3203652580C85D0A580F0B5B79A9C090844260BAFAD3D3344F88BEBB716","Timestamp":0000000000,"Hash":"01GNN43742ZSNK8267ZNFKY2RV"}'
headers = {
                'authorization': auth,
                'use_response_compression': 'true',
                'Accept-Encoding': 'gzip',
                'Host': api,
                'Connection': None,
                'User-Agent': None,
            }
# replace with your local server URL
payload = {'key1': 'value1', 'key2': 'value2'}  # replace with your data
pos = 0;
response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
print(response.text.split('Crowns:')[1].split(',')[0])


