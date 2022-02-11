###########################################
#                                         #
#                                         #
#            callWebServer                #
#             version 0.1                 #
#                                         #
###########################################

import requests
import time
from random import randint

#Global variable to set for your project
baseURL = "http://192.168.256.256/"
urls = ["2022/02/10/hello-world", "sample-page", "wp-login.php", "page404.html"]

def call(url):
    """
        Send get request to the URL pass in parameter.
        Return the status code.
    """
    try :
        response=requests.get(url)
        return response.status_code
    except :
        print("Unable to reach {}".format(baseURL))

def main() :
    """Script execution
    """    
    requestsNumber = 10
    for url in urls:
        for x in range(requestsNumber):
            call(baseURL + url)
        requestsNumber += 10
        

    print("infinity")
    while True:
        value = randint(0, len(urls)-1)
        call(baseURL + urls[value])


#Main
main()