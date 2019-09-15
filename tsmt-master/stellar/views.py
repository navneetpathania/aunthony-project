from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
import requests,sys,qrcode,os
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from stellar_base.builder import Builder
from stellar_base.horizon import Horizon
from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from .forms import ContactForm,FeedbackForm,AccountForm
from .models import Accounts, Contact


network_data = ['https://horizon-testnet.stellar.org','https://horizon.stellar.org']
SITE_ADDR = 'GAFNKWN2GX7FCCSYLS36OUN2NIWJAU4UVZC44MVTQQX6HDAUZ2UUQL6I'
SITE_SEED = 'SCC2V25EPMDLWUXNOJNLTBFXMWDHLLNJOY4DN5LWIEKFMYADNPW2OFXX'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
@login_required()
def index(request):
    return render(request, 'base.html')

# @login_required
# def send(request):
#     account = request.GET.get('account')
#     user = request.GET.get('user')
#     currency = request.GET.get('currency')
#     r = {'account': account, 'user': user,'currency': currency}
#     print("rrr : ",r)
#     return render(request, 'stellar/send.html', r)
@login_required
def send(request):
    if request.method == "POST":
        account = request.POST['to_addr']
        user = request.POST['to_user']
        currency = request.POST['currency']
        amount = request.POST['amount']
        from_address = Accounts.objects.get(user_name=request.user)
        sender = from_address.seed
        # r = {'account': account, 'user': user,'currency': currency}
        return send_payment(request,amount,currency,sender,account)
    return render(request, 'stellar/send.html')

def send_contact(request,id,):
    if request.method == "POST":
        account = request.POST['to_addr']
        user = request.POST['to_user']
        currency = request.POST['currency']
        amount = request.POST['amount']
        from_address = Accounts.objects.get(user_name=request.user)
        sender = from_address.seed
        return send_payment(request, amount, currency, sender, account)
    send_detailes = Contact.objects.get(id=id)
    return render(request, 'stellar/send.html', {'send_detailes': send_detailes})

def send_payment(request,amount,currency,sender,account):
    builder = Builder(secret=sender)
    builder.append_payment_op(account,amount,currency)
    builder.add_text_memo("first payment")
    builder.sign()
    s = builder.submit()
    print(s['_links'])
    return HttpResponse("send successfully plz check user transaction here")



@login_required
def get_contacts(request):
    r = Contact.objects.all()
    return render(request, 'stellar/get_contacts.html', {'r': r})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.user_name = request.user
            #post.created = timezone.now()
            post.save()
            message = _("thank you for your contact")
        else:
            message = _("sorry something went wrong")
        context = {'success': message}
        return render(request, 'stellar/create_contact.html', context)
    if request.method =='GET':
        form = ContactForm()
        return render(request, 'stellar/create_contact.html', {'form': form})

@login_required
def contact_delete(request,id):
    Contact.objects.filter(id=id).delete()
    # contact = request.GET.get('contact')
    # if contact:
    #     r = get_object_or_404(Contact,user_name=request.user,contact=contact)
    #     #r = Contact.objects.filter(user_name=request.user,contact=contact)
    #     if r:
    #         print("delete")
    #         print(r)
    #         r.delete()
    #     else:
    #         message = _("sorry something went wrong")
    #         context = {'success': message}
    # else:
    #     print("TEST")
    # x = Contact.objects.filter(user_name=request.user)
    return redirect ('/stellar/get_contacts')

@login_required
def request(request):
    user = Accounts.objects.get(user_name=request.user)
    account =user.address
    file = str(account)+".png"
    r = {'img':str(file),'account': account}
    print(r)
    return render(request, 'stellar/request.html',{'r': r})
# @login_required
# def accountdetails(request):
#     hz = Horizon()
#     url = "https://horizon-testnet.stellar.org/account"
#     user = Accounts.objects.filter(user_name=request.user)
#     address = user[0].address # = 'GDVRS4JT7QUXBYOZWDAJEQUBJC5L74Q5ASDYK5HROOGJHNBUVKB6CNGW'
#     # r = hz.account(address)
#     r = url + str(address)
#     print(r)
    # return render(request, 'stellar/accountdetails.html',{'r': r})

@login_required
def keys(request):
    user = Accounts.objects.filter(user_name=request.user)
    address = user[0].address
    secret_key = user[0].seed
    r = {'address':address,'secret_key':secret_key}
    print(r)
    return render(request, 'stellar/keys.html',{'r':r})


def importaccount(request):
    user = Accounts.objects.get(user_name=request.user)
    print(user)
    print("username: ",user.user_name)
    print(f'name {user.name}')
    print(f'account_id {user.address}')
    context = {
        'username':user.user_name,
        'name':user.name,
        'addres':user.address,
        'seed':user.seed
    }
    return render(request,'stellar/import_account.html',context)

@login_required
def qrcode_gen(request):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    user = Accounts.objects.get(user_name=request.user)
    address = user.address
    qr.add_data(address)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    file =os.path.join(BASE_DIR,'static') + "/qr/" + str(address)+".png"
    img.save(file)
    return file

