import csv
import json
import os
import datetime
import argparse


def convert(input: str):
    print("start")

    if input == "lib":
        source_filename = "isil_libraries_20231031_J.csv"
        result_filename = "libraries.json"
    elif input == "lib_public":
        source_filename = "isil_libraries_public_20231031_J.csv"
        result_filename = "libraries_public.json"
    else:
        raise Exception("invalid argument: input")

    # データ読み込み
    result = []
    with open(os.path.join("../data/", source_filename), "r", encoding="utf-8") as f:
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
    with open(os.path.join("../results/", result_filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=str, default="lib", choices=["lib", "lib_public"]
    )
    arg = parser.parse_args()

    convert(arg.input)
