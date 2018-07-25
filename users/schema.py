import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    user = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    skills = graphene.String()
    points = graphene.String()
    badges = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        skills = graphene.String()
        points = graphene.Int()
        badges = graphene.String()

    #3
    def mutate(self, info, name, email, password, skills, points, badges):
        user = User(
            name=name,
            email=email,
            password=password,
            skills=skills,
            points=points,
            badges=badges
            )
        user.save()

        return CreateUser(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            skills=user.skills,
            points=user.points,
            badges=user.badges
        )


#4
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
