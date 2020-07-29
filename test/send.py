import requests
url="http://localhost:5000/api/data"
my_data = {'date': '2020-08-01', 'cases': '4500000'}
x=requests.post(url,data=my_data)
print(x.text)

my_data = {'date': '2020-08-01', 'cases': '4800000'}
x=requests.post(url,data=my_data)
print(x.text)

my_data = {'date': '2020-08-05', 'cases': '4800000'}
x=requests.post(url,data=my_data)
print(x.text)