print(__file__)
print("===")
print()


import requests

print("__name__:", __name__)
print()


rest_url_base = "http://127.0.0.1:30000"

def stop_server (url_base):
    url = "{url}/stop_server".format(url = url_base)
    print(url)

    resp = requests.get(url)
    print(resp)
    if (not resp.ok):
        print("Failed to execute request - GET")


try:
    stop_server(rest_url_base)

except Exception as ex:
    print("stop_server - REST: {0}".format(ex))

print()
print()
