# finxOS

开源在线数据平台，通过简单易用的API方式使用

## install

### 1. 通过一键安装脚本安装(推荐)

```shell
python onekey_install_finxos.py
```

### 2. 直接从pypi上安装

```shell
pip install finxos
```

需要注意的是，python-snappy这个包在Windows上的安装需要比较多的编译依赖,建议从[这个网页](http://www.lfd.uci.edu/~gohlke/pythonlibs)下载编译好的包，然后安装:

```shell
pip install python_snappy-0.5.1-cp27-cp27m-win_amd64.whl
```

### 3. 下载源代码，运行下面的命令：

```shell
python setup.py install
```

## 快速使用

```python
from finxos.data import DataApi 

api = DataApi(addr="tcp://data.quantos.org:8910")
result, msg = api.login("phone", "token") # 示例账户，用户需要改为自己在www.quantos.org上注册的账户
print(result)
print(msg)

df, msg = api.daily('000002.SZ', 20180101, 20180801)
print(df)
print(msg)

```
