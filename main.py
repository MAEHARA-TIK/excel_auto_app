import glob
import logging
import os
from datetime import datetime

import pandas as pd
from config.settings import INPUT_DIR, LOG_FILE, OUTPUT_DIR

# ===== ログ設定 =====
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def merge_sales_files():
    print(">>> merge_sales_files 実行中")
    """inputフォルダ内のExcelをまとめて1ファイルに統合"""
    files = glob.glob(os.path.join(INPUT_DIR, "*.xlsx"))
    if not files:
        logging.warning("Excelファイルが見つかりません。")
        print("⚠️ inputフォルダにExcelファイルがありません。")
        return

    df_list = []
    for f in files:
        try:
            data = pd.read_excel(f)
            data["source_file"] = os.path.basename(f)
            df_list.append(data)
            logging.info(f"読込成功: {f}")
        except Exception as e:
            logging.error(f"読込失敗: {f} → {e}")
            print(f"❌ {f} の読み込みに失敗しました。")

    try:
        merged = pd.concat(df_list, ignore_index=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(
            OUTPUT_DIR, f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        )
        merged.to_excel(output_path, index=False)
        logging.info(f"統合完了: {output_path}")
        print(f"✅ 統合完了 → {output_path}")
    except Exception as e:
        logging.error(f"統合処理エラー: {e}")
        print("❌ 統合処理でエラーが発生しました。")


if __name__ == "__main__":
    logging.info("=== Excel自動統合ツール 開始 ===")
    try:
        merge_sales_files()
    except Exception as e:
        logging.critical(f"予期しないエラー: {e}")
    logging.info("=== 処理終了 ===")
