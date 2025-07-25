class robot:
    def __init__(self,x,y):
        self.y=y
        self.x=x


    def move(self,huongchay):
        self.x=self.x+huongchay[0]
        self.y=self.y+huongchay[1]

    def vitri(self):
        print(f"vi chi hien tai cua ban la: {self.x}, {self.y}")

    pass


class chay:
    def __init__(self,robot,dichuyen):
        self.robot=robot
        self.dichuyen=dichuyen

    def setmove(self):
        if self.dichuyen=="TREN":
            self.robot.move(huongchay[0])
        if self.dichuyen=="DUOI":
            self.robot.move(huongchay[1])
        if self.dichuyen=="TRAI":
            self.robot.move(huongchay[3])
        if self.dichuyen=="PHAI":
            self.robot.move(huongchay[2])      


robot1=robot(0,0)
huongchay=[[0,1],[0,-1],[1,0],[-1,0]]
dichuyen=input(f"chon huong ban muon di chuyen: \n Trai \n Phai \n Tren \n Duoi\n").upper()
chay1=chay(robot1,dichuyen)
chay1.setmove()
robot1.vitri()

