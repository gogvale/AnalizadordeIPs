import logsPaloAlto as pa

import pandas as pd
import os
import sys
import time


def loadCSV(file):
    df_IPs_Cheo = pd.read_csv(os.path.expanduser(file))
    testing_IPs = df_IPs_Cheo['X_Forwarded_For']
    testing_IPs_list = testing_IPs.to_list()
    return testing_IPs_list


if __name__ == "__main__":

    file = '~/Downloads/analisis Block-malicious_ip.csv'
    IP_List = loadCSV(file)

    tmp = pa.logsPaloAlto()
    jobList = []

    for ip in IP_List:
        jobList.append(tmp.POST(ip))

    for job in jobList:

        queryStatus = 'ACT'
        attempt = 0
        while queryStatus is 'ACT':
            attempt += 1
            ans = tmp.GET(job)
            queryStatus = edsonClass.getStatus(
                ans)  # TODO: Poner clase de Edson

            if queryStatus is 'ACT':
                time.sleep(3)

            print('{status}…({attempt})'.format(
                status=queryStatus, attempt=attempt), end='\r')
