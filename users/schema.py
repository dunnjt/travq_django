import graphene
from graphene_django import DjangoObjectType

from .models import User, Question, Answer, Tag, Skill, Badge


class UserType(DjangoObjectType):
    class Meta:
        model = User

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer

class SkillType(DjangoObjectType):
    class Meta:
        model = Skill

class BadgeType(DjangoObjectType):
    class Meta:
        model = Badge

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class Query(graphene.ObjectType):
    user = graphene.List(UserType)
    question = graphene.List(QuestionType)
    answer = graphene.List(AnswerType)
    tag = graphene.List(TagType)
    badge = graphene.List(BadgeType)
    skill = graphene.List(SkillType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()

    def resolve_question(self, info, **kwargs):
        return Questions.objects.all()

    def resolve_tag(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_answer(self, info, **kwargs):
        return Answers.objects.all()

    def resolve_skill(self, info, **kwargs):
        return Skill.objects.all()

    def resolve_badge(self, info, **kwargs):
        return Badge.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    points = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        skills = graphene.String()
        points = graphene.Int()

    #3
    def mutate(self, info, name, email, password, skills, points):
        user = User(
            name=name,
            email=email,
            password=password,
            skills=skills,
            points=points
            )
        user.save()

        return CreateUser(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            skills=user.skills,
            points=user.points
        )

class CreateAnswer(graphene.Mutation):
    id = graphene.Int()
    userId = graphene.String()
    votes = graphene.Int()
    createdOn = graphene.Date()
    answer = graphene.String()

    #2
    class Arguments:
        votes = graphene.Int()
        answer = graphene.String()
        userId = graphene.String()
        question = graphene.String()

    #3
    def mutate(self, info, answer, votes, userId, question):
        answer = Answer(
            answer=answer,
            votes=votes,
            userId=userId,
            question=question
            )
        answer.save()

        return CreateAnswer(
            id=answer.id,
        )

class CreateQuestion(graphene.Mutation):
    id = graphene.Int()
    userId = graphene.String()
    question = graphene.String()
    tags = graphene.String()
    createdOn = graphene.Date()

    #2
    class Arguments:
        question = graphene.String()
        tags = graphene.String()
        userId = graphene.String()

    #3
    def mutate(self, info, question, tags, userId):
        question = Question(
            question=question,
            tags=tags,
            userId=userId
            )
        question.save()

        for t in tags:
            temp = Tag(tag=t)
            temp.save()
            question.tags.add(temp)
            question.save()

        return CreateQuestion(
            id=question.id,
            createdOn=question.createdOn
        )

class CreateSkill(graphene.Mutation):
    id = graphene.Int()
    userId = graphene.String()
    skill = graphene.String()

    #2
    class Arguments:
        userId = graphene.String()
        skill = graphene.String()

    #3
    def mutate(self, info, userId, skill):
        skill = Skill(
            skill=skill,
            userId=userId
            )
        skill.save()

        return CreateSkill(
            id=skill.id,
        )

class CreateBadge(graphene.Mutation):
    id = graphene.Int()
    userId = graphene.String()
    badge = graphene.String()

    #2
    class Arguments:
        userId = graphene.String()
        badge = graphene.String()

    #3
    def mutate(self, info, userId, badge):
        skill = Skill(
            skill=badge,
            userId=userId
            )
        badge.save()

        return CreateBadge(
            id=badge.id,
        )

class CreateTag(graphene.Mutation):
    id = graphene.Int()
    tag = graphene.String()

    #2
    class Arguments:
        tag = graphene.String()

    #3
    def mutate(self, info, tag):
        tag = Tag(
            tag=tag
            )
        tag.save()

        return CreateTag(
            id=tag.id,
        )

#4
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_question = CreateQuestion.Field()
    create_answer = CreateAnswer.Field()
    create_skill = CreateSkill.Field()
    create_badge = CreateBadge.Field()
    create_tag = CreateTag.Field()
