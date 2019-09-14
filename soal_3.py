def num_of_frasa(stringku, kata):

    if len(kata) > len(stringku):
        print('panjang kata tidak boleh lebih dari panjang string')
        return

    dibalik = 1
    kata2 = kata
    kata2 = list(kata2)
    kata2.reverse()
    kata2 = ''.join(kata2)
    if kata == kata2:
        dibalik = 0

    stringku = stringku.lower()
    kata = kata.lower()

    n_frasa = 0
    end_point = len(stringku) - len(kata)

    for i in range(0,end_point+1):
        if kata == stringku[i:i+len(kata)]:
            n_frasa += 1

    if dibalik == 1:
        stringku = list(stringku)
        stringku.reverse()
        stringku = ''.join(stringku)
        for i in range(0,end_point+1):
            if kata == stringku[i:i+len(kata)]:
                n_frasa += 1

    print('ditemukan', str(n_frasa), 'kali')


if __name__ == '__main__':
    num_of_frasa('banananana', 'nAna')
    num_of_frasa('a','a')
    num_of_frasa('Lathif Al Rasyid', 'al')
    num_of_frasa('bananananaa', 'nan')
    num_of_frasa('bananananaa', 'aa')
