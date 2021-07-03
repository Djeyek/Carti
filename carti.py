import random
print('h3L0o caRti) vAMP.')
words = ['opIum? ', 'slatT ', 'LiT ', 't0niGht ', 'mOOn ', 'lovv ', 'k1ss ', 'Red. ', 'punK MonK ', 'g0d ', 'WYA wYA wYa ', 'vAMP. ', 'goT. T@nK ', 'mEH ', 'duMmO ',
         'drUnK ', 'YESss ', 'BIO ' , 'LoV3 ', 'tANK ', 'pS. ', 'THOT ', 'oMG ', '💋💋💋 ' , '💔💔 ', '❤❤❤ ', '💋💋💋 ' , '💔💔 ', '❤❤❤ ', '💋💋💋 ' , '💔💔 ', '❤❤❤ ']
lyr = str(input('inPut uR t3Xt'))
place = int(input('wH3re 1 hAve to t@alk (1 - aT the begin 2 - at the enD'))
num = int(input('h0W maNY wOrdS i c0Uld s@y'))
if place == 1:
    print(lyr, ''.join(random.choices(words, k=num)))
if place == 2:
    print( ''.join(random.choices(words, k=num)), lyr)
else:
    print('u aR duMb.')
