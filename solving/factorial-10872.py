def factorial():

    def _recursive(n): 
        if n > 1: 
            t = _recursive(n - 1)
            value = n * t
            return value
        else: 
            return 1
    n = int(input())
    print(_recursive(n))
factorial()  