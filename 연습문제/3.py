class Word:
    def __init__(self,ggg,word1,word2,answer):
        self.ggg=ggg
        self.word1=word1
        self.word2=word2
        self.answer=answer

    def show_question(self):
        print('"{0}"의 뜻은?'.format(self.ggg))
        print("1.{0}".format(self.word1))
        print("2.{0}".format(self.word2))


    def check_answer(self,answer1):
        if self.answer==answer1:
            print("정답입니다.")
        else:
            print("틀렸습니다.")



word=Word("얼죽아","얼어 죽어도 아메리카노","얼굴은 죽어도 아기피부",1)
word.show_question()
word.check_answer(int(input("=> ")))

