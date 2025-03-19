m = float(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('As conversões da medida de {}m, corresponde a:'
      '\n{:.5f}km'
      '\n{:.4f}hm'
      '\n{:.3f}dam'
      '\n{:.2f}dm'
      '\n{:.2f}cm'
      '\n{:.2f}mm'
      .format(m, km, hm, dam, dm, cm, mm))
