from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from models import AppotaGameUser
from django.http import HttpResponse,HttpRequest
import hashlib
import pdb
client_secret_ios_itunes = "client_secret"
client_secret_ios_appvn = "client_secret"
client_secret_android_appvn = "client_secret"
client_secret_android_gplay = "client_secret"

class GameUserResource(ModelResource):
    class Meta:
        queryset = AppotaGameUser.objects.all()
        resource_name = 'game_user'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization= Authorization()

# Verify and then increase gold for transaction
def proceed_transaction(querydict, client_secret):
    verify_status = verify_transaction(querydict, client_secret)
    if verify_status:
        charge_transaction(querydict)
    else:
        return HttpResponse(status=200)
# State in this case is defined by splitting with character "|"
# For exampe: game_user_name|server_playing|game_currency|
def get_game_currency(state):
    game_currency = str(state).split("|")[2]
    return game_currency

def get_game_user_name(state):
    game_currency = str(state).split("|")[0]
    return game_currency

def get_game_server(state):
    server = str(state).split("|")[1]
    return server

# Return mouney amount in VND
# 1 USD = 21000 VND
def money_to_vnd(money_amount, money_currency):
    if money_currency == "USD":
        return (int) (money_amount * 21000)
    return money_amount

# Corresponding to each money amount -> number of game currency
# 1 coin <-> 100 vnd, 1 gold <-> 500 vnd, 1 ruby <-> 1000 vnd,  1 diamond <-> 5000 vnd, vip <-> 50000 vnd, month_card <-> 100000
def get_game_amount(game_currency, money_amount, money_currency="VND"):
    money_amount_vnd = money_to_vnd(money_amount, money_currency)
    if game_currency == "coin":
        return money_amount_vnd/100
    if game_currency == "gold":
        return money_amount_vnd/500
    if game_currency == "ruby":
        return money_amount_vnd/1000
    if game_currency == "diamond":
        return money_amount_vnd/5000
    if game_currency == "vip":
        return money_amount_vnd/50000
    if game_currency == "month_card":
        return money_amount_vnd/10000

def charge_transaction(querydict):
    money_amount = querydict["amount"]
    money_currency = querydict["currency"]
    state = querydict["state"]
    game_currency = get_game_currency(state)
    game_user_name = get_game_user_name(state)
    game_user_server = get_game_server(state)
    # Number of game amount will be increased
    game_amount = get_game_amount(game_currency, money_amount, money_currency)
    # Get game_user from server
    current_game_amount = getattr(game_user, game_currency)
    setattr(game_user, game_currency, current_game_amount+game_amount)


def get_game_user(game_user_name, game_user_server):
    list_user = AppotaGameUser.objects.filter(username=game_user_name, server=game_user_server)
    print list_user
    if len(list_user) == 0:
        # Create user
        game_user = AppotaGameUser(username=game_user_name, server=game_user_server)
        game_user.save()
    return AppotaGameUser.objects.filter(username=game_user_name, server=game_user_server)[0]

def verify_transaction(querydict, client_secret):
    pdb.set_trace()
    # Sort all key for dictionary by alphabe
    sorted(querydict)
    # Get hash from appota server
    appota_hash = querydict["hash"]
    # Remove hash from dictionary
    querydict.pop("hash", None)
    # Create hash to compare from query dict
    input_hash = ""
    for value in querydict.values():
        input_hash += str(value)
    input_hash += client_secret
    output_hash = hashlib.md5(input_hash).hexdigest()
    if output_hash != appota_hash:
        # Invalide hash
        return False
    else:
        return True

def dict_from_querydict(querydict):
    dict = {}
    for k,v in querydict.items():
        dict[k] = v
    return dict
def notice_url_ios_appvn(request):
    proceed_transaction(dict_from_querydict(request.POST), client_secret_ios_appvn)

def notice_url_ios_itunes(request):
    proceed_transaction(dict(request.POST.iterlists()), client_secret_ios_itunes)

def notice_url_android_appvn(request):
    proceed_transaction(request.POST, client_secret_android_appvn)

def notice_url_android_gplay(request):
    proceed_transaction(request.POST, client_secret_android_gplay)


# def notice_url(request):
#     uname = request.POST["username"]
#     status = request.POST["status"]
#     sandbox = request.POST["sandbox"]
#     transaction_id = request.POST["transaction_id"]
#
#     list_user = AppotaGameUser.objects.filter(username=uname)
#     print list_user
#     if len(list_user) == 0:
#         # Create user
#         game_user = AppotaGameUser(username=uname)
#         game_user.save()
#     else:
#
#     return HttpResponse("OK")


