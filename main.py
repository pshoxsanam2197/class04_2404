# 7-m
class Kitob:
    def och(self):
        print("Kitob ochildi")

    def oqi(self):
        self.och()
        print("Kitob o'qilmoqda")

    def yop(self):
        self.oqi()
        print("Kitob yopildi")

k1 = Kitob()
k1.och()
print("-----------")
k1.oqi()
print("-----------")
k1.yop()

# 8-m
class Ovqat:
    def tayyorla(self):
        print("Ovqat tayyorlandi")

    def ye(self):
        self.tayyorla()
        print("Oqat yeyildi")

    def yuv(self):
        self.ye()
        print("Idishlarni yuv")

o1 = Ovqat()
o1.tayyorla()
print("-----------")
o1.ye()
print("-----------")
o1.yuv()
