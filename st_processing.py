import text_analysis as ta
from comm_get import*

def streampro(textWindow, userWindow, indexWindow, set, nextPageToken):
    try:
        print('\n')
        print("-----------------333----------------")
        #nextPageToken, ctext, cuser, textNum = get_chat(chat_id, nextPageToken, indexWindow[-1][-1]+1)


        #textWindow.append(ctext)
        #userWindow.append(cuser)
        #indexWindow.append(textNum)

        print("len=", len(textWindow[-1]))

        for (t, n) in zip(textWindow[-1], indexWindow[-1]):
            tt = ta.get_word_counts(t)
            if len(tt) > 0:
                set[0].addpar(tt, n)
                set[1].addpar(tt, n)
                set[2].addpar(tt, n)
                set[3].addpar(tt, n)


        """if len(textWindow) > 20:
            for i in range(len(textWindow[0])):
                set[0].subpar()
                set[1].subpar()
                set[2].subpar()
                set[3].subpar()

            textWindow.pop(0)
            indexWindow.pop(0)
            userWindow.pop(0)
            print("-------", len(textWindow),"-------")"""

        print("rrrrrrrrrrrrrrrr")
        lis_text = [[],[],[],[]]
        lis_user = [[],[],[],[]]

        print("main1 ", set[0].mainset[:5])
        print("set1 ", set[0].index[:5])
        print("コメント")
        for i in range(1, len(set[0].index[0])+1): 
            com, usr = set[0].findText(textWindow, userWindow, indexWindow, set[0].index[0][-i])
            lis_text[0].append(com)
            lis_user[0].append(usr)
            print(com, usr)
            #lis_text[0].append(set[0].findText(textWindow, indexWindow, set[0].index[0][-i]))


        print("main2 ", set[1].mainset[:5])
        print("set2 ", set[1].index[:5])
        print("コメント")
        for i in range(1, len(set[1].index[0])+1):
            com, usr = set[0].findText(textWindow, userWindow, indexWindow, set[1].index[0][-i])
            lis_text[1].append(com)
            lis_user[1].append(usr)
            print(com, usr)
            #print(set[1].findText(textWindow, indexWindow, set[1].index[0][-i]))
            #lis_text[1].append(set[0].findText(textWindow, indexWindow, set[0].index[0][-i]))

        #print("main3 ", set[2].mainset[:10])
        #print("set3 ", set[2].index[:10])
        #print("コメント")
        for i in range(1, len(set[2].index[0])+1): 
            com, usr = set[0].findText(textWindow, userWindow, indexWindow, set[2].index[0][-i])
            lis_text[2].append(com)
            lis_user[2].append(usr)
            print(com, usr)

        #print("main4 ", set[3].mainset[:10])
        #print("set4 ", set[3].index[:10])
        #print("コメント")
        for i in range(1, len(set[3].index[0])+1):
            com, usr = set[0].findText(textWindow, userWindow, indexWindow, set[3].index[0][-i])
            lis_text[3].append(com)
            lis_user[3].append(usr)
            print(com, usr)

        #エラー処理がまだ
        rank_key = set[0].mainset[:3]

        #man = [len(set[0].index[0]), len(set[0].index[1]), len(set[1].index[0])*2, len(set[1].index[1])*2, len(set[2].index[0])*3, len(set[2].index[1])*3, len(set[3].index[0])*4, len(set[3].index[1])*4]
        #print(man)
        #print(man.index(max(man)))
        
        comp = []
        if len(set[0].index) != 0:
            comp.append(len(set[0].index[0]))

        if len(set[1].index) != 0:
            comp.append(len(set[1].index[0])*3)            
        
        if len(set[2].index) != 0:
            comp.append(len(set[2].index[0])*4)   

        if len(set[3].index) != 0:
            comp.append(len(set[3].index[0])*5)

        if len(comp) == 4:
            comped = sorted(comp)
            in1 = comp.index(comped[-1])
            in2 = comp.index(comped[-2])
            out_text = [lis_text[in1][-1],lis_text[in2][-1]]
            out_user = [lis_user[in1][-1],lis_user[in2][-1]]
            out_key1 = set[in1].mainset[0]
            out_key2 = set[in2].mainset[0]
        else:
            out_text = None
            out_user = None
            out_key1 = None
            out_key2 = None


        return textWindow, userWindow, indexWindow, nextPageToken, rank_key, out_text, out_user, out_key1, out_key2
    except Exception as e:
        print(f"An error occurred: {e}")
        # ここで適切な数の None を返すか、他のデフォルト値を設定してください。
        return None, None, None, None, None, None, None, None, None
