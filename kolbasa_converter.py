import os

amo, names = int(input()), input()

os.mkdir('out')

#os.system('ls')

#os.system('for n in `for m in \`ls \"' + names + '\"*\`; do echo \"$m\"; done`; do cp \"$n\" `echo \"$n\" | tr \" \" _`; done')

#names.replace(' ', '_')

for i in range(1, amo + 1):
	if (i < 10 and amo >= 10):
		os.system('jpegtopnm ' + names + '_0' + str(i) + '.jpg > ' + 'out/0' + str(i) + '.pnm')
	else:
		os.system('jpegtopnm ' + names + '_' + str(i) + '.jpg > ' + 'out/' + str(i) + '.pnm')

os.system("pnmcat -tb `for n in \`ls out\`; do echo out/$n; done` | pnmtotiff -packbits > result.tiff")
os.system('rm -rf out')