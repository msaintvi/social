from social.models import User, Group, Post

def run():
    if User.objects.exists():
        return  # Skip if already initialized

    User.objects.create(
        username='DaBoi27',
        password='DaBoi10@',
        email='DaBoi@gmx.fr',
        first_name='Yanis',
        last_name='Diable-Campagne',
        date_of_birth='2000-08-09',
        about="C'est un profil template.",
        privacy='public',
    )

    Group.objects.create(individual='DaBoi27', affiliation='Ratz')

    Post.objects.create(title='Hello World!', content='This is a test post.', creator='DaBoi27')
    Post.objects.create(title='Fourmis Extraterrestes?!', content='Je viens de voir les fourmis de Kevins...', creator='DaBoi27')
    Post.objects.create(title='Ragondin Inc.', content='En vrai. Le communisme.', creator='DaBoi27')
