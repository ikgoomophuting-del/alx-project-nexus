@role_required(['admin'])
def admin_dashboard(request):
    ...
  
@role_required(['teacher', 'admin'])
def manage_lessons(request):
    ...

