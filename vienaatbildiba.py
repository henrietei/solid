class Taisnsturis():
    def __init__(self, a, b):
        self.mala1=a
        self.mala2=b

    def perimetrs(self):
        return 2*(self.mala1+self.mala2)

    def laukums(self):
        return self.mala1*self.mala2

JaunsTaisnsturis=Taisnsturis(2,5)
print(JaunsTaisnsturis.perimetrs())
print(JaunsTaisnsturis.laukums())