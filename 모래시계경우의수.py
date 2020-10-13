def main():
    A = int(input("Input A : "))
    B = int(input("Input B : "))
    gcd = GetGCD(A, B)

    if gcd != 1:
        print("두 수가 서로소가 아니므로 모든 시간을 측정할 수 없습니다 ")
        return 0

    list_m = list(range(0,A))
    list_n = list(range(0,A))
    count = 0
    while count < A:
        list_m[count] = 0
        count += 1
    count = 0
    while count < A:
        list_n[count] = 0
        count += 1

    m = 0
    while m<=B:
        n=0
        while n<=A:
            result = MakeNumberPositive(m*A - n*B)
            check=0
            while check<A:
                if result==check+1 and list_m[check]==0 and list_n[check]==0:
                    list_m[check]=m
                    list_n[check]=n
                check+=1
            n+=1
        m+=1
        
    c = 0
    while c<A:
        print("|"+str(list_m[c])+"X"+str(A)+" - "+str(list_n[c])+"X"+str(B)+"| = "+str(c+1))
        c+=1

def MakeNumberPositive(num):
    if num >= 0:
        return num
    else:
        return num * (-1)


def GetGCD(a, b):
    #유클리드 호제법
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


if __name__ == "__main__":
    main()