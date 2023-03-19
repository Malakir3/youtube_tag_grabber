#!/usr/bin/python

import os
from dotenv import load_dotenv
from module import data_analyze
from module import youtube

# 環境変数の読み込み
load_dotenv()

DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")
YOUTUBE_API_SERVICE_NAME = os.environ.get("YOUTUBE_API_SERVICE_NAME")
YOUTUBE_API_VERSION = os.environ.get("YOUTUBE_API_VERSION")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
SEARCH_WORD = os.environ.get("SEARCH_WORD")
MAX_RESULTS = os.environ.get("MAX_RESULTS")

if __name__ == "__main__":
    # 動画詳細の一覧を取得
    finder_result = youtube.search(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        DEVELOPER_KEY,
        SEARCH_WORD,
        MAX_RESULTS,
    )

    # 一覧をデータフレームに格納
    data_frame = data_analyze.create_data_frame(finder_result)

    # データフレームからグラフを出力
    data_analyze.create_result_graph(data_frame, SEARCH_WORD, MAX_RESULTS)
