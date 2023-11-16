
# 図書館データ




## 実行方法

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
