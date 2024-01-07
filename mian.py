import flet as ft
from st_processing import*
import calc_set as ms
import time


class hotword_ranking(ft.UserControl):
    def __init__(self):
        super().__init__()  # 基底クラスのコンストラクタを呼び出す
        self.num = '0'
        self.data = 'コメント'
        self.width = 200
        self.padding = 16
        self.text_control = ft.Text(self.data, style=ft.TextThemeStyle.TITLE_MEDIUM)

    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.CircleAvatar(content=ft.Text(self.num), bgcolor=ft.colors.PURPLE_200),
                        ft.Column(
                            controls=[
                                self.text_control,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ]
                ),
                width=self.width,
                padding=self.padding,
            )
        )
    
    def update_data(self, new_data):
        self.data = new_data
        self.build()
        self.text_control.value = self.data
        self.update()  # MyControlを更新



class chat_field(ft.UserControl):
    def __init__(self):
        super().__init__()  # 基底クラスのコンストラクタを呼び出す
        self.num = '0'
        self.data = "コメント"
        self.data_old = "コメント"
        self.keyword_data1 = "-"
        self.keyword_data2 = "-"
        self.keyword_data3 = "-"
        self.keyword_data4 = "-"
        self.keyword_len = 4
        #self.padding = 40
        self.text_control = ft.Text(self.data, style=ft.TextThemeStyle.TITLE_MEDIUM)
        self.text_old = ft.Text(self.data_old, color=ft.colors.BLACK38)

        self.keyword1 = ft.Text(self.keyword_data1, size=20, color="pink300", style=ft.TextThemeStyle.TITLE_MEDIUM)
        self.keyword2 = ft.Text(self.keyword_data2, size=20, color="orange300", style=ft.TextThemeStyle.TITLE_MEDIUM)
        self.keyword3 = ft.Text(self.keyword_data3, size=20, color="orange300", style=ft.TextThemeStyle.TITLE_MEDIUM)
        self.keyword4 = ft.Text(self.keyword_data4, size=20, color="pink300", style=ft.TextThemeStyle.TITLE_MEDIUM)


    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Column(
                            [self.keyword1, self.keyword2,]
                        ),
                        ft.Column(
                            [ft.Text("  ")]
                        ),
                        ft.Column(
                            [self.keyword3, self.keyword4,]
                        ),
                        ft.Column(
                            [ft.Text("  ")]
                        ),
                        ft.Column(
                            controls=[self.text_control, self.text_old,],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ]
                ),
                width=750, padding=24,
            )
        )

    def update_data(self, new_data, new_user, keyword):
        
        self.data = new_data
        self.data_old = new_user
        self.keyword_len = len(keyword)

        if len(keyword) == 1:
            self.keyword_data1 = keyword[0]
            self.keyword_data2 = "-"
            self.keyword_data3 = "-"
            self.keyword_data4 = "-"
        if len(keyword) == 2:
            self.keyword_data1 = keyword[0]
            self.keyword_data2 = keyword[1]
            self.keyword_data3 = "-"
            self.keyword_data4 = "-"
        if len(keyword) == 3:
            self.keyword_data1 = keyword[0]
            self.keyword_data2 = keyword[1]
            self.keyword_data3 = keyword[2]
            self.keyword_data4 = "-"   
        if len(keyword) == 4:
            self.keyword_data1 = keyword[0]
            self.keyword_data2 = keyword[1]
            self.keyword_data3 = keyword[2]
            self.keyword_data4 = keyword[3]

        self.build()

        self.text_control.value = self.data
        self.text_old.value = self.data_old
        self.keyword1.value = self.keyword_data1
        self.keyword2.value = self.keyword_data2
        self.keyword3.value = self.keyword_data3
        self.keyword4.value = self.keyword_data4

        self.update()



