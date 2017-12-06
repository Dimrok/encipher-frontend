import requests
import sys
import time
url = sys.argv[1]

# Check connection.
while True:
  try:
    print("try to contact", url)
    requests.get(url).raise_for_status()
    break
  except:
    time.sleep(0.5)
    pass

expected = ["modulus:", "publicExponent:", "privateExponent:", "prime1:", "prime2:", "exponent1:", "exponent2:", "coefficient:"]

body = requests.get(url)
body.raise_for_status()
body = body.text
for expectation in expected:
  assert expectation not in body

body = requests.get(url + '?payload=castor')
body.raise_for_status()
body = body.text
for expectation in expected:
  assert expectation in body
assert "00:c7:34:59:9b:10:69:30:4c:3c:41:4f:f8:b2:85:" in body
assert "01:96:d9:c0:c9:84:a2:a2:90:f2:2b:20:27:75:70:" in body
assert "75:5b:2c:fb:a4:58:41:58:35:cd:ef:b9:2f:c3:82:" in body
