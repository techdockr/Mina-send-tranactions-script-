# Mina-send-tranactions-script-
Run this script on the Mina node. 
It will help you to make scheduled transactions. 
You need to install python on the host 
It is important to unlock your key before running script 
sudo docker exec -it mina bash

export KEYPATH=$HOME/keys/my-wallet
coda accounts import -privkey-path $KEYPATH

export MINA_PUBLIC_KEY=$(cat $HOME/keys/my-wallet.pub)
coda accounts unlock -public-key $MINA_PUBLIC_KEY
Also add your key  to the value pubkey =
