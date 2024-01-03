## 本地开发
```bash
# 1
uvicorn main:app --reload

# 2
# python run.py
```

## 生产
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --log-config=./settings/log.json
```
