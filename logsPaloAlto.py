import requests
import sys
import xml.etree.cElementTree as et
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class logsPaloAlto():
    
    def __init__(self , serverIpAddr='10.4.29.121'):
        self.setup(serverIpAddr)


    def setup(self , serverIpAddr):
        self.serverIpAddr = serverIpAddr
        self.payload = ""
        self.headers = {
                'key': "LUFRPT1FMkhtM1Y2empPZFFuaE95anFDTmpvTGFjZXc9Y1hyeGlWdXpJUXFSRW81cy9DczVmaC9IUjVLZG9kc0VZZzBDQlYyQ05paz0=",
                'Authorization': "Basic ZWxveWE6TWNwbHVzMTEzYWRtIW4=",
                'cache-control': "no-cache",
                'Postman-Token': "a456d01a-989d-460f-9ef3-4834561f2917"
        }
        self.url = "https://{}/api/".format(self.serverIpAddr)
        print('Setup finished…')


    def POST(self, IpAddr):
        """Asks Palo Alto for a query and returns a job #"""
        self.querystring = {"type":"log","log-type":"traffic","query":"( addr in {} )".format(IpAddr)}
        ans = requests.request("GET", self.url, data=self.payload, headers=self.headers, params=self.querystring, verify=False)
        self.response = ans
        print('Done posting…')

        self.job = self.getJobID()
        return self.job


    def getJobID(self):
        try:
            ans = et.fromstring(self.response.content).getchildren()[0].findtext('job')
            print('Job:',ans)
        except:
            print("Couldn't get response. Please check log")
            ans=''
        return ans

        
    def GET(self,jobID):
        """Gets response from jobID"""
        self.querystring = {"type":"log","action":"get","job-id":jobID}
        ans = requests.request("GET", self.url, data=self.payload, headers=self.headers, params=self.querystring, verify=False)
        self.response = ans
        return ans
    
def main(ip=''):
    
    tmp = logsPaloAlto()

    if len(sys.argv) >= 2:
        ip = sys.argv[1]
    elif ip is not '':
        ip = ip
    else:
        ip = '68.183.70.42'
    
    tmp.POST(ip)

    ans = tmp.GET(tmp.job)
    
    print(ans.text)

if __name__ == "__main__":
    main()

