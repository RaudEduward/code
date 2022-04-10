def make_division_by(n):
    def division(a):
        return a/n        
    return division
def run():
    make_division_by3 = make_division_by(3)
    print(make_division_by3(18))
    make_division_by5 = make_division_by(5)
    print(make_division_by5(100))
    make_division_by18 = make_division_by(18)
    print(make_division_by18(54))

if __name__=='__main__':
    run()
