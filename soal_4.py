import math

def cetak_gambar(n):

    if n < 1:
        print('error, parameter harus lebih dari nol.')
        return
    if n % 2 == 0:
        print('error, parameter harus merupakan bilangan ganjil.')
        return

    m = math.floor(n/2)
    l = n - 2

    if n > 1:
        print((n-m-2)*' ' + l*'- ' + (m)*' ' + 'panjang' + (m)*' ' + l*' -' + (n-m-2)*' ')

        for i_atas in range(m):

            print('*', end='')
            print(l*'     =', end='')
            print('     ', end='')
            print('*')
    
        print((n-1)*'*     ', end='')
        print('*')

        for i_bawah in range(m):
    
            print('*', end='')
            print(l*'     =', end='')
            print('     ', end='')
            print('*')

    else:
        print(0*' ' + m*' ' + 'panjang' + m*' ' + 0*' ')
        print('*')


if __name__ == '__main__':
    cetak_gambar(13)
