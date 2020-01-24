import requests
urls = requests.get("http://www.python.org/no_page")
try:
    urls.raise_for_status()
except Exception as error:
    print('There was a problem: %s' % (error))
else:
    print('All The urls work')





