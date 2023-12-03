# 使用 sg90 舵机控制 HP 1106 打印机开关

因为环境隔离，路由器需要控制舵机，而舵机又是通过 shell 控制，所以需要一个中间渠道，当前项目就是这个中间渠道。

简单流程是：openwrt 路由器发起请求 -> web -> sg90s.py

> sg90s.py 不会自动运行。 

## 背景
点击这里查看 -> [https://www.xingbaifang.com/archives/c5cce2b5-3e61-4ab3-bdb8-e6b5539f30a3](https://www.xingbaifang.com/archives/c5cce2b5-3e61-4ab3-bdb8-e6b5539f30a3)

## 部署环境
舵机需要 GPIO 控制，所以当前项目部署在「树莓派」里。


## 主要功能
* /alive 判断当前项目是否存活
* /go 启动舵机，内部调用 sg90s.py

## 开发
```
python -m venv .venv
. .venv/bin/activate
pip install .
pip install flask gunicorn
flask run --debug --port 7040
```

## 上线
```
sh run
```

## 其他：
* 项目基于 [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#)
* 推荐使用 python3
* 需要设置 sg90s.py 权限
   ```
  sudo chmod +x sg90s.py
  ```
* 检查当前端口是否占用
  ```
  # liunx
  netstat -nlp | grep 7040
  # mac
  lsof -P -i :7040
  ```
