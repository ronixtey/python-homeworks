import requests;

r = requests.get("http://httpbin.org/get", params={'id': 8, 'post': 98});
print(r.text);

r = requests.post("http://httpbin.org/post", data='{key": "value"}')
# print("Headers: " + str(r.headers));
print("Text:" + str(r.text));
# print("URL: " + str(r.url));

r = requests.put("http://httpbin.org/put", data='{key": "value"}')
print("Text:" + str(r.text));

r = requests.delete("http://httpbin.org/delete");
print("Text:" + str(r.text));

r = requests.head("http://httpbin.org/get");
print("Text:" + str(r));

r = requests.options("http://httpbin.org/get");
print("Text:" + str(r));
