# Fishing_log
PythonとpostgreSQLを使った釣果記録表

PythonのtkinterとpostgreSQLの学習用に作成したプログラム
postgreSQLはローカルホストで使用しています。

main.py実行で釣果テーブルが表示されます。

「更新」ボタンクリックでデータベースに登録されている、
釣果情報を釣果テーブルに表示。
「登録」ボタンクリックで釣果入力フォームが表示され、
釣果情報を入力できます。
釣果入力フォームの「登録」ボタンをクリックすることで、
入力した釣果情報をデータベースに登録できます。

ディレクトリ構成
.
├── Fishing_log_app
│   ├── __init__.py
│   ├── __pycache__
│   ├── main_window.py・・・釣果テーブル画面に関するコード
│   ├── pgsql_method.py・・・DBへの登録、DBからの情報取得に関するコード
│   └── regist_window.py・・・釣果入力フォームに関するコード
├── README.md
├── __pycache__
├── main.py
├── venv
│   └── Pyenv_postgreSQL
└── デモ動画.mov・・・プログラムの操作している様子を撮影しました。
