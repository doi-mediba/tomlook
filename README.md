# groups.conf チェッカー

2つのTOMLファイル内に記載された各Groupに含まれるUserが完全一致しているかを確認するスクリプト

# 使い方

- git cloneでローカルに持ってくる

    cd checktoml
    python main.py toml_file_a toml_file_b

- 片方のファイルだけユーザがいない（またはいる）場合、実行するとFailedと表示され、存在しないユーザを表示する。
