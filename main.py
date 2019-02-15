import logsPaloAlto as pa
import ToCSV
import pandas as pd
import os
import sys
import time


def loadCSV(file):
    df_IPs_Cheo = pd.read_csv(os.path.expanduser(file))
    testing_IPs = df_IPs_Cheo['X_Forwarded_For']
    testing_IPs_list = testing_IPs.to_list()
    return testing_IPs_list
def writeXML(XML_string,fileName):
    with open(fileName,mode='w') as file:
        file.write(XML_string)
def waitAnswer(tmp, job):
    filename = 'Response.xml'
    queryStatus = 'ACT'
    attempt = 0
    while queryStatus == 'ACT':
        
        attempt += 1
        ans = tmp.GET(job)
        writeXML(ans.text,filename)
        XML_Object = ToCSV.toCSV(filename)
        queryStatus = XML_Object.StatusCheck()
        if queryStatus != 'FIN':
            time.sleep(3)

        print('{status}…({attempt})'.format(
            status=queryStatus, attempt=attempt), end='\r')

    print('Query finished.')
    print(ans.text)
    
if __name__ == "__main__":

    file = '~/Downloads/analisis Block-malicious_ip.csv'
    IP_List = loadCSV(file)

    tmp = pa.logsPaloAlto()

    for ip in IP_List:
        waitAnswer(tmp, tmp.POST(ip))