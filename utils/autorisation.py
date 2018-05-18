

def acheteur_check(user):
    return user.groups.filter(name='acheteurs').exists()


def vendeur_check(user):
    return user.groups.filter(name='vendeurs').exists()




