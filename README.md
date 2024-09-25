# 使用 sg90 舵机控制 HP 1106 打印机开关

大致流程是：路由器 -> 舵机 HTTP 服务 -> 执行 shell 脚本（sg90s.py） -> 舵机

本项目包含：HTTP 服务 + 舵机控制脚本。

> sg90s.py 不会自动运行，对外需要通过 WEB 服务来调用。

## 背景

家里打印机由于停电或者其他原因会中断与路由器的连接，导致打印文件时，没有反应，还得手动去重启打印机来解决，虽然出现这种情况不是很多，但是家人解决起来还是得靠口头指挥，非常不方便。

这种情况发生过几次，就考虑能否通过程序来检测打印机状态，一旦检测掉线，就让打印机重启。

详细介绍点击这里 -> [https://www.xingbaifang.com/archives/60a18c56-e0ea-4796-bde7-51bd998a2ef5](https://www.xingbaifang.com/archives/60a18c56-e0ea-4796-bde7-51bd998a2ef5)

## 部署环境

舵机需要 GPIO 控制，所以部署在「树莓派」里。

## 主要功能

* /alive 判断当前 WEB 服务是否存活
* /go 启动舵机，内部调用 sg90s.py

## 最终成果

![result](https://static.ca01.cn/2024/09/1727230881891-WechatIMG347.jpg)

## 开发

```shell
python -m venv .venv
. .venv/bin/activate
pip install .
pip install flask gunicorn
flask run --debug --port 7040
```

## 上线

```shell
sh run
```

## 其他

* 项目基于 [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#)
* 推荐使用 python3
* 需要设置 sg90s.py 权限
  
  ```shell
  sudo chmod +x sg90s.py
  ```

* 检查当前端口是否占用

  ```shell
    # liunx
    netstat -nlp | grep 7040
    # mac
    lsof -P -i :7040
  ```
