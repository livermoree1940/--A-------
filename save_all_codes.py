# -*- coding: utf-8 -*-
"""
一键获取全部 A 股代码列表并导出为 CSV / TXT
运行：python save_all_codes.py
"""
import pathlib
import adata

# 1. 拉取全量数据
print("正在拉取全部 A 股代码列表，请稍候…")
df = adata.stock.info.all_code()
print(f"共获取 {len(df)} 条记录")

# 2. 生成输出目录
out_dir = pathlib.Path("output")
out_dir.mkdir(exist_ok=True)

# 3. 导出 CSV（UTF-8-SIG，Windows 直接双击打开不乱码）
csv_file = out_dir / "A股全部股票代码.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")
print(f"CSV 已保存 → {csv_file.resolve()}")

# 4. 导出 TXT（制表符分隔，无索引）
txt_file = out_dir / "A股全部股票代码.txt"
df.to_csv(txt_file, index=False, sep="\t", encoding="utf-8")
print(f"TXT 已保存 → {txt_file.resolve()}")