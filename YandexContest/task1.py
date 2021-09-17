import json
from sys import stdin

file = ''
for line in stdin:
    file += line
try:
    orders = json.loads(file)
    orders.sort(key=lambda x: x['event_id'])
except:
    print(1)
    exit()

output = []
for order in orders:
    try:
        if order['status'] == "OK":
            order_id = order['order_id']
            count = order['count'] - order['return_count']
            item_id = order['item_id']
            if count > 0:
                exist_order = list(filter(lambda x: x['id'] == order_id, output))
                if exist_order:
                    exist_order_index = output.index(exist_order[0])
                    exist_item = list(filter(lambda x: x['id'] == item_id, output[exist_order_index]['items']))
                    if exist_item:
                        output[exist_order_index]['items'][exist_order[0]['items'].index(exist_item[0])]['count'] = count
                    else:
                        output[exist_order_index]['items'].append(
                            {
                                'count': count,
                                'id': item_id
                            }
                        )
                else:
                    output.append(
                        {
                            'id': order_id,
                            'items': [
                                {
                                    'count': count,
                                    'id': order['item_id']
                                }
                            ]
                        }
                    )
            else:
                exist_order = list(filter(lambda x: x['id'] == order_id, output))
                if exist_order:
                    exist_order_index = output.index(exist_order[0])
                    if len(exist_order[0]['items']) > 1:
                        exist_item = list(filter(lambda x: x['id'] == item_id, output[exist_order_index]['items']))
                        if exist_item:
                            output[exist_order_index]['items'].pop(exist_order[0]['items'].index(exist_item[0]))
                    elif output[exist_order_index]['items'][0]['id'] == item_id:
                        output.pop(exist_order_index)

        else:
            order_id = order['order_id']
            item_id = order['item_id']
            exist_order = list(filter(lambda x: x['id'] == order_id, output))
            if exist_order:
                exist_order_index = output.index(exist_order[0])
                if len(exist_order[0]['items']) > 1:
                    exist_item = list(filter(lambda x: x['id'] == item_id, output[exist_order_index]['items']))
                    if exist_item:
                        output[exist_order_index]['items'].pop(exist_order[0]['items'].index(exist_item[0]))
                elif output[exist_order_index]['items'][0]['id'] == item_id:
                    output.pop(exist_order_index)
    except:
        pass
print(json.dumps(output, sort_keys=True, indent=4))
