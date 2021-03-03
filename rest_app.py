print(__file__)
print("===")
print()


import os
import signal
from flask import Flask, request

import db_connector as db

print("__name__:", __name__)
print()


app = Flask(__name__)

rc_ok = 200
rc_err = 500

rc_err_dupl_id = 1062


@app.route('/test', methods = ['GET'])
def test ():
    print("test()")

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/stop_server', methods = ['GET'])
def stop_server ():
    print("stop_server()")

    os.kill(os.getpid(), signal.CTRL_C_EVENT)

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users', methods = ['GET'])
def get_usrs ():
    print("get_usrs()")

    try:
        rc, usrs = db.get_usrs(conn)
        if (rc != db.rc_ok):
            print("Error: Failed to execute - db.get_usrs")
            exit(1)

    except Exception as ex:
        print("Error - get_usrs: {0}".format(ex))
        exit(1)

    ret_json = {"Status": "Ok", "Result": usrs}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users/<id>', methods = ['GET'])
def get_usr (id):
    print("get_usr()")

    try:
        rc, usr = db.get_usr(conn, id)
        if (rc != db.rc_ok):
            print("Error: Failed to execute - db.get_usr")
            exit(1)

        if (len(usr) == 0):
            ret_json = {"Status": "Error", "Reason": "Illegal ID"}
            print(ret_json)

            return ret_json, rc_err

    except Exception as ex:
        print("Error - get_usr: {0}".format(ex))
        exit(1)

    ret_json = {"Status": "Ok", "Result": usr}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users/<id>', methods = ['POST'])
def add_usr (id):
    print("add_usr()")

    try:
        usr = request.json
        usr[db.usr_id] = id
        print(usr)

        rc = db.add_usr(conn, usr)
        if (rc != db.rc_ok):
            if (rc == rc_err_dupl_id): # Error - Duplicate ID
                return add_usr(str(int(id) + 1))
            else:
                print("Error: Failed to execute - db.add_usr")

                ret_json = {"Status": "Error", "Reason": "Illegal ID"}
                print(ret_json)

                return ret_json, rc_err

    except Exception as ex:
        print("Error - add_usr: {0}".format(ex))
        exit(1)

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users/<id>', methods = ['PUT'])
def set_usr (id):
    print("set_usr()")

    try:
        usr = request.json
        usr[db.usr_id] = id
        print(usr)

        rc = db.set_usr(conn, usr)
        if (rc != db.rc_ok):
            print("Error: Failed to execute - db.set_usr")

            ret_json = {"Status": "Error", "Reason": "Illegal ID"}
            print(ret_json)

            return ret_json, rc_err

    except Exception as ex:
        print("Error - set_usr: {0}".format(ex))
        exit(1)

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users/<id>', methods = ['DELETE'])
def del_usr (id):
    print("del_usr()")

    try:
        rc = db.del_usr(conn, id)
        if (rc != db.rc_ok):
            print("Error: Failed to execute - db.del_usr")

            ret_json = {"Status": "Error", "Reason": "Illegal ID"}
            print(ret_json)

            return ret_json, rc_err

    except Exception as ex:
        print("Error - del_usr: {0}".format(ex))
        exit(1)

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute - db.open_conn")
    exit(1)

app.run(host = '0.0.0.0', debug = True, port = 30000)

print()
print()
