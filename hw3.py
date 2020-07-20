#! /usr/bin/env python

class Account():
    def __init__(self, passwd, balance):
        self.__passwd = passwd
        self.__balance = balance
    
    def deposit(self, money):
        print(money,'원 입금')
        self.__balance += money
        print('잔액',self.__balance,'원')
    
    def withdraw(self,money):
        if money > self.__balance:
            print('잔액부족')
        else:
            print(money,'원 출금')
            self.__balance -= money
            print('잔액',self.__balance,'원')
        
    def transfer(self,name,money):
        if money > self.__balance:
            print('잔액부족')
        else:
            print(name,'에게',money,'원을  송금합니다.')
            self.__balance -= money
            print('잔액',self.__balance,'원')

    def pwConfirm(self,givePw):
        if self.__passwd == givePw:
            print("원하시는 서비스를 선택하세요.\n","deposit\n","withdraw\n","transfer")
        else:
            print("비밀번호가 다릅니다.")


sooji = Account(1234,0)
jisu = Account(2345,2000)
seonhoe = Account(3456,0)
yeseul = Account(4567,0)
eunbi = Account(5678,0)

jisu.deposit(30000) #성공!
jisu.withdraw(32000) #성공!
jisu.transfer(input("누구에게 송금하시겠습니까?: "),3000) #성공!
#jisu.pwConfirm(input("비밀번호를 입력하세요.: ")) #안됨... 도대체 왜??ㅠㅠ

#기록을 계속 남겨서 누적되게 하는데 내 눈에는 안 보이는 방법은 없겠지??
#비밀번호 입력해서 성공해야 다음으로 넘어가게 하고싶은데 딕셔너리 만들어서??





