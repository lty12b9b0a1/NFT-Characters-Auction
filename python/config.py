from web3 import Web3

SETTING = {
    "ROPSTEN_URL": "https://ropsten.infura.io/v3/XXX",
    "MAINNET_URL": "http://127.0.0.1:8545",
    "CONTRACT_ADDRESS": "0xa76c47F40472dE3e21a1D37bb7325eedD9B36397",
    "WALLET_PRIVATEKEY": "4f3871f9da597f345e5c4ff1a78b224b00a221bda3a762d0f92078b626c118f6",
    "WALLET_ADDRESS": "0x48CDe04640688E90023eAa7e482A8B909f89aAF9",
    "TIME_SPAN": 100
}

w3 = Web3(Web3.HTTPProvider(SETTING["MAINNET_URL"]))


def sendTransation(tx_dic):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


def sendTransationWithMoreGas(tx_dic, gwei):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic['nonce'] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)
