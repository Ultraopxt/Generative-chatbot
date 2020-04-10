#导入库
from model import ChatBot
import torch,warnings,argparse
warnings.filterwarnings("ignore")


#主程序，打印log，同时对话
if __name__ == "__main__":
    print('Loading the model...')
    chatBot = ChatBot('modelB.pkl')
    print('Finished...')

    allRandomChoose,showInfo = False, False
    #在控制端显示的词语
    while True:
        inputSeq = input("主人: ")
        if inputSeq=='_crazy_on_':
            allRandomChoose = True
            print('小可爱: ','成功开启疯狂模式...')
        elif inputSeq=='_crazy_off_':
            allRandomChoose = False
            print('小可爱: ','成功关闭疯狂模式...')
        elif inputSeq=='_showInfo_on_':
            showInfo = True
            print('小可爱: ','成功开启日志打印...')
        elif inputSeq=='_showInfo_off_':
            showInfo = False
            print('小可爱: ','成功关闭日志打印...')
        else:
            outputSeq = chatBot.predictByBeamSearch(inputSeq, isRandomChoose=True, allRandomChoose=allRandomChoose, showInfo=showInfo)
            print('小可爱: ',outputSeq)
        print()