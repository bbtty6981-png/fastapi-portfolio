# FastAPI Portfolio

## 概要
FastAPI, Docker, AWS EC2 を使ったポートフォリオAPIです。

## ローカル起動方法

docker build -t fastapi-app .
docker run -d -p 5001:5001 --name fastapi-container fastapi-app

## EC2 デプロイ手順
EC2 へ SSH 接続
Docker イメージを配置
起動コマンドを実行
ブラウザで http://<EC2のIP>:5001 にアクセス
