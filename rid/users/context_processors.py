from auth.models import RidUser

def get_dept_names(request):
    context = {}
    context['dept_names'] = RidUser.department_labels
    context['batch_names'] = RidUser.batch_labels
    return context
