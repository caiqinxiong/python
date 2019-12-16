from repository import models


def process_memory(info, server_list):
    # 更新内存
    memory_info = info['memory']['data']
    server_obj = server_list.first()
    memory_db_info = server_obj.memory_list.all().values('slot')
    memory_slot_set = set(memory_info)
    db_slot_set = {i['slot'] for i in memory_db_info}

    add_slot_set = memory_slot_set - db_slot_set
    update_slot_set = memory_slot_set & db_slot_set
    delete_slot_set = db_slot_set - memory_slot_set

    if add_slot_set:
        memory_obj_list = []
        for slot in add_slot_set:
            data = memory_info[slot]
            memory_obj_list.append(models.Memory(**data, server=server_obj))
        if memory_obj_list:
            models.Memory.objects.bulk_create(memory_obj_list)
    # if update_slot_set:
    #     for slot in update_slot_set:
    #         data = memory_info[slot]
    #         models.Memory.objects.filter(slot=slot, server=server_obj).update(**data)

    if delete_slot_set:
        models.Memory.objects.filter(slot__in=delete_slot_set, server=server_obj).delete()


def process_disk(info, server_list):
    # 更新内存
    disk_info = info['disk']['data']
    server_obj = server_list.first()
    disk_db_info = server_obj.disk_list.all().values('slot')
    disk_slot_set = set(disk_info)
    db_slot_set = {i['slot'] for i in disk_db_info}

    add_slot_set = disk_slot_set - db_slot_set
    update_slot_set = disk_slot_set & db_slot_set
    delete_slot_set = db_slot_set - disk_slot_set

    if add_slot_set:
        disk_obj_list = []
        for slot in add_slot_set:
            data = disk_info[slot]
            disk_obj_list.append(models.Disk(**data, server=server_obj))
        if disk_obj_list:
            models.Disk.objects.bulk_create(disk_obj_list)
    if update_slot_set:
        for slot in update_slot_set:
            data = disk_info[slot]
            models.Disk.objects.filter(slot=slot, server=server_obj).update(**data)

    if delete_slot_set:
        models.Disk.objects.filter(slot__in=delete_slot_set, server=server_obj).delete()


def process_nic(info, server_list):
    # 更新内存
    nic_info = info['nic']['data']
    server_obj = server_list.first()
    nic_db_info = server_obj.nic_list.all().values('name')
    nic_name_set = set(nic_info)
    db_name_set = {i['name'] for i in nic_db_info}

    add_name_set = nic_name_set - db_name_set
    update_name_set = nic_name_set & db_name_set
    delete_name_set = db_name_set - nic_name_set

    if add_name_set:
        nic_obj_list = []
        for name in add_name_set:
            data = nic_info[name]
            data['name'] = name
            nic_obj_list.append(models.NIC(**data, server=server_obj))
        if nic_obj_list:
            models.NIC.objects.bulk_create(nic_obj_list)
    if update_name_set:
        for name in update_name_set:
            data = nic_info[name]
            data['name'] = name

            models.NIC.objects.filter(name=name, server=server_obj).update(**data)

    if delete_name_set:
        models.NIC.objects.filter(name__in=delete_name_set, server=server_obj).delete()