from auth.models import RUser

def get_dept_names(request):
    context = {}
    context['dept_names'] = RUser.department_labels
    context['batch_names'] = RUser.batch_labels
    return context
