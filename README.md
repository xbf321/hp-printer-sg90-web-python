# 

## 需要设置 sg90s.py 权限

```
sudo chmod +x sg90s.py
```

## 地址被占用


```
# liunx
netstat -nlp | grep 7040
# mac
lsof -P -i :7040
```

## Dev

```
flask run --debug --port 7040
```

## 生产环境

```
gunicorn app:app -c gunicorn.conf.py
```