# fujielab-util-launcher

Multiple Program Launcher Utility

[English README](README.md)

## 使用方法

### 実行方法

```
fujielab-launcher [オプション]
```

#### オプション

- `-d`, `--debug`: デバッグモードを有効にします。詳細なログメッセージが表示されます。
- `-r`, `--reset-config`: 前回利用時に自動的に保存された設定を初期化してランチャのない状態から開始します。
- `-c`, `--config`: 過去にエクスポートされた設定ファイルをインポートした状態で起動します。
- `--version`: バージョン情報を表示して終了します。
- `--lang`: UIの言語を指定します (`en` または `ja`)。省略した場合はシステムのロ
  ケールに従います。
- `-h`, `--help`: ヘルプメッセージを表示して終了します。

### デバッグモード

デバッグモードでは、アプリケーションの動作に関する詳細な情報が表示されます。
設定ファイルの保存・読み込み、ウィンドウの状態変更、プロセスの起動・停止などの操作について
詳細なログが出力されます。

開発やトラブルシューティングの際に便利です。通常の使用時には必要ありません。

```bash
# デバッグモードで起動
fujielab-launcher  -d
```

### カスタム設定ファイルの使用

過去にエクスポートした設定ファイルの状態で起動するには、`-c`または`--config`オプションを使用します。

```bash
fujielab-launcher --config /path/to/your/custom_config.yaml
```

これは異なる設定プロファイル間を切り替えたり、別のシステムから設定をインポートする場合に便利です。

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
