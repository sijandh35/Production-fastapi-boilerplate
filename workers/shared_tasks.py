from celery import shared_task

@shared_task(name='High_Priority_test', queue='high_priority')
def high_priority_task(data):
    print("I am inside this high-priority task")
    return f"Processed high-priority task with data: {data}"

@shared_task(name='Default_Priority_test', queue='default')
def default_task(data):
    print("I am inside this default task")
    return f"Processed default task with data: {data}"

@shared_task(name='Low_Priority_test', queue='low_priority')
def low_priority_task(data):
    print("I am inside this low-priority task")
    return f"Processed low-priority task with data: {data}"

@shared_task(name='add_numbers', queue='low_priority')
def add(x, y):
    z = x + y
    print(z)
    return z