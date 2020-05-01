vm=int(input('Digite um número em metros para conversão: '))
vkm=vm*0.001
vhm=vm*0.01
vdam=vm*0.1
vdm=vm*10
vcm=vm*100
vmm=vm*1000
print('{} metro(s) equivale(m) curso_em_video_estruturas_de_controle {} cm, ou {} mm, ou {} dm, ou {} dam, ou \n'
      '{} hm, ou {} km.'.format(vm,vcm,vmm,vdm,vdam,vhm,vkm))