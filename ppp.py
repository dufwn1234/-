name=["유튜버1","유튜버2","유튜버3","유튜버4"]

for i in name:
    mail_file=open("{0}.txt".format(i),"w",encoding="utf8")
    mail_file.write("안녕하세요? {0}님.\n".format(i))
    mail_file.write("""
(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.    
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.\n
    """.format(i))
    mail_file.write("- 나코 드림.")
    mail_file.close()

































'''
안녕하세요? XXX님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
'''