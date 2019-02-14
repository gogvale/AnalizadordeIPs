import logsPaloAlto as pa

import pandas as pd
import os
import sys


def loadCSV(file):
    df_IPs_Cheo = pd.read_csv(os.path.expanduser(file))
    testing_IPs = df_IPs_Cheo['X_Forwarded_For']
    testing_IPs_list = testing_IPs.to_list()
    return testing_IPs_list
    

if __name__ == "__main__":
    # file = sys.argv[1]
    file = '/home/gabriel/Downloads/analisis Block-malicious_ip.csv'
    IP_List = loadCSV(file)

    tmp = pa.logsPaloAlto()
    jobList = []

    for ip in IP_List:
        jobList.append(tmp.POST(ip))
    
    