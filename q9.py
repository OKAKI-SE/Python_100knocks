#Q9: RPGゲームクラスの作成
#問題：キャラクターのステータスを登録して、お互いに攻撃することができるクラスを作成せよ。
#条件：
#・キャラクターは名前,体力の現在値、体力の最大値、攻撃力,防御力の5つのパラメータをもっており、いつでも参照することができる。
#・キャラクターは別のキャラクターを攻撃して、相手の体力を自分の攻撃力(-相手の防御力)分だけ減らすことができる。

class Character:
    def __init__(self,name,maxhp,attack_point,defence_point):
        self.name = name
        self.maxhp = maxhp 
        self.hp = maxhp
        self.attack_point = attack_point
        self.defence_point = defence_point


    def status(self):
        return "{}:体力 {}/{}:攻撃力 {} 防御力 {}".format(self.name,self.hp,self.maxhp,self.attack_point,self.defence_point)

    def attack(self,enemy):
        cal_attack_point = self.attack_point - enemy.defence_point
        enemy.hp -= cal_attack_point
        print("{}の攻撃！{}に{}のダメージ！".format(self.name,enemy.name,cal_attack_point))


yusha = Character("勇者",60,10,2)
slime = Character("スライム",15,5,1)

# ステータスを表示
print(yusha.status())
print(slime.status())

# 勇者の攻撃
yusha.attack(slime)
# スライムの攻撃:
slime.attack(yusha)

# ステータスを表示
print(yusha.status())  # 勇者のステータス
print(slime.status())  # スライムのステータス