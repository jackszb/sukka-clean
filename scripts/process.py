import requests
import json

URLS = [
    ("https://raw.githubusercontent.com/jackszb/pure-sukka-rules/main/reject_rules.json", "reject-I.json"),
    ("https://raw.githubusercontent.com/jackszb/sukka-json/main/non_ip/reject.json", "reject-II.json"),
]


def process_rules(data):
    # 修改 version
    data["version"] = 3

    # 处理 rules
    for rule in data.get("rules", []):
        if "ip_cidr" in rule:
            del rule["ip_cidr"]

    return data


def main():
    for url, filename in URLS:
        print(f"Downloading: {url}")
        res = requests.get(url)
        res.raise_for_status()

        data = res.json()
        new_data = process_rules(data)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)

        print(f"Saved: {filename}")


if __name__ == "__main__":
    main()
