# NFT-Characters-Auction
This is a NFT characters auction website.

1.Download the frontend. 
Use 

$npm install i 

to install all the dependencies.
Use

$npm start

to start the service


2.Download the contract. 
Use 

$npm install i 

to install all the dependencies.
Use

$truffle migrate --network development

to submit your contract to block chains

3.download "python" file
This is just for touch the block chain regularly to upload the local time if you test your contract on the loacl chain.
Use

$python eb.py

to start

##
To start correctly, you need to change the config information to your own loack netword.
In frontend, you need to change the abi and contract address in ./src/pages/Login/eth.js
In python, you need to change the abi in config.py, contract address in contract.py
