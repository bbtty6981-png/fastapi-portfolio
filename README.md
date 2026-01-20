# FastAPI CRUD Portfolio API  
Docker + FastAPI + PostgreSQL

本リポジトリは、FastAPI / Docker Compose / PostgreSQL を使用した  
**実務レベルの CRUD API システム** です。  
副業・案件対応用のポートフォリオとして作成しています。

---

## 🚀 機能一覧（Items テーブル CRUD）

| メソッド | エンドポイント          | 内容       |
|---------|---------------------------|------------|
| GET     | `/items/`                 | 全データ取得 |
| POST    | `/items/`                 | 新規作成 |
| GET     | `/items/{item_id}`        | 1件取得 |
| PUT     | `/items/{item_id}`        | 更新 |
| DELETE  | `/items/{item_id}`        | 削除 |

---

## 🧱 技術構成

- FastAPI  
- PostgreSQL 15  
- SQLAlchemy  
- Docker / Docker Compose  
- Uvicorn  
- Swagger UI  

---

## 📦 ディレクトリ構成

```
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── api/
│   └── items.py
└── routers/
    └── items.py
docker-compose.yml
Dockerfile
requirements.txt
```

---

## 🔧 実行方法（Docker Compose）

### 1. 起動
```bash
docker-compose up --build -d
```

### 2. 停止
```bash
docker-compose down
```

---

## 🌐 API 動作確認

起動後、自動的に Swagger UI が有効になります。

👉 http://localhost:8000/docs

---

## 🗄️ データ永続化（PostgreSQL）

```
volumes:
  postgres_data:
    driver: local
```

Docker コンテナを停止しても DB データが保持されます。

---

## 🎯 ポートフォリオとしての狙い

- FastAPI + Docker の **実務 API 実装力** を示す  
- ORM / ルータ分割 / DB 永続化など **案件で必要な構成を再現**  
- 商品管理 API としてすぐ使える仕様  

---

## 📩 応募コメント例

「FastAPI / Docker / PostgreSQL を用いた CRUD API 開発経験があります。  
本ポートフォリオでは、商品管理 API（Items CRUD）を実装し、DB 永続化・DockerCompose で本番構成を再現しています。」

---

# 🔧 GitHub 反映手順（bbtty6981-png 用）

```bash
cd ~/Desktop/fastapi-portfolio

git init
git add .
git commit -m "Initial commit - FastAPI CRUD Portfolio"

git branch -M main
git remote add origin https://github.com/bbtty6981-png/fastapi-portfolio.git
git push -u origin main
```

---

# 🔍 DB 永続化チェック手順

1. Swagger → GET `/items/`  
   現在の件数を確認

2. Docker 停止  
```bash
docker-compose down
```

3. 再起動  
```bash
docker-compose up -d
```

4. 再度 GET `/items/`  
   → 同じデータが残っていれば **永続化成功**
