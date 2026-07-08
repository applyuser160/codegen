# 開発ガイド (Development Guide)

## 開発環境・ツール
- **依存関係管理**: 本プロジェクトでは依存関係の管理に `pyproject.toml` を使用しています。
- **対応バージョン**: Python 3.12 以上の環境が必要です。

## テストの実行方法
プロジェクト内のテスト（特に `codegen` 周り）を正常に実行するためには、適切なパスの設定が必要です。以下のコマンドを用いてテストを実行してください。

```bash
cd codegen && PYTHONPATH=src python -m pytest tests/
```
- `codegen` ディレクトリに移動してから実行します。
- 環境変数 `PYTHONPATH` に `src` ディレクトリを含めることで、モジュールの解決エラーを防ぎます。
