import numpy as np
def  main():
    x=np.linspace(0, (2*np.pi), 1000)
    print("x                           sin(x)")
    for x_val in x:
        print(x_val,"    ", np.sin(x_val))
if __name__ == "__main__":
    main()