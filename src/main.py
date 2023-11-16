import csv
import json
import datetime


def main():
    print("main")

    # データ読み込み
    result = []
    with open(
        "../data/isil_libraries_public_20231031_J.csv", "r", encoding="utf-8"
    ) as f:
        reader = csv.reader(f, delimiter=",")

        # 最初の行のヘッダーは飛ばす
        next(reader)

        # 変換
        for row in reader:
            result.append(
                {
                    "isil": row[0],
                    "name_jp": row[1],
                    "name_en": row[2],
                    "yomi": row[3],
                    "postal_code": row[4],
                    "prefecture": row[5],
                    "address1": row[6],
                    "address2": row[7],
                    "telephone_number": row[8],
                    "fax_number": row[9],
                    "url": row[10],
                    "former_isil": row[11],
                    "registered_at": row[12],
                    "updated_at": row[13],
                }
            )

    # 変換結果を保存
    now = datetime.datetime.now().isoformat()
    data = {"updated_at": now, "data": result}
    with open("../results/libraries_public.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("done")


if __name__ == "__main__":
    main()
