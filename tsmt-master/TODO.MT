#TODO
For developers to understand how this should work please register at lobstr.co to see another wallet.

Will contain remittance SEO information
Contain status check for Western union, WARI and Ria Transfers

A crypto wallet designed to supported

    • Facebook basic – for 100 million users who don’t have normal internet
    • Bitcoin lightening – for faster transactions
    • Stellar wallet functions
    • Google AMP 

    • Pages will be designed for low quality internet – max 80 kb per page
    • No Javascript
    • No SVG Images
    • Work on mobile/desktop

https://developers.facebook.com/docs/internet-org/how-to-submit/

Translated into 

Languages English:

(India, Kenya, Zambia, Indonesia, Tanzania, and Nigeria, Ph

French:
Senegal, Morocco


#background
Wallet made using django
sqlite for testing
postgresql for live
redis for queing if required
emails using amazon sqs


## Goals for v 0.1 of the application
1) Make python3 compatible and django 2.2
fix 
'django.contrib.auth.middleware.AuthenticationMiddleware' must be in MIDDLEWARE in order to use the admin application.
?: (admin.E409) 'django.contrib.messages.middleware.MessageMiddleware' must be in MIDDLEWARE in order to use the admin application.

2) Clean up code and make pep6 compatible
3) Move to version 2 of python library
Move logging to logging modual
https://github.com/StellarCN/py-stellar-base


v0.11
Better encryption of private key following stellar wallet guidelines (AES encryted)

Wallet must refuse any weak passphrase.
    • Wallet must lock out accounts due to multiple failed login attempts.
    • Wallet must provide a strict account recovery process.
    • https://github.com/ethereum/wiki/wiki/Web3-Secret-Storage-Definition

v0.2
5) Change account creation process to look like lobstr
(funds locked until funded)
6) Reference transactions from https://github.com/orbitlens/stellar-expert-explorer to make sure that memo fields are ok
7) Follow wallet guidelines where necessary
https://www.stellar.org/community/wallet-guidelines
Clean up layout

Support OTP if possible (2FA) via sms text or google authentication
facebook login
Autofund option like lobstr wallet

v0.3
Lookup western union transferred
3) allow facebook registration (if no javascript)
Ria
Translate to FR
Submit to facebook basics program

v0.5
https://stackoverflow.com/questions/35091546/accelerated-mobile-pages-in-django
path payments
https://www.stellar.org/developers/horizon/reference/resources/path.html



- GIT
- NAV Accordian - I guess we need to just use templates...



- display balance is various currencies
- display buys and sells in the blockchain
- send money
- request money via email
- create account - add to db
-
- celery
- login user (part 2)
- create login



TEMPO - "Open Remittance". What does open remittance mean? It means a fully KYC compliant open payment rail for retmittance.
CRM pas Uim3ahzaem
