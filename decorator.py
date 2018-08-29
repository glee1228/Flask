def hello(f) :
    def greeting() :
        print("^0^")
        f()
        print("ㅠㅠ")
    return greeting

@hello
def korean() :
    print("안녕하세요")
    
@hello
def english() :
    print("hello")
    
def test() :
    print("테스트입니다")
    
#korean()
#english()
a = hello(test)
a()