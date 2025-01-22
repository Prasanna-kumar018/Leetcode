class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        arr= num1.split('+')
        arr2= num2.split('+')
        """
        a + bi  c+di
        (ac-bd) + bci + adi 
        (ac-bd) + (bc+ad)i 
        """
        a= int(arr[0])
        b=int(arr[1][:-1])
        c=int(arr2[0])
        d=int(arr2[1][:-1])
        return str(a*c+(-b*d))+"+"+str(a*d+b*c)+"i"
        