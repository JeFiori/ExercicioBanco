def main():

    l = [0,0,0,0,0,0,0,0,0,0]
    num = 0

    for cont in range(15):

        n = int(input("Digite um número entre 1 e 10: "))
        l[n-1] = l[n-1] + 1

    while num < 10:

        if l[num] == 1:
            print("O número %d apareceu 1 vez." % (num+1))

        else:
            print("O número %d apareceu %d vezes." % ((num+1),l[num]))
        num = num + 1


print(main())