import re

regex = r"^((?!api).)*$"

# Test the regex on a sample URL
url = "https://www.example.com/asdfasd/askdf"

if re.match(regex, url):
  print("URL matches the regex")
else:
  print("URL does not match the regex")
