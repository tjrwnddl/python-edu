class FourCal:
    #first=0 # 생략이 가능 (파이썬만 가능)
    #second=0 # 생략이 가능
    #result=0 # 생략이 가능
    def __init__(self, first, second):      # 맴버필드 초기화 하기 위함
        self.first=first
        self.second=second
    def add(self):
        self.result = self.first + self.second
    def div(self):
        self.result = self.first / self.second

class MoreFourCal(FourCal):
    # def add(): 클래스의 상속
    # def div():
    def sub(self):
        self.result=self.first - self.second
    def mul(self):
        self.result=self.first * self.second
    def div(self): # 재정의 (override) 부모로부터 받은 함수를 재정의하고 싶다.
        if self.second == 0:
            self.result = 0
        else:
            self.result=self.first / self.second 
            


mmCal=MoreFourCal(200,400)
PI=3.141592