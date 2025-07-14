from typing import List
from dataclasses import dataclass, field
import os
import datetime
import shutil
import glob
import re
import yaml

SOURCE_DIR_PATH = ".\\ja\\blog"
DESTINATION_DIR_PATH = "..\\content\\ja\\blog"

@dataclass
class YamlConfig:
    date: str = ""
    title: str = ""
    description: str = ""
    linkTitle: str = ""
    slug: str = ""
    author: str = "Yuki Wada"
    weight: int = 999
    categories: List[str] = field(default_factory=list)
    aliases: List[str] = field(default_factory=list)
    math: bool = True
    draft: bool = True

    def __str__(self):
        return "---\n" + yaml.dump(
            {
                "date": self.date,
                "title": self.title,
                "description": self.description,
                "slug": self.slug,
                "author": self.author,
                "weight": self.weight,
                "categories": self.categories,
                "aliases": self.aliases,
                "math": self.math,
                "draft": self.draft,
            },
            allow_unicode=True,
        ) + "---\n"

class MarkDownReplacer:
    @staticmethod
    def split_into_config_and_content(file_content):
        yaml_config_str = ""
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
                    yaml_config_str += raw_line
            elif flag == "InContent":
                content += raw_line
            else:
                raise ValueError()

        yaml_config = YamlConfig(**yaml.full_load(yaml_config_str))
        return yaml_config, content

    @staticmethod
    def replace_content(src_file_md_path, dst_file_md_path):
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
                equation_text = re.sub(r"\,", r"\\,", equation_text)
                replaced_inline_text += raw_text
                replaced_inline_text += r"\\(" + equation_text + r"\\)"

            replaced_inline_text += src

            return replaced_inline_text

        def convert_block(src):
            src_block_text = re.sub(r"\n", " ", src[2:-2])
            if not src_block_text.strip().startswith(r"\begin"):
                src_block_text = r" \begin{aligned} " + src_block_text + r" \end{aligned} " 
            src_block_text = escape_underbar(src_block_text)
            src_block_text = re.sub(r"\\", r"\\\\", src_block_text) 
            src_block_text = re.sub(r"\,", r"\\,", src_block_text)
            return r"\\[" + src_block_text + r"\\]"

        with open(src_file_md_path, "r", encoding="utf8") as f:
            file_content = f.read()
            # src_yaml_config, src_text = MarkDownReplacer.split_into_config_and_content(file_content)
            src_text = file_content

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

        return replaced_content

class PathCalculator:
    @staticmethod
    def calculate_copy_infos():
        glob_search_path = os.path.join(
            SOURCE_DIR_PATH,
            "**",
            "index.md",
        )

        for src_file_path in glob.glob(glob_search_path, recursive=True):
            # src_file_name = os.path.basename(src_file_path)
            # if (
            #     src_file_name.startswith("index") or 
            #     src_file_name.startswith("_index") or
            #     src_file_name.startswith("raw") or
            #     src_file_name.startswith("@")
            # ):
            #     continue

            src_dir_path = os.path.dirname(src_file_path)

            dst_dir_name = os.path.basename(os.path.dirname(src_file_path))
            dst_dir_path = os.path.join(DESTINATION_DIR_PATH, dst_dir_name)

            src_file_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(src_file_path))

            copy_info = {
                "src_dir_path": src_dir_path,
                "dst_dir_path": dst_dir_path,
                "src_file_timestamp": src_file_timestamp,
            }

            yield copy_info
            # print(copy_info)

    @staticmethod
    def copy_dir(src_dir_path, dst_dir_path):
        def update_index_config(src_file_md_path, dst_file_md_path):
            with open(src_file_md_path, "r", encoding="utf8") as f:
                file_content = f.read()
                src_yaml_config, src_text = MarkDownReplacer.split_into_config_and_content(file_content)

            dst_yaml_config = ""
            with open(dst_file_md_path, "r", encoding="utf8") as f:
                file_content = f.read()
                dst_yaml_config, _ = MarkDownReplacer.split_into_config_and_content(file_content)

            dst_content = str(src_yaml_config) + src_text
            with open(dst_file_md_path, "w", encoding="utf8") as f:
                f.write(dst_content)

        def copy_file(src_file_path, dst_file_path):
            dst_dir_path = os.path.dirname(dst_file_path)
            if not os.path.exists(dst_dir_path):
                os.makedirs(dst_dir_path, exist_ok=True)
            shutil.copy(src_file_path, dst_file_path)

        src_file_path = os.path.join(src_dir_path, "index.md")
        dst_file_path = os.path.join(dst_dir_path, "index.md")

        if src_file_path.endswith("index.md") and os.path.exists(dst_file_path):
            update_index_config(src_file_path, dst_file_path)
        else:
            copy_file(src_file_path, dst_file_path)

    @staticmethod
    def calculate_replacement_infos():
        glob_search_path = os.path.join(
            DESTINATION_DIR_PATH,
            "**",
            "index.md",
        )

        for src_file_md_path in glob.glob(glob_search_path, recursive=True):
            dst_file_md_path = os.path.join(
                os.path.dirname(src_file_md_path),
                "index.md",
            )
            yield src_file_md_path, dst_file_md_path
            # print(src_file_md_path, dst_file_md_path)


def md_to_dirs():
    for copy_info in PathCalculator.calculate_copy_infos():
        src_dir_path = copy_info["src_dir_path"]
        dst_dir_path = copy_info["dst_dir_path"]
        PathCalculator.copy_dir(src_dir_path, dst_dir_path)


def replace_md_files():
    for src_file_md_path, dst_file_md_path in PathCalculator.calculate_replacement_infos():
        replaced_file_content = MarkDownReplacer.replace_content(src_file_md_path, dst_file_md_path)
        with open(dst_file_md_path, "w", encoding="utf8") as g:
            g.write(replaced_file_content)


def run():
    md_to_dirs()
    replace_md_files()


if __name__ == "__main__":
    run()