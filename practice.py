import requests 

url = "https://buyme.co.il/siteapi"
def register():
    payload = {" password":"Aa123456789","name":"Michael","username":"rasaf67031@gosarlar.com","confirm":"Aa123456789","termsAndConditions":"true","creation_source":"11"}
    response = requests.request("POST" , url + "/register", data=payload)
    print(response.json)

register()