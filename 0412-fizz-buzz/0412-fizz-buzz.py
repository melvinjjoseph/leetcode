class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fizz(n):
            if n%3==0 and n%5==0:
                return "FizzBuzz"
            elif n%3==0:
                return "Fizz"
            elif n%5==0:
                return "Buzz"
            else: 
                return str(n)
        res=[]
        for i in range(1,n+1):
            res.append(fizz(i))
        return res