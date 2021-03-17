import json

jsonStr = """
{
  "name": "Rashmi",
  "email": "rashmi@email.com",
  "addresses": [
    {
      "type": "residential",
      "street name": "bab",
      "city": "bab"
    },
    {
      "type": "Official",
      "street name": "ffsf",
      "city": "dfsdf"
    }
    ]
}"""

jsonObj = json.loads(jsonStr)

print(jsonObj["name"])
print(jsonObj["email"])
print(jsonObj["addresses"][0]["type"])

