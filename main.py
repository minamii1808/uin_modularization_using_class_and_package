nama = 'Minami Candrika Hamada'
program = 'Momentum dan Impuls'
print(f' program {program} oleh {nama}')

def hitung_momentum(massa, kecepatan):
    momentum = massa * kecepatan
    print(f'momentum = {massa}kg dibutuhkan dalam {kecepatan}m/s')
    print(f'sehingga momentum = {momentum}kgm/s')
    return massa * kecepatan

# massa = 450
# kecepatan = 35
momentum = hitung_momentum(450, 35)
momentum = hitung_momentum(380, 45)

def hitung_impuls(gaya, perubahanselangwaktu):
    impuls = gaya * perubahanselangwaktu
    print(f'impuls ={gaya}N dibutuhkan dalam {perubahanselangwaktu}s')
    print(f'sehingga impuls = {impuls}Ns')
    return gaya * perubahanselangwaktu

# gaya = 750
# perubahanseLangwaktu = 20

impuls = hitung_impuls(750, 20)
impuls = hitung_impuls(354, 15)

def hitung_gaya (massa, percepatan):
    gaya = massa * percepatan
    print(f'gaya = {massa}kg dibutuhkan dalan {percepatan}m/s^2')
    print(f'sehingga gaya = {gaya}N')
    return massa * percepatan

# massa = 1800
# percepatan = 10

gaya = hitung_gaya(1800, 10)
gaya = hitung_gaya(2000, 15)



