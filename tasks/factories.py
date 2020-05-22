import factory
from models import Task, Keyword


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
    retired = False
