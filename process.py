import json

les_mis = json.load(open('miserables.json', 'r'))

char_dict = {j['id']: i for i, j in enumerate(les_mis['nodes'])}

mis = dict()
mis['nodes'] = (
    [{
        'id': char_dict[i['id']]
        ,'group': i['group']
        ,'name': i['id']} for i in les_mis['nodes']]
)
mis['links'] = (
    [{
        'source': char_dict[i['source']]
        ,'target': char_dict[i['target']]
        ,'value': i['value']} for i in les_mis['links']]
)

json.dump(mis, open('miserables_2.json', 'w'))

