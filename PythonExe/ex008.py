print('============Matématicamente falando=================')
metros = float(input(f'Bem vindo diga-nos, quantos metros de fio você deseja converter? : '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
cent = metros * 100
milim = metros * 1000
diam = metros * 10

print(f'Perfeito, você tem {metros} metros de fio, considerando isso, você ', end=' ')
print(f'tem ao todo {cent} em centimetros, também pode considerar')
print(f' {milim} em milimetros, {diam} em diamêtros, {dam}DAM em dam, {hm}HM em HM\n')
print(f'e em kilometros {km}KM')

