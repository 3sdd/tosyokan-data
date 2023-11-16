
# 図書館データ




## 実行方法

公共図書館以外のデータを変換
```bash
docker compose run script --input=lib
```

公共図書館のデータを変換
```bash
docker compose run script --input=lib_public
```



dockerビルド。

```bash
docker build --tag 'my-tosyokan-data-converter' .
```

変換の実行。
```bash
docker run my-tosyokan-data-converter
```


## データ

`data`フォルダーに以下から取得した図書館データ（ISIL管理台帳ファイル（2023年10月31日現在））のcsvファイルを配置している。
データは2023/11/16にダウンロードした。

ソース: https://www.ndl.go.jp/jp/library/isil/index.html#list


- 公共図書館: `isil_libraries_public_20231031_J.csv`
- 公共図書館以外: `isil_libraries_20231031_J.csv`


## 変換結果

address1,address2の名前は変更するかもしれない。

```json
{
    "isil": "ISIL",
    "name_jp": "図書館名(日本語)",
    "name_en": "図書館名(英語)",
    "postal_code":"郵便番号",
    "prefecture":"図書館所在地の都道府県",
    "address1": "市区町村",
    "address2": "町名番地",
    "telephone_number":"電話番号",
    "fax_number":"代表FAX番号",
    "url": "URL",
    "registered_at":"登録日",
    "updated_at":"更新日"
}

```