from django.shortcuts import render,redirect,HttpResponse
from web import models
import datetime
from django_redis import get_redis_connection
import json
from utils.encrypt import uid
# from utils.alipay import AliPay
from django.conf import settings

def index(request):

    return render(request, 'index.html')

def backend(request):

    return render(request, 'project_list.html')

def price(request):
    policy_list = models.PricePolicy.objects.filter(category=2)
    return render(request,'price.html',{'policy_list':policy_list})

def payment(request,policy_id):
    policy_object = models.PricePolicy.objects.filter(id=policy_id,category=2).first()
    if not policy_object:
        return redirect('price')
    number = request.GET.get('number','')
    if not number or not number.isdecimal():
        return redirect('price')
    number = int(number)
    if number < 1:
        redirect('price')
    origin_price = number * policy_object.price

    balance = 0
    _object = None
    if request.tracer.price_policy.category == 2:
        # 找到之前订单：总支付费用 、 开始~结束时间、剩余天数 = 抵扣的钱
        # 之前的实际支付价格
        _object = models.Transaction.objects.filter(user=request.tracer.user, status=2).order_by('-id').first()
        total_timedelta = _object.end_datetime - _object.start_datetime
        balance_timedelta = _object.end_datetime - datetime.datetime.now()
        if total_timedelta.days == balance_timedelta.days:
            # 按照价值进行计算抵扣金额
            balance = _object.price_policy * price * _object.count / total_timedelta.days * (balance_timedelta.days - 1)
        else:
            balance = _object.price_policy * price * _object.count / total_timedelta.days * balance_timedelta.days

    if balance >= origin_price:
        return redirect('price')

    context = {
        'policy_id': policy_object.id,
        'number': number,
        'origin_price': origin_price,
        'balance': round(balance, 2),
        'total_price': origin_price - round(balance, 2)
    }
    conn = get_redis_connection()
    key = 'payment_{}'.format(request.tracer.user.mobile_phone)
    conn.set(key, json.dumps(context), ex=60 * 30)
    context['policy_object'] = policy_object
    context['transaction'] = _object

    return render(request, 'payment.html', context)

def pay(request):
#     conn = get_redis_connection()
#     key = 'payment_{}'.format(request.tracer.user.mobile_phone)
#     context_string = conn.get(key)
#     if not context_string:
#         return redirect('price')
#     context = json.loads(context_string.decode('utf-8'))
# #生成订单,更新订单状态为已支付,计算开始和结束时间
#     order_id = uid(request.tracer.user.mobile_phone)
#     total_price = context['total_price']
#     models.Transaction.objects.create(
#         status=1,
#         order=order_id,
#         user=request.tracer.user,
#         price_policy_id=context['policy_id'],
#         count=context['number'],
#         price=total_price
#     )
#     #跳转到支付宝支付
#     # 生成支付链接
#     ali_pay = AliPay(
#         appid=settings.ALI_APPID,
#         app_notify_url=settings.ALI_NOTIFY_URL,
#         return_url=settings.ALI_RETURN_URL,
#         app_private_key_path=settings.ALI_PRI_KEY_PATH,
#         alipay_public_key_path=settings.ALI_PUB_KEY_PATH
#     )
#     query_params = ali_pay.direct_pay(
#         subject="trace rpayment",  # 商品简单描述
#         out_trade_no=order_id,  # 商户订单号
#         total_amount=total_price
#     )
#     pay_url = "{}?{}".format(settings.ALI_GATEWAY, query_params)
#     return redirect(pay_url)
    return HttpResponse({})






















