class SnowLeopard():
    def characteristics(leopard):
        print("Characteristics of Snow Leopard")
        print("The snow leopard's arms are ", leopard.arm_length, "cm long")
        print("The snow leopard's legs are ", leopard.leg_length, "cm long")
        print("The snow leopard has ", leopard.eyes, "eyes")
        print("It is" , leopard.tail, "the snow leopard has a tail")
        print("It is", leopard.furry, "the snow leopard is very furry")
def main():
    sl = SnowLeopard()
    sl.arm_length = 60
    sl.leg_length = 65
    sl.eyes = 2
    sl.tail = True
    sl.furry = True
    sl.characteristics()
if __name__ == "__main__":
    main()