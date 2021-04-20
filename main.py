import os
import json
import requests


def main():
    appid = os.environ["INPUT_APPID"]
    appkey = os.environ["INPUT_APPKEY"]
    mod_id = os.environ["INPUT_MOD_ID"]
    mod_tiile = os.environ["INPUT_MOD_TITLE"]
    mod_tags = os.environ["INPUT_MOD_TAGS"]
    mod_version = os.environ["INPUT_MOD_VERSION"]
    mod_desc = os.environ["INPUT_MOD_DESC"]
    mod_content = os.environ["INPUT_MOD_CONTENT"]

    mod = {
        "id": mod_id,
        "mods_title": mod_tiile,
        "mods_key": mod_tags,
        "mods_version": mod_version,
        "mods_desc": mod_desc,
        "mods_content": ""
    }

    if mod_content != "":
        markdown_file = open(mod_content, "r", encoding="UTF-8")
        lines = markdown_file.readlines()
        markdown_file.close()
        md_str = "".join(lines)
        mod["mods_content"] = md_str

    mod = json.dumps(mod)

    values = {
        "APPID": appid,
        "APPKEY": appkey,
        "mod": mod
    }

    url = "https://mod.3dmgame.com/api/UpModData"

    res = requests.post(url, data=values)

    print(f"::set-output name=RESPONSE::{res.text}")


if __name__ == "__main__":
    main()
