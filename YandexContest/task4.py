markets, billing = [open(i) for i in input().split()]
print('order_id,shop_name,shop_id,cost')
markets = markets.read().rstrip().split('\n')[1:]
billing = billing.read().rstrip().split('\n')[1:]
for i in markets:
    for j in billing:
        shop_id, shop_name = i.split(',')
        order_id, shop_id_2, cost = j.split(',')
        if shop_id == shop_id_2:
            print(f'{order_id},{shop_name},{shop_id},{cost}')
