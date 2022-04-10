def secondary (a: int):
    list_a=[i for i in range(1,a+1) if a % i == 0]
    if len(list_a) <= 2: 
        print("numero primo")
    else:
        print("Numero no primo")
def run():
    a= int(input("Digite un número: "))
    secondary(a)

if __name__=='__main__':
    run()
