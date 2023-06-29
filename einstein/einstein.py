def main():
    m = int(input("m: "))
    c = square(300000000)
    E = m*c
    print(E)

def square(n):
    return n*n

main()