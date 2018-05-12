# Mac 下安装 PIL

## 链接

<https://stackoverflow.com/questions/9070074/how-can-i-install-pil-on-mac-os-x-10-7-2-lion>

## 命令

```bash

# download

curl -O -L <http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz>

# extract

tar -xzf Imaging-1.1.7.tar.gz cd Imaging-1.1.7

# build and install

python setup.py build sudo python setup.py install

# or install it for just you without requiring admin permissions:

# python setup.py install --user
```
