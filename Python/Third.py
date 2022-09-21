from urllib import response
import numpy as np
import requests

P=np.array([1,2,3,4])
print(np.shape(P))
print(np.version.version)
response=requests.get("http://randomfox.ca/floof")
print(response.status_code)