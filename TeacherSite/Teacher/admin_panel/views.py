from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps  # Импортируем модуль для работы с приложениями и моделями в проекте Django
from django.forms import modelform_factory  # Импортируем функцию для создания форм на основе моделей
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Отображение всех моделей
@login_required
def admin_dashboard(request):
    """
    Функция отображает список всех моделей, зарегистрированных в проекте.
    """
    models = apps.get_models()  # Получаем все модели из проекта
    context = {
        'models': [
            {
                'name': model._meta.object_name,  # Имя модели
                'verbose_name_plural': model._meta.verbose_name_plural  # Множественное имя модели для отображения
            }
            for model in models  # Перебираем все модели и добавляем их в контекст
        ]
    }
    # Отправляем данные в шаблон по путюю 'admin_panel/dashboard.html'
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
# Список записей модели
def model_list_view(request, model_name):
    """
    Функция отображает список записей для выбранной модели.
    """
    # Получаем модель по имени. 'main' — это название приложения, где зарегистрированы модели.
    model = apps.get_model('main', model_name)

    # Получаем все записи этой модели
    objects = model.objects.all()

    context = {
        'objects': objects,  # Список всех записей модели
        'model_name': model_name  # Имя модели для использования в шаблоне
    }

    # Отправляем данные в шаблон 'admin_panel/model_list.html'
    return render(request, 'admin_panel/model_list.html', context)

@login_required
# Редактирование или добавление записи модели
def model_edit_view(request, model_name, object_id=None):
    """
    Функция для редактирования или добавления записи модели.
    Если object_id передан, происходит редактирование записи, иначе — добавление новой записи.
    """
    # Получаем модель по имени
    model = apps.get_model('main', model_name)

    instance = None  # Экземпляр модели по умолчанию None (используется для добавления новой записи)
    if object_id:
        # Если передан object_id, пытаемся получить существующую запись
        instance = get_object_or_404(model, id=object_id)

    # Создаем форму на основе модели. exclude=[] означает, что все поля модели будут включены в форму.
    ModelForm = modelform_factory(model, exclude=[])

    if request.method == 'POST':
        # Если запрос POST, обрабатываем данные формы
        form = ModelForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()  # Сохраняем данные формы (новая запись или обновление существующей)
            # Перенаправляем на страницу со списком записей модели после успешного сохранения
            return redirect('model_list_view', model_name=model_name)
    else:
        # Если запрос GET, создаем форму для добавления новой записи или редактирования существующей
        form = ModelForm(instance=instance)

    context = {
        'form': form,  # Форма для отображения в шаблоне
        'model_name': model_name  # Имя модели для использования в шаблоне
    }

    # Отправляем данные в шаблон 'admin_panel/model_edit.html'
    return render(request, 'admin_panel/model_edit.html', context)

@login_required
def model_delete_view(request, model_name, object_id):
    model = apps.get_model('main', model_name)
    instance = get_object_or_404(model, id=object_id)

    if request.method == 'POST':
        instance.delete()
        return redirect('model_list_view', model_name=model_name)

    context = {
        'object': instance,
        'model_name': model_name
    }

    return render(request, 'admin_panel/model_delete_confirm.html', context)

# Логин
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_board')  # перенаправляем на админ-панель
        else:
            return render(request, 'admin_panel/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'admin_panel/login.html')

# Логаут
def logout_view(request):
    logout(request)
    return redirect('login')