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


def writeXML(XML_string, fileName):
    with open(fileName, mode='w') as file:
        file.write(XML_string)


def waitAnswer(tmp, job, XML_Object):
    filename = 'Response.xml'
    queryStatus = 'ACT'
    attempt = 0
    while queryStatus == 'ACT':
        attempt += 1
        ans = tmp.GET(job)
        writeXML(ans.text, filename)
        XML_Object.setup()
        queryStatus = XML_Object.StatusCheck()
        if queryStatus != 'FIN':
            time.sleep(3)

        print('{status}…({attempt})'.format(
            status=queryStatus, attempt=attempt))

    print('-----------')
    XML_Object.GetEvents()
    return XML_Object


if __name__ == "__main__":

    file = '~/Downloads/analisis Block-malicious_ip.csv'
    filename = 'Response.xml'

    IP_List = loadCSV(file)

    tmp = pa.logsPaloAlto()
    XML_Object = ToCSV.toCSV(filename)

    for idx, ip in enumerate(IP_List):
        print('Progress:','{0:.2f}'.format(100*idx/len(IP_List)),'\b%')
        XML_Object = waitAnswer(tmp, tmp.POST(ip), XML_Object)
    XML_Object.SaveToCSV()
