# coding:utf-8
import sys
sys.path.append('.')

import qrcode
from stellar_base.operation import Payment
from stellar_base.asset import Asset
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.keypair import Keypair
from stellar_base.memo import *
from stellar_base.horizon import Horizon

url = 'https://horizon-testnet.stellar.org'

# Only for sample 'requests' and 'simplejson' are required.
import requests
import json

def newAccount(creator=False):
    kp = Keypair.random()
    r = requests.get(url + '/friendbot?addr=' + kp.address().decode('ascii')) # Get 1000 lumens
    assert 'hash' in json.loads(r.text)
    return {
        'address': kp.address().decode('ascii'),
        'seed': kp.seed().decode('ascii')
    }


# send anna usd
def send_asset(amt, from_addr, to_addr, asset_nm):
    asset = Asset(asset_nm, issuer_addr)
    tx = Transaction(source=from_addr['address'], opts={'sequence': str(get_sequence(from_addr['address'])), 'fee': 100})
    pay_dic = {'destination': to_addr['address'],'asset': asset, 'amount': str(amt)}
    tx.add_operation(operation=Payment(pay_dic))
    envelope = Te(tx=tx, opts={"network_id": "TESTNET"})
    envelope.sign(Keypair.from_seed(from_addr['seed']))
    req = hz.submit(te=envelope.xdr())
    print(req)


#send_asset(1,anna1,bob1,'USD')


def get_balances(address):
    hz = Horizon()
    if address is None:
        anna1 = {'address': u'GDVRS4JT7QUXBYOZWDAJEQUBJC5L74Q5ASDYK5HROOGJHNBUVKB6CNGW',
        'seed': u'SDIXGWLFZYV2DJYKJBUBSAC5HP33TGTQ5RKJSRFAQTMTBWUKCE3ATHRJ'}
        address = anna1['address']
    print(address)
    r = hz.account(address)['balances']
    return r
