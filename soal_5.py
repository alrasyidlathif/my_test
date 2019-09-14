import random

def cetak(n):

    list_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    
    list_string = []
    for i in range(n):
        stringku = ''
        for j in range(32):
            i_random = random.randint(0,len(list_char)-1)
            stringku += list_char[i_random]
        list_string.append(stringku)

    set_string = set(list_string)
    if len(set_string) == len(list_string):
        print('tidak ada string yang sama')
    else:
        print('ada string yang sama')

    print('================================')

    for s in list_string:
        print(s)


if __name__ == '__main__':
    cetak(10)
