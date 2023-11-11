
from random import randint
from django.shortcuts import render

from django.utils.text import slugify

from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Project, Category, Lesson
from .serializers import ProjectListSerializer, ProjectDetailSerializer, CategorySerializer, LessonListSerializer


@api_view(['GET'])

def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)



@api_view(['GET'])


def get_projects(request):
    category_id = request.GET.get('category_id', '')
    projects = Project.objects.filter(status=Project.PUBLISHED)

    if category_id:
        projects = projects.filter(categories__in=[int(category_id)])

    serializer = ProjectListSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])

def get_project(request, slug):
    project = Project.objects.filter(status=Project.PUBLISHED).get(slug=slug)
    project_serializer = ProjectDetailSerializer(project)
    lesson_serializer = LessonListSerializer(project.lessons.all(), many=True)

    if request.user.is_authenticated:
        project_data = project_serializer.data
    else:
        project_data = {}

    return Response({
        'project': project_data,
        'lessons': lesson_serializer.data
    })





@api_view(['POST'])
def create_project(request):
    status = request.data.get('status')

    print(request.data)

    if status == 'published':
        status = 'draft'

    project = Project.objects.create(
        title=request.data.get('title'),
        slug='%s-%s' % (slugify(request.data.get('title')), randint(1000, 10000)),
        short_description=request.data.get('short_description'),
        long_description=request.data.get('long_description'),
        status=status,
        created_by=request.user
    )

    for id in request.data.get('categories'):
        project.categories.add(id)
    
    project.save()

    # Lessons

    for lesson in request.data.get('lessons'):
        tmp_lesson = Lesson.objects.create(
            project=project,
            title=lesson.get('title'),
            slug=slugify(lesson.get('title')),
            short_description=lesson.get('short_description'),
            long_description=lesson.get('long_description'),
            status=Lesson.DRAFT
        )

    return Response({'project_id': project.id})