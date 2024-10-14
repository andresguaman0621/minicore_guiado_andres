from django.shortcuts import render
from .models import Employee, Project, Task

from datetime import datetime, timedelta

def index(request):
    if request.method == 'POST':
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']

        date_start = datetime.strptime(date_start, '%Y-%m-%d').date()
        date_end = datetime.strptime(date_end, '%Y-%m-%d').date()

        task_in_process_date = Task.objects.filter(date_start__range=[date_start, date_end], status='In Progress') # pylint: disable=no-member

        for task in task_in_process_date:
            task.date_end = task.date_start + timedelta(days=task.estimate_time)

            date_start_task = task.date_start.strftime('%Y-%m-%d')

            date_end_task = task.date_end.strftime('%Y-%m-%d')
            day_end_task = int(date_end_task.split('-')[2])

            date_end_filter = date_end.strftime('%Y-%m-%d')

            # Ver si se paso el mes para agregarle los días restantes
            if int(date_end_filter.split('-')[1]) > int(date_end_task.split('-')[1]):
                day_end_task += 30

            day_difference = int(date_end_filter.split('-')[2]) - day_end_task

            task.delay = day_difference

        return render(request, 'index.html', {
            'task_in_process_date': task_in_process_date,
            'date_start': date_start.strftime('%Y-%m-%d'),
            'date_end': date_end.strftime('%Y-%m-%d')
        })
    else:
        return render(request, 'index.html')

def employee(request):
    if request.method == 'POST':
        new_employee = Employee(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
        new_employee.save()

        employee = Employee.objects.all() # pylint: disable=no-member
        return render(request, 'empleados.html', {
            'employee': employee
        })
    else:
        employee = Employee.objects.all() # pylint: disable=no-member
        return render(request, 'empleados.html', {
            'employee': employee
        })

def project(request):
    if request.method == 'POST':
        new_project = Project(
            name=request.POST['name']
        )
        new_project.save()

        project = Project.objects.all() # pylint: disable=no-member
        return render(request, 'proyectos.html', {
            'project': project
        })
    project = Project.objects.all() # pylint: disable=no-member
    return render(request, 'proyectos.html', {
        'project': project
    })

def task(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        project_id = request.POST['project_id']

        try:
            employee = Employee.objects.get(pk=employee_id) # pylint: disable=no-member
            project = Project.objects.get(pk=project_id) # pylint: disable=no-member
        except Employee.DoesNotExist: # pylint: disable=no-member
            return render(request, 'tareas.html', {
                'error': 'El empleado no existe'
            })
        except Project.DoesNotExist: # pylint: disable=no-member
            return render(request, 'tareas.html', {
                'error': 'El proyecto no existe'
            })

        new_task = Task(
            description=request.POST['description'],
            date_start=request.POST['date_start'],
            estimate_time=request.POST['estimate_time'],
            status=request.POST['status'],
            id_employee=employee,
            id_project=project
        )
        new_task.save()

        task = Task.objects.all() # pylint: disable=no-member
        employee = Employee.objects.all() # pylint: disable=no-member
        project = Project.objects.all() # pylint: disable=no-member

        return render(request, 'tareas.html', {
            'employee': employee,
            'task': task,
            'project': project
        })
    else:
        task = Task.objects.all() # pylint: disable=no-member
        employee = Employee.objects.all() # pylint: disable=no-member
        project = Project.objects.all() # pylint: disable=no-member

        return render(request, 'tareas.html', {
            'employee': employee,
            'task': task,
            'project': project
        })
    
# Delete
def delete_employee(request, id):
    employee = Employee.objects.get(pk=id) # pylint: disable=no-member
    employee.delete()

    employee = Employee.objects.all() # pylint: disable=no-member
    return render(request, 'empleados.html', {
        'employee': employee
    })

def delete_project(request, id):
    project = Project.objects.get(pk=id) # pylint: disable=no-member
    project.delete()

    project = Project.objects.all() # pylint: disable=no-member
    return render(request, 'proyectos.html', {
        'project': project
    })

def delete_task(request, id):
    task = Task.objects.get(pk=id) # pylint: disable=no-member
    task.delete()

    task = Task.objects.all() # pylint: disable=no-member
    employee = Employee.objects.all() # pylint: disable=no-member
    project = Project.objects.all() # pylint: disable=no-member
    return render(request, 'tareas.html', {
        'employee': employee,
        'task': task,
        'project': project
    })

# Update
def update_task(request, id):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        project_id = request.POST['project_id']

        task = Task.objects.get(pk=id) # pylint: disable=no-member
        task.description = request.POST['description']
        task.date_start = request.POST['date_start']
        task.estimate_time = request.POST['estimate_time']
        task.status = request.POST['status']
        task.id_employee = Employee.objects.get(pk=employee_id) # pylint: disable=no-member
        task.id_project = Project.objects.get(pk=project_id) # pylint: disable=no-member
        task.save()

        task = Task.objects.all() # pylint: disable=no-member
        employee = Employee.objects.all() # pylint: disable=no-member
        project = Project.objects.all() # pylint: disable=no-member

        return render(request, 'tareas.html', {
            'employee': employee,
            'task': task,
            'project': project
        })
    else:
        task = Task.objects.get(pk=id) # pylint: disable=no-member
        employee = Employee.objects.all() # pylint: disable=no-member
        project = Project.objects.all() # pylint: disable=no-member

        return render(request, 'edit_task.html', {
            'employee': employee,
            'task': task,
            'project': project
        })
    
def update_employee(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id) # pylint: disable=no-member
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.save()

        employee = Employee.objects.all() # pylint: disable=no-member
        return render(request, 'empleados.html', {
            'employee': employee
        })
    else:
        employee = Employee.objects.get(pk=id) # pylint: disable=no-member
        return render(request, 'edit_employee.html', {
            'employee': employee
        })
    
def update_project(request, id):
    if request.method == 'POST':
        project = Project.objects.get(pk=id) # pylint: disable=no-member
        project.name = request.POST['name']
        project.save()

        project = Project.objects.all() # pylint: disable=no-member
        return render(request, 'proyectos.html', {
            'project': project
        })
    else:
        project = Project.objects.get(pk=id) # pylint: disable=no-member
        return render(request, 'edit_project.html', {
            'project': project
        })