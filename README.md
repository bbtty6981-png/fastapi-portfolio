# FastAPI Portfolio

## 概要
FastAPI・Docker・AWS EC2 を使ったシンプルなポートフォリオ API です。
ローカル環境と EC2 どちらでも同じ手順で実行できるようにテンプレ化しています。

## ローカル起動手順（Docker）
```bash
docker build -t fastapi-app .
docker run -d -p 5001:5001 --name fastapi-container fastapi-app
```

## ローカル確認用URL
- http://localhost:5001/
- http://localhost:5001/items
- http://localhost:5001/docs

---

## EC2 デプロイ手順（Docker）
```bash
# EC2 に SSH 接続
ssh -i ~/Downloads/Tatsuya.pem ec2-user@3.26.7.18

# Docker ビルド & 起動
docker build -t fastapi-app .
docker run -d -p 5001:5001 --name fastapi-container fastapi-app

# ブラウザでアクセス
http://3.26.7.18:5001
```

## EC2 確認用URL（固定）
- http://3.26.7.18:5001/
- http://3.26.7.18:5001/items
- http://3.26.7.18:5001/docs

---

## 使用技術
- FastAPI
- Docker
- Uvicorn
- AWS EC2
