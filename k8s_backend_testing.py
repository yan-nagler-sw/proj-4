print(__file__)
print("===")
print()


import requests
import db_connector as db

print("__name__:", __name__)
print()


txt_k8s_svc_url = "k8s_url.txt"

f = open(txt_k8s_svc_url, "r")
url_base = f.read()
print(url_base)


url_test = "{url}/test".format(url = url_base)
url_tbl = "{url}/{tbl}".format(url = url_base, tbl = db.tbl_users)


url = url_test
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()


"""
url = url_tbl
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()


url = "{url}/{id}".format(url = url_tbl, id = 1)
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()


url = "{url}/{id}".format(url = url_tbl, id = 3)
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()


url = "{url}/{id}".format(url = url_tbl, id = 3)
print(url)

usr_json = {db.usr_name: "name-c"}
print(usr_json)

resp = requests.post(url, json = usr_json)
print(resp)
if (not resp.ok):
    print("Failed to execute request - POST")

print(resp.json())
print()


resp = requests.post(url, json = usr_json) # Error - Duplicate ID
print(resp)
if (not resp.ok):
    print("Failed to execute request - POST")

print(resp.json())
print()


usr_json = {db.usr_name: "name-cc"}
print(usr_json)

resp = requests.put(url, json = usr_json)
print(resp)
if (not resp.ok):
    print("Failed to execute request - PUT")

print(resp.json())
print()


url = url_tbl
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()


url = "{url}/{id}".format(url = url_tbl, id = 3)
print(url)

resp = requests.delete(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - DELETE")

print(resp.json())
print()


url = url_tbl
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()
print()
"""
