import math
class robot:
    def __init__(self,x,y):
        self.y=y
        self.x=x

    def move(self,huongchay):
        self.x=self.x+huongchay[0]
        self.y=self.y+huongchay[1]
        
        if abs(self.x)  > 5 or abs( self.y) >5:
            print("ban da di chuyen ra ngoai pham vi, vui long di lai")
            return False
        else: return True

    def vitri(self):
        print(f"vi chi hien tai cua ban la: {self.x}, {self.y}")

    pass


class chay:
    huongchay=[[0,1],[0,-1],[1,0],[-1,0]]
    def __init__(self,robot,dichuyen):
        self.robot=robot
        self.dichuyen=dichuyen

    def setmove(self):
        if self.dichuyen=="TREN":
            self.robot.move(self.huongchay[0])
        if self.dichuyen=="DUOI":
            self.robot.move(self.huongchay[1])
        if self.dichuyen=="TRAI":
            self.robot.move(self.huongchay[3])
        if self.dichuyen=="PHAI":
            self.robot.move(self.huongchay[2])   

# ke thua
class smartrobot(robot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.history=[(x,y)]

    def move(self, huongchay):
        vitri=[self.x,self.y]
        super().move(huongchay)
        vitrimoi=[self.x,self.y]
        if vitrimoi!=vitri:
            self.history.append(vitrimoi)
    def move_history(self):
        for i in self.history:
            print(i)

    pass   


# robot1=robot(0,0)
# lichsu=[]
robot1=smartrobot(0,0)
huongchay=[[0,1],[0,-1],[1,0],[-1,0]]
soluot=5
i=0
while i < soluot:
    dichuyen=input(f"chon huong ban muon di chuyen: \n Trai \n Phai \n Tren \n Duoi\n").upper()
    chay1=chay(robot1,dichuyen)
    chay1.setmove()
    robot1.vitri()
    robot1.move_history()
    i+=1
# print(f"{chay.__dict__}")


