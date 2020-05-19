def once(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@once
def get_logger():
    return [1, 2, 3] * 2


print(id(get_logger), id(get_logger))
