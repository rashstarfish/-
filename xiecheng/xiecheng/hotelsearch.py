import requests
import json

url = "https://m.ctrip.com/restapi/soa2/21881/json/HotelSearch?testab=fb38c2750c0fa174c6e558d603ac0fbb936c6936058a3977f21032b9f168ae5e"

payload = json.dumps({
   "searchCondition": {
      "sortType": "1",
      "adult": 1,
      "child": 0,
      "age": "",
      "pageNo": 2,
      "optionType": "City",
      "optionId": "2",
      "lat": 0,
      "destination": "",
      "keyword": "",
      "cityName": "上海",
      "lng": 0,
      "cityId": 2,
      "checkIn": "2024-11-17",
      "checkOut": "2024-11-18",
      "timeOffset": 28800
   },
   "head": {
      "HotelExtension": {
         "hotelUuidKey": "a4XwakJ4dYDZiNlE8qeA5EFmI3Bv1Xw4Zw8Y7bj7oIZOYsLYpFEkOi6Tj7UWbY1OWszRBorf8ez0EO4jUZWPOvU4I9trPYZ4J1NwOQrAMIpswzlvq0jOJ1GvdSwZQvagjtJohjO6w3XRn3joJ7ZvpZYDlyBqjdMvTmeDdYafjzcy7FiP7eNcrtYSNenNR5qYagyOcjNov6TEnpvDgWFmj4GxU9KslRqYtcwbQEMfYg4YDbiOdwDBRm7EpbWLQEftRMUy8YFsEbdKN3YZ8wSFWqJ0YBOesnWoDKdNYmarU9wdY5fwd8j5EDzva1Y1tyBkjdtvDSefZYk7jU3yqJGzvh9Y9HyQSj5Nvske0BYdojGUyLJGTYPfv8pW0qW9cJ1diGBxmYPZwMQRX9x95vH3e7cY4tifOYTdKP9eMfrSYUv5Fy5SwZ3yFmYMfJlYtcKhkxoj8MJ5Ti8ZiHYk8JkPjdZyNhYUgi8DisUiAbjcBKfBvZlvUYt7RA3E61K8dEg7E6pYH7wH7wQhJHBYBHwOMIcZjo4ylYb7xtkw7kRhFRS5yFkiDoRonj58ElSyZoyGgiP1YTPyfFiFTjbgelaWdcRsY3gEA1iB8Igtr0fIOZWHYUNRXOWDMjtZRBTyo3iMARqFwtTyaLWBMjkLjQZylDi0Xi30vAaEOUi3ZKBYthxBBxZNvLzjXowkbvLljb0wUNIA1y9Y7qIfci1prsqRB8Yq3Y4hWHleqnw3Mjg5wkHWQ6KX0WgYnMIAcizvd8RmXY71YlbWAHeSOwZaj68w9DYMbKkoi5Y41wUPikFIzhRs3yHkiNoRfMjDNEazyz8ypfizsYMFyNti3Mytnv14xbwdYzyg5KZ5e01E5SjL1W5tWhNWB0YQhYSBYO4R5NYkgWtkYtMY8mYNcjXSe0hEnLWZLe05w15eBnj0sY30yn4Eo8jpDENsrg0j84wP0y3QxsjFNeNYdMRX0WHGW1zWHZWmzY8YLQWq9Ktpeb3vHDEoFWnpyPqjcJ38vAlEMZWoMytMjn8I1zj4w9YUpwpleGcwtZE39EtaElmRhDEgzrTkv3Mv5YF6jpTwfUyd4YlNEOoET3YXsYUqYosY0hIllxMg"
      }
   }
})
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
   'Content-Type': 'application/json',
   'Accept': '*/*',
   'Host': 'm.ctrip.com',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
