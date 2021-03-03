print(__file__)
print("===")
print()


import db_connector as db

print("__name__:", __name__)
print()


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.open_conn")


# Table: users

def print_usrs (usrs):
    print("---")
    for usr in usrs:
        print(usr)


rc = db.del_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_usrs")

print()


rc, usrs = db.get_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usrs")

print_usrs(usrs)
print()


usr = {db.usr_id: 1, db.usr_name: "name-a"}

rc = db.add_usr(conn, usr)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_usr")


usr = {db.usr_id: 2, db.usr_name: "name-b"}

rc = db.add_usr(conn, usr)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_usr")


usr = {db.usr_id: 3, db.usr_name: "name-c"}

rc = db.add_usr(conn, usr)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_usr")

print()


rc, usrs = db.get_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usrs")

print_usrs(usrs)
print()


rc = db.add_usr(conn, usr) # Error - Duplicate ID
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_usr")

print()


usr = {db.usr_id: 3, db.usr_name: "name-cc"}

rc = db.set_usr(conn, usr)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.set_usr")

print()


rc, usrs = db.get_usr(conn, 3)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usr")

print_usrs(usrs)
print()


rc = db.del_usr(conn, 3)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_usr")

print()


rc, usrs = db.get_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usrs")

print_usrs(usrs)
print()

print("===")
print()


# Table: config

def print_cfgs (cfgs):
    print("---")
    for cfg in cfgs:
        print(cfg)


rc = db.del_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_cfgs")

print()


rc, cfgs = db.get_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfgs")

print_cfgs(cfgs)
print()


url = "http://127.0.0.1:30001/users/get_user_data/1"

cfg = {db.cfg_url: url, db.cfg_bws: "chrome", db.cfg_usr_name: "name-a"}

rc = db.add_cfg(conn, cfg)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_cfg")

print()


rc, cfgs = db.get_cfg(conn, url)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfg")

print_cfgs(cfgs)
print()


rc = db.close_conn(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.close_conn")

print()
