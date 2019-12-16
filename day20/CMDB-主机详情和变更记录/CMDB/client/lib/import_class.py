import importlib


def get_class(class_path):
    module_name, cls_name = class_path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_name)
    cls = getattr(module, cls_name)
    return cls