import random
import string
n=[]

def shutudai():
    al = list(string.ascii_uppercase)
    q=random.sample(al,10)
    print("対象文字:")
    for i in q:
        print(i+" ",end="")
    
    print("\n")

    q2= random.sample(q,random.randint(7,9))
    print("表示文字:")
    for i in q2:
        print(i+" ",end="")

    for i in q:
        if (i in q2):
            continue
        else:
            n.append(i)

    print("\n")
    
    return n


def kaitou(ans_lst):
    ans1 = input("欠損文字はいくつあるでしょうか?:")
    if int(ans1)==len(n):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        count=len(n)
        for i in range(count):
            ans2=input(f"{i+1}つ目の文字を入力してください")
            if ans2 in n:
                n.remove(ans2)
            else:
                print("不正解です。またチャレンジしてください")
                break
            if len(n)==0:
                print("正解!!!")

    else:
        print("不正解です。またチャレンジしてください")

if __name__ == "__main__":
    ans_lst=shutudai()
    kaitou(ans_lst)