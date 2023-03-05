# ブロックチェーン (Python)

## 概要
- ブロックチェーンの学習用プロジェクト。

## 学んだこと
- ブロックチェーン及び Proof of Work の仕組み。
- ブロックチェーンの実装方法。
- Flask の使い方。

## 参考資料
- https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
- https://qiita.com/hidehiro98/items/841ece65d896aeaa8a2a

## 環境構築手順
1. python3 系と pipenv をインストールする。
2. 必要なライブラリをインポートする。
   ```sh
   pipenv install
   ```

## サーバー起動手順
1. 仮想環境を起動する。
   ```sh
   pipenv shell
   ```
2. サーバー1を起動する。
   ```sh
   python3 -m server 5000
   ```
3. 別ターミナルでサーバー2を起動する。
   ```sh
   pipenv shell
   python3 -m server 5001
   ```

## 使い方
```sh
# トランザクションを生成する。
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"

# マイニングを実行する。
curl "http://localhost:5000/mine"

# チェーンを確認する。
curl "http://localhost:5000/chain"

# サーバー1にサーバー2を登録する。
curl -X POST -H "Content-Type: application/json" -d '{
   "nodes": ["http://localhost:5001"]
}' "http://localhost:5000/nodes/register"

# サーバー2でマイニングを実行する。
curl "http://localhost:5001/mine"
curl "http://localhost:5001/mine"
curl "http://localhost:5001/mine"

# サーバー1のチェーンをサーバー2のチェーンに置き換える(コンセンサス)。
curl "http://localhost:5000/nodes/resolve"

# サーバー1のチェーンがサーバー2のチェーンに置き換わっていることを確認する。
curl "http://localhost:5000/chain"
```
