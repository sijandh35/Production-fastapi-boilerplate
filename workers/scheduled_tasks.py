scheduled_tasks = {}

scheduled_tasks['add-every-30-seconds'] = {
        'task': 'add_numbers',
        'schedule': 30.0,
        'args': (16, 16)
    }