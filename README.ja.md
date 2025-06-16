# fujielab-util-launcher

Multiple Program Launcher Utility

[English README](README.md)

## 使用方法

### コマンドライン引数

```
python -m fujielab.util.launcher.run [オプション]
```
または
```
fujielab-launcher [オプション]
```

#### オプション

- `-d`, `--debug`: デバッグモードを有効にします。詳細なログメッセージが表示されます。
- `--reset-config`: 設定ファイルを初期化します。既存の設定は上書きされます。
- `--version`: バージョン情報を表示して終了します。
- `-h`, `--help`: ヘルプメッセージを表示して終了します。

### デバッグモード

デバッグモードでは、アプリケーションの動作に関する詳細な情報が表示されます。
設定ファイルの保存・読み込み、ウィンドウの状態変更、プロセスの起動・停止などの操作について
詳細なログが出力されます。

開発やトラブルシューティングの際に便利です。通常の使用時には必要ありません。

```bash
# デバッグモードで起動
python -m fujielab.util.launcher.run -d
```

または

```bash
python -m fujielab.util.launcher.run --debug
```

## 機能

- 設定可能な複数プログラムランチャー
- Pythonスクリプトやシェルコマンドのサポート
- カスタマイズ可能なワークスペースディレクトリ設定
- クロスプラットフォーム対応（Windows、macOS、Linux）

## インストール方法

### PyPIから

```bash
pip install fujielab-util-launcher
```

### ソースから

```bash
git clone https://github.com/fujielab/fujielab-util-launcher.git
cd fujielab-util-launcher
pip install -e .
```

## ライセンス

Apache License 2.0
