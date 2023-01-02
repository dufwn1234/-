##상속
##일반유닛
class Unit:
    def __init__(self, name):
        self.name=name
        self.hp=hp


##공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp,  damage):
        Unit.__init__(self, name, hp )
        self.damage=damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged (self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) 
        self.hp-=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp)) 
        if self.hp <=0 :
            print("{0} : 파괴되었습니다.".format(self.name))


# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# ##공격 2번받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


##다중 상속
##날수있는 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self , name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 {2}]".format(name, location,self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name,hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,  damage)
        Flyable.__init__(self, flying_speed)



