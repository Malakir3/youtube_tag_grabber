from googleapiclient.discovery import build


def search(
    youtube_api_service_name, youtube_api_version, api_key, search_word, max_results
):
    # サービスオブジェクトを生成
    youtube = build(youtube_api_service_name, youtube_api_version, developerKey=api_key)

    # 動画一覧を取得
    search_response = (
        youtube.search()
        .list(
            q=search_word,
            type="video",
            part="id,snippet",
            maxResults=max_results,
            order="viewCount"
            # 以下は任意で設定。channelIdを使用する場合は、envの値を引数で受け取るよう記述する。
            # channelId = CHANNEL_ID,
            # videoDuration = "medium",
        )
        .execute()
    )

    # 動画の詳細情報を検索
    finder_result = []
    for each_video in search_response.get("items", []):
        video_detail = (
            youtube.videos()
            .list(id=each_video["id"]["videoId"], part="snippet,statistics")
            .execute()
        )

        # 一時的な辞書を作成
        tmp_dict = {}
        tmp_dict["title"] = video_detail["items"][0]["snippet"]["title"]
        tmp_dict["view_count"] = video_detail["items"][0]["statistics"]["viewCount"]
        # タグが設定されていない動画は例外として扱う
        if "tags" in video_detail["items"][0]["snippet"]:
            tmp_dict["tags"] = video_detail["items"][0]["snippet"]["tags"]
        else:
            tmp_dict["tags"] = ["タグ無し"]

        # 結果配列に辞書を格納
        finder_result.append(tmp_dict)

    ##########################################################
    # 任意の後続処理
    # 例：結果を表示
    # json_result = json.dumps(finder_result,indent=4,ensure_ascii=False)
    # print(json_result)
    ##########################################################

    return finder_result
