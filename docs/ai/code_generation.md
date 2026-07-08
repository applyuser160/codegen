# コード生成 (Code Generation)

## datamodel-code-generator の利用
- `datamodel-code-generator` を使用し、Python環境の `sys.executable` 経由で実行する構成となっています。
- OpenAPIやJSON Schemaなどのモデル定義から自動的にデータモデルを生成します。

## Entity Generator の仕様
- **フォーマット対応**: JSONのサポート、配列型の対応、`$ref` (他モデルの参照)、NULL許容型に対応しています。
- **インポートとファイルパス**: 他のモデルを参照する際、クロスモデルインポートパスには `snake_case` を使用します。
- **テンプレートエンジン**: `Jinja2` を導入して、コードの出力テンプレートを管理しています。
- **基底クラス**: `Base` エンティティを定義し、各モデルがそれを継承する仕組みを整えています。
