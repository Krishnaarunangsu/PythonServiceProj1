from requests import post

uuid = 1234
post_url = 'http://localhost:5000/api/add_message/1234'
json_params = {"mytext": "Hi TCG"}
# res = post(post_url, json={"mytext": "Hi TCG"})
res = post('http://localhost:5000/api/add_message7', json=json_params)
if res.ok:
    print(res.json())
