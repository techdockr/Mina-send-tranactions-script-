import os
import time
import subprocess
import random
import linecache

#publichniy klyuch
pubkey = 'B62qj48bRmvCe7odDkC3ffSQZXFxZoWVy1Cx8qpzbg7QVtne9xi6E2G'

#diapzon sekundax chtobi tranzaksii otpravilis kajdiy n sekund
period = random.randint(5, 12)

#skolko sikl nujno
sikl  = 300

#komisia naibole luchshaya
tfee = random.randint(243, 288)

#podklyuchayemsya k uzelu Synced
def main():
	codast = 'mina client status'
	stprocess = subprocess.Popen(codast, shell = True)
	output, error = stprocess.communicate()
	stprocess.wait()
	time.sleep(300)

	#chitayem skolko strok est .txt fayle
	with open('address.txt') as f:
		text = f.readlines()
		size = int(len(text))

	i=0
	while True:
		if i >= sikl:
			break
		i+=1
		#randomna viberayem address dlya otpravki tranzaksii
		ranad = random.randint(1, size)
		print(ranad)
		#otkrivayem stroka iz txt fayla randomna
		sendadd = str(linecache.getline('address.txt', ranad)).replace('\n', '')
		print(sendadd)

		#razbalkariyum akkaunt
		unac = ('mina accounts unlock -public-key ' + pubkey)
		process = subprocess.Popen(unac, shell = True)
		output, error = process.communicate()
		process.wait()

		#otpravlyayem tranzaksii

		sentok = 'mina client send-payment \
		-amount 0.5 \
		-receiver ' + sendadd + ' \
		-fee ' + str(tfee) + ' \
		-sender ' + pubkey
		processtwo = subprocess.Popen(sentok, shell = True)
		output, error = processtwo.communicate()
		processtwo.wait()

		#jdyom 60 sekund i povtorayem sikl
		time.sleep(period)


if __name__ == '__main__':
	main()

# codast = 'coda client status'
# stprocess = subprocess.Popen(codast, shell = True)
# output, error = stprocess.communicate()
# stprocess.wait()
# time.sleep(30)

# unac = 'coda accounts unlock -public-key B62qnQvWhcqDewRE7XKArixgqgMoLf7ftPeQbU1dLtFSfi1EdVacmKM'
# process = subprocess.Popen(unac, shell = True)
# output, error = process.communicate()
# process.wait()

# sendadd='B62qpPpNjFD2L87EKyd8KstBeDeaLTTXDtPr7cS3XZCDuRimJFb3LUH'
# sentok = 'mina client send-payment \
#   -amount 0.5 \
#   -receiver ' + sendadd + ' \
#   -fee 130 \
#   -sender B62qnQvWhcqDewRE7XKArixgqgMoLf7ftPeQbU1dLtFSfi1EdVacmKM'
# processtwo = subprocess.Popen(sentok, shell = True)
# output, error = processtwo.communicate()
# processtwo.wait()


# expubkey = ['export KEYPATH=$HOME/keys/my-wallet']
# process = subprocess.Popen(expubkey, shell = True, text=True)
# output, error = process.communicate()

# impubkey = ['coda accounts import', '-privkey', '-path', '$KEYPATH']
# process = subprocess.run(impubkey, shell = True, stdout=subprocess.PIPE)


# expubkey = ['export', 'KEYPATH=$HOME/keys/my-wallet']
# process = subprocess.run(expubkey, shell = True)
# com1 = os.system('coda client status')
# print(com1)

# time.sleep(5)

# com2 = os.system('export KEYPATH=$HOME/keys/my-wallet')
# print(com2)
# print('vipolnena 1')
# com3 = os.system('coda accounts import -privkey-path $KEYPATH')
# print(com3)
# print('vipolnena 2')
# time.sleep(5)
# com4 = os.system('export MINA_PUBLIC_KEY=$(cat $HOME/keys/my-wallet.pub)')
# print(com4)
# time.sleep(5)
# com5 = os.system('coda accounts unlock -public-key $MINA_PUBLIC_KEY')
# print(com5)


# inrec = 'B62qnF9UD3HcPV3K5vVVxaWY3M1rXBJVenNxqFaTaFJkiSW7jBgZRRx'
# com6 = os.system('coda client send-payment \n-amount 0.1 \n-receiver ' + inrec + ' \n-fee 130 \n-sender $MINA_PUBLIC_KEY')
# print(com6)
