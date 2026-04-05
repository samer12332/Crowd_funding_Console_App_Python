def get_next_id(items, id_key):
    if not items:
        return 1

    max_id = 0
    for item in items:
        current_id = item.get(id_key, 0)
        if isinstance(current_id, int) and current_id > max_id:
            max_id = current_id

    return max_id + 1
