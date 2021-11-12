# Chabak_IK-31  
DevOps labs of Chabak Oleh IK-31 group 
## lab_3


## Хід роботи

1. Створоврюємо папку з назвою лаб роботи. Ініціалізуємо середовище `pipenv` та встановлюємо необхідні пакети за допомогою:
    pipenv --python 3.7
    pipenv install django
    
2. За допомогою Django Framework створюємо заготовку (template)
    pipenv run django-admin startproject my_site

3. Запускаємо Django сервер. Переходимо на localhost:8000:
    pipenv run python manage.py runserver

4. Зупиняємо сервер виконавши переривання `Ctrl+C`.
5. Далі робимо темплейт додатку у якому буде описано всі web сторінки сайту.:
    pipenv run python manage.py startapp main

6. Робимо папку `main/templates/`, а також у даній папці файл з розширенням `.html` (`main.html`). Також у папці додатку робимо ще один файл `main/urls.py`. 
    
7. Після створення додатку нам потрібно вказати Django frameworks його назву та де шукати веб сторінки. 

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
], 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

8.Переходимо до нашого додатку та створимо сторінки двох типів - перша буде зчитуватись з `.html` темплейта, друга буде просто повертати відповідь у форматі JSON;
     - відкриемо та ознайомимось із вмістом файла `main/views.py`. 
     
9. Щоб поєднати функції із реальними URL шляхами за якими будуть доступні наші веб сторінки заповнюємо файл `main/urls.py` Як можна зрозуміти з коду у нас є два URL посилання:
     - головна сторінка яка буде опрацьовуватись функцією `main`;
     - сторінка health/ яка буде опрацьована функцією `health`;

urlpatterns = [
    path('', views.main, name='main'),
    path('health/', views.health, name='health')
]

10. Запускаємо сервер та переконуємося що сторінки доступні.

11. Роль моніторингу буде здійснювати файл `monitoring.py` який за допомогою бібліотеки `requests` буде опитувати сторінку `health`. Встановлюємо бібліотеку;
     pipenv install requests

12. Як видно із заготовленої функції health() відповідь формується як python словник і далі обробляється функцією JsonResponse(). 

13. Захист:

     i. Модифікувати функцію `health` так щоб у відповіді були: згенерована на сервері дата, URL сторінки моніторингу, інформація про сервер на якому запущений сайт та інформація про клієнта який робить запит до сервера;

     def health(request):
    osInfo = os.uname()
    response = {
    'date': datetime.now().strftime("%d.%m.%y %H:%M"),
    'current_page': request.get_host() + request.get_full_path(),
    'server_info': f"OSName: {osInfo.sysname}; NodeName: {osInfo.nodename}; Release:{osInfo.release}; Version:{osInfo.version}; Indentificator:{osInfo.machine}",
    'client_info': f"Browser: {request.META['HTTP_USER_AGENT']}  IP: {request.META['REMOTE_ADDR']} "
    }
    return JsonResponse(response)

     ii. Дописати функціонал, який буде виводити повідомлення про недоступність сайту у випадку, якщо WEB сторінка недоступна 

     try:
         r = requests.get(url)
         data = json.loads(r.content)
         logging.info("Server is available. Server time: %s", data['date'])
         logging.info("Viewed page: %s", data['current_page'])
         logging.info("Server request contains this fields:")
         for key in data.keys():
              logging.info("Key: %s, Data: %s", key, data[key])
    except Exception as x:
         logging.error("Server is unavailable")

     iii. Після запуску моніторингу запит йде лише один раз, після чого програма закінчується - зробіть так, щоб дана програма запускалась раз в хвилину та працювала в бекграунді (період запуску зробити через функціонал мови Python);

     while(True):
        main("http://localhost:8000/health")
        time.sleep(60)

       Для запуску в беграунді викликаємо файл так
     pipenv run python3 monitoring.py &

     iv. спростіть роботу з пайтон середовищем через швидкий виклик довгих команд, для цього зверніть увагу на секцію `scripts` у Pipfile. Зробіть аліас на запус моніторингу:
     
        [scripts]
        server = "python manage.py runserver"
        mon = "python3 monitoring.py"

14.Переконуємося що все працює, комітимо та додаемо _README.md_. 
