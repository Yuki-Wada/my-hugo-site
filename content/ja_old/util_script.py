import os
import datetime
import shutil
import glob
import re

REPLACE_DIR_PATH = "./content/ja/docs/"

SETTING_YAML_TEMPLATE = """---
title: '{title}'
description: '{title}'
date: '{date}'
categories: []
weight: {weight}
math: true
---

"""

def replace_md_file(src_file_md_path, dst_file_md_path):
    def split_config_and_content(file_content):
        yaml_config = ""
        content = ""

        flag = "TextHead"
        for raw_line in file_content.splitlines():
            raw_line += "\n"
            line = raw_line.strip()
            if flag == "TextHead":
                if line == "---":
                    flag = "InYaml"
                elif not line:
                    pass
                else:
                    flag = "InContent"
            elif flag == "InYaml":
                if line == "---":
                    flag = "InContent"
                elif not line:
                    pass
                else:
                    yaml_config += raw_line
            elif flag == "InContent":
                content += raw_line
            else:
                raise ValueError()

        return yaml_config, content


    def escape_underbar(code):
        code = re.sub(r"_", " _ ", code)
        return code

    def convert_inline(src):
        replaced_inline_text = ""
        while True:
            match = re.search(r"\$[^$]+?\$", src, flags=re.DOTALL)
            if match is None:
                break
            start, end = match.span()

            raw_text = src[:start]
            equation_text = src[start + 1:end - 1]
            src = src[end:]

            equation_text = escape_underbar(equation_text)
            replaced_inline_text += raw_text
            replaced_inline_text += r"\\(" + equation_text + r"\\)"

        replaced_inline_text += src

        return replaced_inline_text

    def convert_block(src):
        src_block_text = re.sub(r"\n", " ", src[2:-2])
        if not src_block_text.strip().startswith(r"\begin"):
            src_block_text = r" \begin{aligned} " + src_block_text + r" \end{aligned} " 
        src_block_text = escape_underbar(src_block_text)
        return r"\\[" + re.sub(r"\\", r"\\\\", src_block_text) + r"\\]"

    with open(src_file_md_path, "r", encoding="utf8") as f:
        file_content = f.read()
        src_yaml_config, src_text = split_config_and_content(file_content)

    replaced_content = ""
    while True:
        match = re.search(r"\$\$[^$]+?\$\$", src_text, flags=re.DOTALL)
        if match is None:
            break
        start, end = match.span()

        inline_text = src_text[:start]
        block_text = src_text[start:end]
        src_text = src_text[end:]

        replaced_content += convert_inline(inline_text)
        replaced_content += convert_block(block_text)

    replaced_content += convert_inline(src_text)

    dst_yaml_config = ""
    if os.path.exists(dst_file_md_path):
        with open(dst_file_md_path, "r", encoding="utf8") as f:
            file_content = f.read()
            dst_yaml_config, _ = split_config_and_content(file_content)

    replaced_file_content = ""
    replaced_file_content += "---\n"
    if dst_yaml_config:
        replaced_file_content += dst_yaml_config
    else:
        replaced_file_content += src_yaml_config
    replaced_file_content += "---\n"
    replaced_file_content += replaced_content

    with open(dst_file_md_path, "w", encoding="utf8") as g:
        g.write(replaced_file_content)

def replace_md_files():
    glob_search_path = os.path.join(REPLACE_DIR_PATH, "**", "raw.md")

    for src_file_md_path in glob.glob(glob_search_path, recursive=True):
        dst_file_md_path = os.path.join(
            os.path.dirname(src_file_md_path),
            "index.md",
        )
        print(src_file_md_path, dst_file_md_path)
        replace_md_file(src_file_md_path, dst_file_md_path)


def md_to_dirs():
    for src_file_path in glob.glob("./content/ja/docs/**/*.md", recursive=True):
        src_file_name = os.path.basename(src_file_path)
        if (
            src_file_name.startswith("index") or 
            src_file_name.startswith("_index") or
            src_file_name.startswith("raw")
        ):
            continue

        dir_name = ".".join(src_file_path.split(".")[:-1])
        os.makedirs(dir_name, exist_ok=True)
        dst_file_path = os.path.join(dir_name, "raw.md")   
        shutil.move(src_file_path, dst_file_path)

        match = re.match(r"(?P<number>([0-9]+_)?)(?P<title>.+)\.md", src_file_name)

        title = match.group("title")
        weight = 999
        if match.group("number"):
            weight = int(match.group("number")[:-1])
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        setting_yaml = SETTING_YAML_TEMPLATE.format(
            title=title,
            date=date,
            weight=weight,
        )

        with open(dst_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        with open(dst_file_path, "w", encoding="utf-8") as f:
            content = f.write(setting_yaml + content)


def run():
    # md_to_dirs()
    replace_md_files()

if __name__ == "__main__":
    run()