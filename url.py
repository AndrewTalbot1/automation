import requests
urls = requests.get(
    "http://www.python.org",
    "www.google.com"
    )
try:
    urls.raise_for_status()
except Exception as error:
    print('There was a problem: %s' % (error))
else:
    print('All The urls work')





