import json
import sys


def parse_nb(path):
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
        # セルの情報をリストに格納
        cells = nb["cells"]
        # セルからコード部分のみ取得
        cells_code = [c["source"] for c in cells if c["cell_type"] == "code"]
        # returnする文字列を定義
        py = ""
        for line in cells_code:
            # セルの最終行に改行を追加
            line[-1] += "\n" * 2
            # 行をテキストとして追加
            for l in line:
                py += l
        # 最終行の改行を全削除して空白行を1行追加
        py = py.rstrip() + "\n"
        return py
