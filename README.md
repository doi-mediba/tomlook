# shiromane groups.conf用 チェッカー

2つのshiromane groups.confファイル内に記載された各Groupに含まれるUserが完全一致しているかを確認するスクリプト

# 環境

- python 3.6.1
- toml 0.9.2

# 使い方

```
#クローンする
git clone git@github.com:mediba-system/tomlook.git
```

TOMLをパースするためのpythonライブラリが必要なので下記のようにコマンドを実行する。

    # ライブラリのインストール
    cd tomlook
    % pip install -r requirements.txt
    
    # 使用方法
    % python main.py toml_file_a toml_file_b

片方のファイルだけユーザがいない（またはいる）場合、実行するとFailedと表示され、存在しないユーザを表示する。
