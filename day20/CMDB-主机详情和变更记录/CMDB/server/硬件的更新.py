info = {
    'RAM slot #0': {
        'capacity': 2048,
        'slot': 'RAM slot #0',
        'model': 'DRAM',
        'speed': 'Unknown',
        'manufacturer': 'Not Specified',
        'sn': 'Not Specified'
    },

    'RAM slot #2': {
        'capacity': 0,
        'slot': 'RAM slot #2',
        'model': 'DRAM',
        'speed': 'Unknown',
        'manufacturer': 'Not Specified',
        'sn': 'Not Specified'
    },
    'RAM slot #3': {
        'capacity': 0,
        'slot': 'RAM slot #3',
        'model': 'DRAM',
        'speed': 'Unknown',
        'manufacturer': 'Not Specified',
        'sn': 'Not Specified'
    },

}

memory_list = [{'solt': 'RAM slot #0'}, {'solt': 'RAM slot #1'}]

memory_slot_set = set(info)
db_slot_set = {i['solt'] for i in memory_list}

add_slot_set = memory_slot_set - db_slot_set
update_slot_set = memory_slot_set & db_slot_set
delete_slot_set = db_slot_set - memory_slot_set

print(add_slot_set)
print(update_slot_set)
print(delete_slot_set)
