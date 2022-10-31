from tkinter.messagebox import QUESTION
from typing import Counter
from unicodedata import name

from regex import P


name=input("名前を教えて下さーい")
print(name,"さんようこそ！")
print("このゲームはあなたの運or判断力が試されるゲームです。")
print("ルールは簡単で値を超えないようにしてください。数を足したければ「yes」そうでなければ「no」を押してください")
print("「no」を押した場合それがあなたのスコアになります。")

print("ゲームスタート")

import random
from re import I
from tkinter import Y
Counter=0

print("21を超えないように限界まで挑戦してください。")
print("現在の数字は0です。")
while Counter<=21:
    a=random.randint(1,5)
    QUESTION=input("まだ足しますか？")
    if QUESTION=="yes":
        Counter=Counter+a
        print("現在の合計は",Counter,"です。")
    elif Counter==21:
        print("おめでとうございます！21ピッタリです！")
        break
    elif QUESTION=="no":
        print("ハイスコアは",Counter,"です。")
        break

else:
     print("21を超えました。失敗です")
    


