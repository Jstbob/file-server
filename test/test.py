import requests,datetime, time
# from urllib3 import encode_multipart_formdata

url='http://127.0.0.1:5000/u/upload'

def upload_file(file_path, url=url):
    files = {'file':open(file_path, "rb")}
    r = requests.post(url, files=files)
    print(r.json())
    return r.json()

def download(url):
    r=requests.get(url).content
    with open(url.split('/')[-1],'wb') as f:
        f.write(r)

def getDate(url):
    r=requests.post(url)
    print('date:',r.text,'!!',sep='')

def getUTCDate(url):
    r=requests.post(url)
    str=r.text
    print('UTCdate',str)
    time2 = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
    time3 = time.mktime(time2.timetuple())
    print(time3)
    time4 = int(time3)
    print(time4)

def test_flow(file):
    path=upload_file(file)['url']
    download(path)
    getDate('http://127.0.0.1:5000/u/getDate')
    getUTCDate('http://127.0.0.1:5000/u/getUTCDate')

if __name__ == '__main__':
    from threading import Thread
    for i in range(1,6):
        t=Thread(target=test_flow,args=(str(i),))
        t.start()