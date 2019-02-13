import requests
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


    def POST(self, IpAddr, printAns=False):
        self.querystring = {"type":"log","log-type":"traffic","query":"( addr in {} )".format(IpAddr)}
        ans = requests.request("GET", self.url, data=self.payload, headers=self.headers, params=self.querystring, verify=False)
        self.response = ans.text

        if printAns:
            print(self.response)

        self.job = self.getJobID()
        print('Done posting…')
        return self.job


    def getJobID(self):
        try:
            ans = self.response.split('</line>')[0].split(' ')[-1]
        except:
            print("Couldn't get response. Please check log")
            ans=''
        return ans
    def GET(self,jobID):
        self.querystring = {"type":"log","action":"get","job-id":jobID}
        ans = requests.request("GET", self.url, data=self.payload, headers=self.headers, params=self.querystring, verify=False)
        self.response = ans.text
        return ans

if __name__ == "__main__":
    tmp = logsPaloAlto()
    job = tmp.POST('68.183.70.42')
    ans = tmp.GET(job)
    print(ans.text)