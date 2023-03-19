import pandas
import matplotlib.pyplot as plt

# matplotlibの全体的な設定
plt.rcParams["font.family"] = "MS Gothic"
plt.rcParams["figure.subplot.left"] = 0.3
plt.rcParams["figure.subplot.bottom"] = 0.1
plt.rcParams["font.size"] = 10


# 引数の配列をデータフレームに格納する
def create_data_frame(arg_list):
    # データフレーム用の配列を作成
    title_list = []
    view_count_list = []
    tags_list = []
    tag_priority_list = []
    for video in arg_list:
        priority = 1
        for tag in video["tags"]:
            title_list.append(video["title"])
            view_count_list.append(video["view_count"])
            tags_list.append(tag)
            tag_priority_list.append(priority)
            priority += 1
    # データフレームを作成
    data_frame = pandas.DataFrame(
        data={
            "title": title_list,
            "view_count": view_count_list,
            "tag": tags_list,
            "tag_priority": tag_priority_list,
        }
    )
    return data_frame


# 引数のデータフレームからグラフを出力する
def create_result_graph(arg_df, search_word, video_number):
    # タグのグループを作成
    group_tag = arg_df.groupby("tag", as_index=False)
    # タグの出現回数を算出後に、多い順に並び変え、インデックスを振り直し、先頭の指定行を抽出
    sorted_group_tag = (
        group_tag.size()
        .sort_values("size", ascending=False)
        .set_index("tag")[0:20]
        .sort_values("size", ascending=True)
    )
    # グラフを描画
    axes = sorted_group_tag.plot(
        kind="barh", title="上位人気タグ"
    )  # MatplotlibのAxesSubplotオブジェクト

    # グラフのプロパティ設定
    axes.set_xlabel("使用回数")
    axes.set_ylabel("")
    axes.get_legend().remove()
    fig = axes.get_figure()
    fig.suptitle('検索ワード："' + search_word + '", 検索数：' + video_number)

    # グラフの保存処理
    try:
        fig.savefig("./graph/result.jpg")
        print('Result graph was successfully saved! See "./graph/result.jpg".')
    except:
        print("Saving result graph was failed.")
