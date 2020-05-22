import factory
from .models import Task, Keyword
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'Username {0}'.format(n))
    password = factory.Sequence(lambda n: f'secure-password{0}'.format(n))
    email = factory.Sequence(lambda n: f'email{0}@gmail.com'.format(n))
    first_name = factory.Sequence(lambda n: f'first{0}'.format(n))
    last_name = factory.Sequence(lambda n: f'last{0}'.format(n))


class KeywordFactory(factory.DjangoModelFactory):
    class Meta:
        model = Keyword

    name = factory.Sequence(lambda n: f'Verbal {0}'.format(n))
    user_submitted = factory.SubFactory(UserFactory)
    date_created = factory.Faker('date_object')


class TaskFactory(factory.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Sequence(lambda n: f'Make a player yawn. {0}'.format(n))
    user_submitted = factory.SubFactory(UserFactory)

    @factory.post_generation
    def add_keywords_to_task(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for keyword in extracted:
                self.keywords.add(keyword)

    date_created = factory.Faker('date_object')
    accepted = True
    retired = False
