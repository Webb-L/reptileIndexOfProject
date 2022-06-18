# ReptileIndexOfProject

爬取Index Of网站中的所有链接。

## 使用

+ https://buildlogs.centos.org/centos/7/isos/

```bash
python3 main.py --url https://buildlogs.centos.org/centos/7/isos/ --parentNode table --startPosition 5
https://buildlogs.centos.org/centos/7/isos/aarch64/
https://buildlogs.centos.org/centos/7/isos/aarch64/BETA-NOT-FOR-PRODUCTION-CentOS-7-1503-20150511-aarch64.img.xz
...
https://buildlogs.centos.org/centos/7/isos/aarch64/sha1sum.txt
https://buildlogs.centos.org/centos/7/isos/armhfp/
...
https://buildlogs.centos.org/centos/7/isos/armhfp/readme.txt
https://buildlogs.centos.org/centos/7/isos/i386/
https://buildlogs.centos.org/centos/7/isos/i386/CentOS-7-i386-Beta-DVD-1503.iso
...
https://buildlogs.centos.org/centos/7/isos/i386/sha256sum.txt
https://buildlogs.centos.org/centos/7/isos/x86_64/
https://buildlogs.centos.org/centos/7/isos/x86_64/CentOS-7-live-GNOME-x86_64.iso
...
https://buildlogs.centos.org/centos/7/isos/x86_64/sha256sum.txt
```

+ https://old-releases.ubuntu.com/releases/ubuntu-server/

```bash
python3 main.py --url https://old-releases.ubuntu.com/releases/ubuntu-server/ --parentNode table --startPosition 4
https://old-releases.ubuntu.com/releases/ubuntu-server/5.10/
https://old-releases.ubuntu.com/releases/ubuntu-server/5.10/FOOTER.html
...
https://old-releases.ubuntu.com/releases/ubuntu-server/5.10/ubuntu-server-5.10-install-powerpc.template
https://old-releases.ubuntu.com/releases/ubuntu-server/FOOTER.html
https://old-releases.ubuntu.com/releases/ubuntu-server/HEADER.html
https://old-releases.ubuntu.com/releases/ubuntu-server/breezy/
https://old-releases.ubuntu.com/releases/ubuntu-server/breezy/FOOTER.html
...
https://old-releases.ubuntu.com/releases/ubuntu-server/breezy/ubuntu-server-5.10-install-powerpc.template
```

## 参数

```bash
usage: main.py [-h] [--url URL] [--parentNode PARENTNODE]
               [--startPosition STARTPOSITION]

爬取Index Of网站中的所有链接。

optional arguments:
  -h, --help            显示此帮助信息并退出。
  --url URL             需要爬取的网站。
  --parentNode PARENTNODE
                        父节点。默认：pre
  --startPosition STARTPOSITION
                        开始爬取位置。默认：1
```