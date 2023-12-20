import pandas as pd
import json
import argparse


def csv_to_json(csv_file_path, json_file_path):
    df = pd.read_csv(csv_file_path, delimiter=';')
    json_data = {"titles": []}

    for index, row in df.iterrows():
        id_amedia = int(row["ID в Амедиатеке"]) if not pd.isna(row["ID в Амедиатеке"]) else None
        id_kp = int(row["ID на Кинопоиске"]) if not pd.isna(row["ID на Кинопоиске"]) else None

        title_data = {
            "id": id_amedia,
            "id_kp": id_kp,
            "ratings": [
                {
                    "kp_rating": str(row["Оценка Кинопоиск"]),
                    "imdb_rating": str(row["Оценка IMDB"])
                }
            ]
        }
        json_data["titles"].append(title_data)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON.')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('json_file', help='Path to the output JSON file')
    args = parser.parse_args()

    csv_to_json(args.csv_file, args.json_file)


if __name__ == '__main__':
    main()
