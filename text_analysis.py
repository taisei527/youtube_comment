import MeCab
from collections import Counter


m = MeCab.Tagger()

#キーワードにしない文字
banwords =  ["ナル", "スル", "ヤル", "クサ"]

def get_word_counts(text):
    # Parse the input text
    node = m.parseToNode(text)

    words = []
    while node:
        # Extract only Noun, Adjective, Adjective verb, Verb, and Adverb
        if node.feature.split(",")[0] in ["名詞", "形容詞", "形状詞", "動詞", "連体詞"]:
            # Use the base form of the word
            try:
                words.append(node.feature.split(",")[6])
            #except:
                #print("text analysis Error")
            except IndexError as e:
                print(e)
        node = node.next

    # Count the occurrence of each word
    word_counts = Counter(words)#意味が異なるが、カタカナが同じ単語をまとめる可能性あり
    return set(word_counts)-set(banwords)