def main(page):
    
    def start_streaming(e):
        yt_url = url_input.value

        slp_time        = 10 #sec
        iter_times      = 90 #回
        take_time       = slp_time / 60 * iter_times
        print('{}分後　終了予定'.format(take_time))
        print('work on {}'.format(yt_url))

        chat_id  = get_chat_id(yt_url)
        set = [ms.set(1), ms.set(2), ms.set(3), ms.set(4)]

        #初期値
        t1 = "私は明日、図書館に一人で行く"
        set[0].addpar(ta.get_word_counts(t1), 0)
        set[1].addpar(ta.get_word_counts(t1), 0)
        set[2].addpar(ta.get_word_counts(t1), 0)
        set[3].addpar(ta.get_word_counts(t1), 0)

        t2 = "君は明日、図書館で一人で遊ぶ"
        set[0].addpar(ta.get_word_counts(t2), 1)
        set[1].addpar(ta.get_word_counts(t2), 1)
        set[2].addpar(ta.get_word_counts(t2), 1)
        set[3].addpar(ta.get_word_counts(t2), 1)

        textWindow = [[t1, t2]]
        indexWindow = [[0, 1]]
        userWindow = [['user0', 'user1']]
        lastNum = 1
        nextPageToken = None

    
        for ii in range(iter_times):#テキストストリーム処理

            nextPageToken, ctext, cuser, textNum = get_chat(chat_id, nextPageToken, lastNum+1)
            textWindow.append(ctext)
            userWindow.append(cuser)
            indexWindow.append(textNum)
            if not ctext:
                print("コメントはありません")
            else:
                textWindow, userWindow, indexWindow, nextPageToken, lis_id, lis_text, lis_user, key_word1, key_word2 = streampro(textWindow, userWindow, indexWindow, set, nextPageToken)
                if lis_id != None:
                    lastNum = indexWindow[-1][-1]

                    # ホットワードランキングを更新
                    chat_text1.update_data(lis_text[0], lis_user[0], key_word1)
                    chat_text2.update_data(lis_text[1], lis_user[1], key_word2)
                    # 上位3つのホットワードを表示
                    rank1.update_data("\n".join(lis_id[0]))
                    rank2.update_data("\n".join(lis_id[1]))
                    rank3.update_data("\n".join(lis_id[2]))
                else:
                    print("テキスト処理が正常に行えませんでした")

            if len(textWindow) > 20:
                for i in range(len(textWindow[0])):
                    set[0].subpar()
                    set[1].subpar()
                    set[2].subpar()
                    set[3].subpar()

                textWindow.pop(0)
                indexWindow.pop(0)
                userWindow.pop(0)
                print("-------", len(textWindow),"-------")

            time.sleep(slp_time)


#以降UIの設定
    rank1 = hotword_ranking()
    rank2 = hotword_ranking()
    rank3 = hotword_ranking()

    rank1.num = 1
    rank2.num = 2
    rank3.num = 3

    hotwords_column = ft.Column([
        ft.Text("   ホットワード", color="purple300", style=ft.TextThemeStyle.TITLE_LARGE),
        rank1,
        rank2,
        rank3
    ])

    chat_text1 = chat_field()
    chat_text2 = chat_field()


    chat_text_column = ft.Column([
        ft.Text("    おすすめコメント", color="pink300", style=ft.TextThemeStyle.TITLE_LARGE),
        chat_text1,
        chat_text2
    ])

    # ホットワードランキングとチャット欄を横に並べる
    main_row = ft.Row(
        controls=[
            hotwords_column,
            chat_text_column
        ], expand=True)

    # URL入力欄とスタートボタンを作成
    url_input = ft.TextField(hint_text="YouTube URLを入力してください")
    start_button = ft.ElevatedButton(text="スタート", on_click=start_streaming)
    controls_row = ft.Row([url_input, start_button])

    # ページにコントロールを追加
    page.add(controls_row)  # URL入力欄とスタートボタンを最上部に配置
    page.add(main_row)      # ホットワードランキングとチャット欄を下に配置


ft.app(target=main)

