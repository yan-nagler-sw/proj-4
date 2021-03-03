print(__file__)
print("===")
print()


import requests
import db_connector as db

print("__name__:", __name__)
print()


url_base = "http://127.0.0.1:30000"
url_tbl = "{url}/{tbl}".format(url = url_base, tbl = db.tbl_users)


def print_usrs (usrs):
    print("---")
    for usr in usrs:
        print(usr)


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.open_conn")


rc = db.del_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_usrs")

print()


url = "{url}/{id}".format(url = url_tbl, id = 1)
print(url)

usr_json = {db.usr_name: "name-a"}
print(usr_json)

resp = requests.post(url, json = usr_json)
print(resp)
if (not resp.ok):
    print("Failed to execute request - POST")

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


rc, usrs = db.get_usr(conn, 1)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usr")

print_usrs(usrs)
print()
print()
