#! python3
import bs4
import urllib.request
import sys,os,time
from urllib.error import HTTPError, URLError

def parse_html(html):
    #if b'https://' or b'http://' in html:
    #    print('found url address')
    #    offset = html.find(b'https://')
    #    #print(offset)
    #    while offset != -1:
    #        print(offset)
    #        print(html[offset:offset+10])
    #        #find next
    #        offset = html.find(b'https://', offset+10)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    processed_pages = 1
    for tags in soup.find_all('a'):
        processed_pages += 1
        print("Processing #%i page \'%s\'"%(processed_pages,(tags['href'])))
        try:
            with urllib.request.urlopen(tags.get('href')) as handle2:
                html2 = handle2.read()
            lst = str(time.time()).split('.')
            file_name = 'FIL'+lst[0]+'.htm'
            with open(file_name, 'wb+') as f:
                f.write(html2)
            #replace_file = 'file:///' +os.getcwd() +file_name
            #tags['href'] = replace_file
        except (ValueError, HTTPError, URLError):
            print("This webpage broken!")
            pass

lst = str(time.time()).split('.')
dir_name = 'DIR'+lst[0]
os.mkdir(dir_name)
work_dir = os.getcwd()
os.chdir(dir_name)
with urllib.request.urlopen(sys.argv[1]) as handle:
    html = handle.read()
##parse root url for subsequence urls@
parse_html(html)
weburl = sys.argv[1].split('.')
filename = weburl[1]+'.htm'
with open(filename, 'wb+') as f:
    f.write(html)
os.chdir(work_dir)