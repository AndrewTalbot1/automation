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