@login_required
def transactions(request):
    a = Accounts.objects.filter(user_name=request.user)
    address = a[0].address # = 'GDVRS4JT7QUXBYOZWDAJEQUBJC5L74Q5ASDYK5HROOGJHNBUVKB6CNGW'
    hz = Horizon()
    r = hz.account_payments(address)
    x = r['_embedded']['records']
    r = {'r': x,'address': address}
    print(r)
    return render(request, 'stellar/transactions.html', r)


@login_required
def accounts(request):
    try:
        user = Accounts.objects.filter(user_name=request.user)
        username = user[0].user_name
        address = user[0].address
        seed = user[0].seed
        name = user[0].name
        r = {'username':username, 'address':address, 'seed':seed, 'name':name}
        return render(request, 'stellar/accounts.html',{'r': r})
    except:
        return render(request, 'stellar/accounts.html')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if(form.is_valid()):
            print(request.POST['username'])
            print(request.POST['message'])
            message = "thank you for your feedback"
        else:
            message = "sorry something went wrong"
        context = {'success': message}
        return render(request, 'stellar/contact.html', context)
    if request.method =='GET':
        form = FeedbackForm()
        return render(request, 'stellar/contact.html', {'form': form})

def results(request, account_id):
    response = "You're looking at the results of account_id %s."
    return HttpResponse(response % account_id)

def detail(request, str_addr):
    hz = Horizon()
    r = hz.account(str_addr)['balances']
    print(r)
    x = {'r': r}
    #return HttpResponse("You're looking at question %s." % r)
    return render(request, 'stellar/accountdetails.html', x)

def accountdr(request, account_addr):
    hz = Horizon()
    if account_addr is None:
        address_addr = 'GDVRS4JT7QUXBYOZWDAJEQUBJC5L74Q5ASDYK5HROOGJHNBUVKB6CNGW'
    r = hz.account(address_addr)['balances']
    print(r)
    x = {'r': r}
    return render(request, 'stellar/accountdetails.html', x)

@login_required
def accountdetails(request):
    try:
        # hz = Horizon()
        user = Accounts.objects.filter(user_name=request.user)
        address = user[0].address
        url = 'https://horizon-testnet.stellar.org/accounts/' + address
        r = requests.get(url)
        r= str(r.text).replace('true','True').replace('false','False')
        r = eval(r)
        r = r['balances']
        # r = hz.account_transactions(address)
        # print(r['_embedded']['records'])
        # r = {'r': r}
        # r['address'] = address
        print(r)
        # return HttpResponse(r)
        return render(request, 'stellar/accountdetails.html', {'r':r})
    except:
        return render(request, 'stellar/accountdetails.html')

@login_required
def create_fund(request):
    user = Accounts.objects.filter(user_name=request.user)
    address = user[0].address
    r = requests.get('https://horizon-testnet.stellar.org/friendbot?addr=' + address)
    return HttpResponseRedirect('/stellar/accountdetails/')

def offers(request):
    # hz = Builder()
    # params = {
    # 'selling_asset_type': 'native', 'buying_asset_type':'credit_alphanum4',
    # 'buying_asset_code': 'AAA',
    # 'buying_asset_issuer': 'GAX4CUJEOUA27MDHTLSQCFRGQPEXCC6GMO2P2TZCG7IEBZIEGPOD6HKF'
    # }
    # print("builder : ",builder)
    # r = builder.order_book(params=params)
    user = Accounts.objects.filter(user_name=request.user)
    address = user[0].address
    selling_asset_type = 'native'
    buying_asset_type = 'credit_alphanum4'
    buying_asset_code = 'AAA'
    buying_asset_issuer = address
    url = 'https://horizon-testnet.stellar.org/order_book?selling_asset_type=native&buying_asset_code=AAA&buying_asset_type=credit_alphanum4&addr={}'.format(address)
    r = requests.get(url)
    r = str(r.text).replace('true','True').replace('false','False')
    r = eval(r)
    return render(request, 'stellar/offer.html',r)

def results(request, account_id):
    response = "You're looking at the results of account_id %s."
    return HttpResponse(response % account_id)

@login_required
def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        account_id = request.POST['account_id']
        seed = request.POST['seed']
        print("Get data..")
        if username:
            message = _("You account is successfully created")
        else:
            message = _("sorry something went wrong")
        context = {'success': message, 'username':username,'name':name ,'account_id':account_id, 'seed':seed}
        return render(request, 'stellar/accounts.html', {'context':context})
    user = Accounts.objects.filter(user_name=request.user)
    address = user[0].address
    seed = user[0].seed
    name = user[0].name
    r = {'account_id':address, 'seed':seed, 'name':name }
    return render(request, 'stellar/accountcreate.html', {'r':r})

@login_required
def get_keys(request):
    user = Accounts.objects.filter(user_name=request.user)
    public_key = user[0].address
    secret_key = user[0].seed

    keys = {'public_key':public_key,'secret_key':secret_key}
    print(keys)
    return render(request,'stellar/keys.html',{'keys':keys})
