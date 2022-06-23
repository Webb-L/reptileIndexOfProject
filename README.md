# ReptileIndexOfProject

爬取Index Of网站中的所有链接。

## 使用

### CentOS Index of

> https://buildlogs.centos.org/centos/7/isos/

```bash
python3 main.py --url https://buildlogs.centos.org/centos/7/isos/ --parentNode table --childStartPosition 5
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
https://buildlogs.centos.org/centos/7/isos/x86_64/
https://buildlogs.centos.org/centos/7/isos/x86_64/CentOS-7-live-GNOME-x86_64.iso
...
https://buildlogs.centos.org/centos/7/isos/x86_64/sha256sum.txt
```

### Ubuntu Index of

> https://old-releases.ubuntu.com/releases/ubuntu-server/

```bash
python3 main.py --url https://old-releases.ubuntu.com/releases/ubuntu-server/ --parentNode table --childStartPosition 4
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

### Qt Index of

> https://download.qt.io/archive/qt/6.3/

+ 输出所有文件。

```bash
python3 main.py --url https://download.qt.io/archive/qt/6.3/ --parentNode table --childStartPosition 4 --type file
https://download.qt.io/archive/qt/6.3/6.3.1/submodules/qtwebview-everywhere-src-6.3.1.zip
https://download.qt.io/archive/qt/6.3/6.3.1/submodules/qtwebview-everywhere-src-6.3.1.zip.mirrorlist
https://download.qt.io/archive/qt/6.3/6.3.1/submodules/qtwebview-everywhere-src-6.3.1.tar.xz
...
https://download.qt.io/archive/qt/6.3/6.3.0/OFFLINE_README.txt.mirrorlist
https://download.qt.io/archive/qt/6.3/CVE-2018-25032-qtbase-6.3.diff
https://download.qt.io/archive/qt/6.3/CVE-2018-25032-qtbase-6.3.diff.mirrorlist
```

+ 输出所有目录。

```bash
python3 main.py --url https://download.qt.io/archive/qt/6.3/ --parentNode table --childStartPosition 4 --type dir
https://download.qt.io/archive/qt/6.3/6.3.1/
https://download.qt.io/archive/qt/6.3/6.3.1/submodules/
https://download.qt.io/archive/qt/6.3/6.3.1/single/
https://download.qt.io/archive/qt/6.3/6.3.0/
https://download.qt.io/archive/qt/6.3/6.3.0/submodules/
https://download.qt.io/archive/qt/6.3/6.3.0/single/
```

## 参数

```bash
python3 main.py
usage: main.py [-h] [--url URL] [--parentNode PARENTNODE]
               [--parentStartPosition PARENTSTARTPOSITION]
               [--childStartPosition CHILDSTARTPOSITION] [--type TYPE]

爬取Index Of网站中的所有链接。

optional arguments:
  -h, --help            显示此帮助信息并退出。
  --url URL             需要爬取的网站。
  --parentNode PARENTNODE
                        父节点。默认：pre
  --parentStartPosition PARENTSTARTPOSITION
                        父节点开始抓取位置。默认： 0
  --childStartPosition CHILDSTARTPOSITION
                        子节点开始抓取位置。默认： 1
  --type TYPE           输出网址类型。类型：all|dir|file 默认值：all
```