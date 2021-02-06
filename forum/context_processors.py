from .models import Department

def departments_contexts(request):
    departments = Department.objects.all()
    return {'departments': departments}