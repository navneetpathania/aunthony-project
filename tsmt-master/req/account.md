

# User story for creating account

create configuration

1) user clicks on Accounts/Balances
2) A button should be for create account and one for import account.



## CREATE


View function create_account should create the users account

It should read if the NETWORK variable is PUBLIC or TESTNET (which I added to settings.py

a new account  
https://www.stellar.org/developers/guides/concepts/accounts.html  


https://github.com/StellarCN/py-stellar-base/blob/master/examples/create_keypair.py

    from stellar_base.keypair import Keypair
    kp = Keypair.random()
    #Each key as a public and private key
    public_key = kp.address().decode('ascii')
    private_key = kp.seed().decode('ascii'
`
A stellar account is created but not active until funded.  

if the network is TESTNET it should be funded automatically by doing an http get with the public key  
r = requests.get('https://friendbot.stellar.org/?addr=' + public_key'  

- There should be a button to display private key once it is funded on the testnet
- If this is live (PUBLIC) then it should display the private key only if the XLM balance is larger than 2.2 if the XLM balance is less than 2.51 it should display.
- You need to topup your wallet to display your balance. To top up your wallet visit tempo.eu.com

The private key needs to be stored encrypted!  
https://pypi.org/project/django-encrypted-model-fields/

    from encrypted_model_fields.fields import EncryptedCharField
    class EncryptedFieldModel(models.Model):
        encrypted_char_field = EncryptedCharField(max_length=100)

- Accounts should be a one to many table
- One user can have multiple accounts and switch between them.


## IMPORT ACCOUNT

- ONE field should be displayed
- private_key
- From the private key the public key can be gotten with Stellar Account
- It should be stored encrypted


### BALANCES OF THE WALLET SELECTED SHOULD BE DISPLAYED

- icon (from ASSETS in the settings.py) NAME BALANCE

code should be something like:  
https://github.com/antb123/stcli/blob/master/stcli.py#L176



    c = Address(CONF['public_key'], network=CONF['network'])
    try:
        c.get()
    except AccountNotExistError:
        print_formatted_text(HTML('<ansiyellow>unfunded account... </ansiyellow> ' +
                             'you need to hit <ansiblue>f to fund for testnet or type key for public</ansiblue> '))
    
    #  print('.. rate ' + str(rate))
    for x in c.balances:
        if x['asset_type'] == 'native':
            if check_asset != '': continue
            usd_val = float(rate['price_usd']) * float(x['balance'])
            print_formatted_text(HTML('XLM: <ansiblue>' + x['balance'] + '</ansiblue> value: USD:' + "{:.2f}".format(usd_val)
                  + ' EUR:' + "{:.2f}".format(eur_val)))
        else:
            if check_asset != '':
                if check_asset.upper() == x['asset_code'].upper():
                    return True
            else:
                print_formatted_text(HTML(x['asset_code'] + ' <ansiblue>' + x['balance'] + '</ansiblue>'))
    if check_asset != '': return False







