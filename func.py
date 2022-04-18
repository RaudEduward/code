from functools import reduce
def run():
    values=[1,2,3,4,5,6,7,8,9,10]
    squares=list(map(lambda x: x**2,values))
    print(squares)
    r_squares=list(filter(lambda x: x % 2 ==0 , squares))
    print(r_squares)

    add_squares = (reduce(lambda x,y: x+y, values))
    print(add_squares)



if __name__=='__main__':
    run()
