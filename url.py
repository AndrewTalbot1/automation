import requests
with open ("testurls.txt", "r") as txt_file:
    for urls in txt_file:
        request = requests.get(urls)
        try:
            request.raise_for_status()
        except Exception as error:
            print('There was a problem: %s' % (error))
        else:
            print('This url works:' + ' ' + urls)


'''
urls_list = [
    "http://www.python.org/no_page_found",
    "http://www.youtube.com",
    "http://www.facebook.com",
    "http://www.baidu.com",
    "http://www.yahoo.com",
]
for urls in urls_list:
    #print(urls)
    request = requests.get(urls)
    try:
        request.raise_for_status()
    except Exception as error:
        print('There was a problem: %s' % (error))
    else:
        print('This url works:'+' ' + urls)
'''