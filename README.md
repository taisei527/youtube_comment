youtube live などにおいて、人気配信は大量のコメントが押し寄せ、配信者がコメントを追えなくなる。そこで、コメントのストリームから頻出コメントを選択して表示するソフトを作成した。


## 頻出コメント
頻出コメントは、コメント内のキーワードの一致数で判断した。例えば、「A君の声、かっこいい」と「Aさんかっこいい」というコメントは"A"と"かっこいい"の２つのキーワードが共通している。
他にも、３つのキーワード、４つのキーワードが一致する場合も考えられる。
コメント集合の中で、このような共通キーワードを全て計算することは非常に重い処理となる。今回は、共通キーワードを最大４つまで、コメント集合内で全て計算した。その中で、多くのコメントに共通するキーワードを見つけ、その共通キーワードをもつコメントを頻出コメントと定めた。


## コメント処理アルゴリズムの流れ
過去２００秒間のコメントをコメント集合とし、コメント集合に対する共通キーワードを10秒おきに更新し、頻出コメントを選択する。
具体的には、以下のような流れ。

1. 10秒間隔でyoutube live のコメントを取得すし、コメント集合に追加。
1. 共通キーワードを計算。ここでコメント集合全体に対して計算すると処理が非常に重くなるので、新たに追加したコメントに対して共通キーワードの増分を計算。
1. 共通キーワードから頻出コメントを選択。
1. コメント集合内の最古の10秒間のコメントを削除。このとき、コメントの削除に対して共通キーワードの減少分を計算。


## 実行
必要なライブラリをインストール後、comm_get.pyのYT_API_KEYにYouTube API keyを入力する。
comm_get.py、YouTube API keyの取得は[1]を参考にした。

実行すると、画像のように左のyoutube liveのコメントから取得した頻出コメントが右のソフトのオススメに表示される。
私の実行環境では、1秒間に5コメント程度のストリームにおいて十分に余裕をもって処理できた。
![スクリーンショット 2024-01-08 214614](https://github.com/taisei527/youtube_comment/assets/134770116/dce4eae1-db8d-4a2d-8889-04b42ce9d479)


[1] https://qiita.com/iroiro_bot/items/ad0f3901a2336fe48e8f


## 今後変更したい点
- キーワードのカタカナ表示を変える
- ホットワードに載せるキーワードの選択アルゴリズムの変更
- 学習済み機械学習モデルを用いた不適切なコメントの識別
