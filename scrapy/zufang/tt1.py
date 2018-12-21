class foo():
    a = 1
    print("foo")

    @classmethod
    def bar(cls, ):
        b = 2
        print("bar")

x = foo
x.bar()
