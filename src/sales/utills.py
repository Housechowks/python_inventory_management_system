import uuid
from customers.models import custmer
from profiles.models import profile



def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


def get_salesman_from_id(val):
    salesman = profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = custmer.objects.get(id=val)
    return customer