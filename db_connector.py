"""
The documentation created using the following command:
python -m pydoc -w proj-1\db_connector.py


DB data:
---

www.remotemysql.com
yan.nagler@gmail.com
qazQWE123

Username: fFFGNbw0B0
Database name: fFFGNbw0B0
Password: 66VHtH6ctH
Server: remotemysql.com
Port: 3306

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `creation_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `config` (
  `url` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `browser` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `user_name` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
"""

print(__file__)
print("===")
print()


import pymysql
import datetime

print("__name__:", __name__)
print()


_host = "remotemysql.com"
_usr = "fFFGNbw0B0"
_pwd = "66VHtH6ctH"
_db = "fFFGNbw0B0"

"""
_host = "127.0.0.1"
_usr = "yan-nagler"
_pwd = "qazQWE123"
_db = "db"
"""

_port = 3306


rc_ok = 0
rc_err = 1


def open_conn ():
    """
    Opens the connection to the DB.
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        conn = pymysql.connect(host = _host,
                               port = _port,
                               user = _usr,
                               passwd = _pwd,
                               db = _db)
        conn.autocommit(True)

    except Exception as ex:
        print("Error - open_conn: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok, conn


def close_conn (conn):
    """
    Closes the connection to the DB.
    @param conn: DB connection
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        conn.close()

    except Exception as ex:
        print("Error - close_conn: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


# Table: users

tbl_users = "users"
_tbl_users = _db + "." + tbl_users

_tbl_users_col1 = "id"
_tbl_users_col2 = "name"
_tbl_users_col3 = "creation_date"

usr_id = _tbl_users_col1
usr_name = _tbl_users_col2
usr_creation_date = _tbl_users_col3

usr_id_idx = 0
usr_name_idx = 1
usr_creation_date_idx = 2


def get_usrs (conn):
    """
    Gets all the user from the 'users' table.
    @param conn: DB connection
    @return: Return code: 0 - Ok, 1 - Fail
    """

    res = []

    try:
        csr = conn.cursor()

        cmd = "SELECT * FROM {tbl};".\
            format(tbl = _tbl_users)
        print(cmd)

        csr.execute(cmd)

        for row in csr:
            res.append(row)

        csr.close()

    except Exception as ex:
        print("Error - get_usrs: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok, res


def get_usr (conn, id):
    """
    Gets user from the 'users' table.
    @param conn: DB connection
    @param id: User ID (PK)
    @return: Return code: 0 - Ok, 1 - Fail
    """

    res = []

    try:
        csr = conn.cursor()

        cmd = "SELECT * FROM {tbl} WHERE {col1} = {val1};".\
            format(tbl = _tbl_users,
                   col1 = _tbl_users_col1, val1 = id)
        print(cmd)

        csr.execute(cmd)

        for row in csr:
            res.append(row)

        csr.close()

    except Exception as ex:
        print("Error - get_usr: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok, res


def add_usr (conn, usr):
    """
    Adds user to the 'users' table.
    @param conn: DB connection
    @param usr: User data
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "INSERT INTO {tbl} ({col1}, {col2}, {col3}) VALUES (%s, %s, %s);".\
            format(tbl = _tbl_users,
                   col1 = _tbl_users_col1,
                   col2 = _tbl_users_col2,
                   col3 = _tbl_users_col3)
        print(cmd)

        dt = datetime.datetime.now()
        vals = (usr[usr_id], usr[usr_name], dt)
        csr.execute(cmd, vals)

        csr.close()

    except Exception as ex:
        print("Error - add_usr: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


def set_usr (conn, usr):
    """
    Sets/Updates user in the 'users' table.
    @param conn: DB connection
    @param usr: User data
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "UPDATE {tbl} SET {col2} = %s WHERE {col1} = %s;".\
            format(tbl = _tbl_users,
                   col2 = _tbl_users_col2,
                   col1 = _tbl_users_col1)
        print(cmd)

        vals = (usr[usr_name], usr[usr_id])
        csr.execute(cmd, vals)

        csr.close()

    except Exception as ex:
        print("Error - set_usr: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


def del_usrs (conn):
    """
    Deletes all the users from the 'users' table.
    @param conn: DB connection
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "DELETE FROM {tbl};".\
            format(tbl = _tbl_users)
        print(cmd)

        csr.execute(cmd)
        csr.close()

    except Exception as ex:
        print("Error - del_usrs: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


def del_usr (conn, id):
    """
    Deletes user from the 'users' table.
    @param conn: DB connection
    @param id: User ID (PK)
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "DELETE FROM {tbl} WHERE {col1} = {val1};".\
            format(tbl = _tbl_users,
                   col1 = _tbl_users_col1, val1 = id)
        print(cmd)

        csr.execute(cmd)
        csr.close()

    except Exception as ex:
        print("Error - del_usr: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


# Table: config

tbl_config = "config"
_tbl_config = _db + "." + tbl_config

_tbl_config_col1 = "url"
_tbl_config_col2 = "browser"
_tbl_config_col3 = "user_name"

cfg_url = _tbl_config_col1
cfg_bws = _tbl_config_col2
cfg_usr_name = _tbl_config_col3

cfg_url_idx = 0
cfg_bws_idx = 1
cfg_usr_name_idx = 2


def get_cfgs (conn):
    """
    Gets all the configurations from the 'config' table.
    @param conn: DB connection
    @return: Return code: 0 - Ok, 1 - Fail
    """

    res = []

    try:
        csr = conn.cursor()

        cmd = "SELECT * FROM {tbl};".\
            format(tbl = _tbl_config)
        print(cmd)

        csr.execute(cmd)

        for row in csr:
            res.append(row)

        csr.close()

    except Exception as ex:
        print("Error - get_cfgs: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok, res


def get_cfg (conn, url):
    """
    Gets configuration from the 'config' table.
    @param conn: DB connection
    @param url: Configuration URL (PK)
    @return: Return code: 0 - Ok, 1 - Fail
    """

    res = []

    try:
        csr = conn.cursor()

        cmd = "SELECT * FROM {tbl} WHERE {col1} = \"{val1}\";".\
            format(tbl = _tbl_config,
                   col1 = _tbl_config_col1, val1 = url)
        print(cmd)

        csr.execute(cmd)

        for row in csr:
            res.append(row)

        csr.close()

    except Exception as ex:
        print("Error - get_cfg: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok, res


def add_cfg (conn, cfg):
    """
    Adds configuration to the 'config' table.
    @param conn: DB connection
    @param cfg: configuration
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "INSERT INTO {tbl} ({col1}, {col2}, {col3}) VALUES (%s, %s, %s);".\
            format(tbl = _tbl_config,
                   col1 = _tbl_config_col1,
                   col2 = _tbl_config_col2,
                   col3 = _tbl_config_col3)
        print(cmd)

        dt = datetime.datetime.now()
        vals = (cfg[cfg_url], cfg[cfg_bws], cfg[cfg_usr_name])
        csr.execute(cmd, vals)

        csr.close()

    except Exception as ex:
        print("Error - add_cfg: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok


def del_cfgs (conn):
    """
    Deletes all the configurations from the 'config' table.
    @param conn: DB connection
    @return: Return code: 0 - Ok, 1 - Fail
    """

    try:
        csr = conn.cursor()

        cmd = "DELETE FROM {tbl};".\
            format(tbl = _tbl_config)
        print(cmd)

        csr.execute(cmd)
        csr.close()

    except Exception as ex:
        print("Error - del_cfgs: {0}".format(ex))
        rc_err = ex.args[0]
        return rc_err

    return rc_ok
