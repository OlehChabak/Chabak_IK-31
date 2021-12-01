# Chabak_IK-31  
DevOps labs of Chabak Oleh IK-31 group  
## lab_5


## Хід роботи  

1. Для ознайомляння з docker-compose звернувся до документації.
Щоб встановити docker-compose використав команду:
sudo apt install docker-compose

2. Ознайомився з бібліотекою Flask, яку найчастіше використовують для створення простих веб-сайтів на Python.

3. Моє завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами двома методами:
за допомогою Makefile;
за допомогою docker-compose.yaml.

4. Першим розгляну метод з Makefile, але спочатку створю робочий проект.

5. Створив папку my_app в якій буде знаходитись мій проект. Створив папку tests де будуть тести на перевірку працездатності мого проекту.
Скопіював файли з репозиторію викладача у відповідні папки мого репозеторію.
Ознайомився із вмістом кожного з файлів. Звернув увагу на файл requirements.txt у папці проекту та тестах.
Даний файл буде мітити залежності для мого проекту він містить назви бібліотек які імпортуються.

6. Я спробував чи проект є працездатним перейшовши у папку my_app та після ініціалізації середовища виконав команди записані нижче:
sudo pipenv --python 3.8
sudo pipenv install -r requirements.txt
sudo pipenv run python app.py

Так само я ініціалузував середовище для тестів у іншій вкладці шелу та запустив їх командою sudo pipenv run pytest test_app.py --url http://localhost:5000 але спочатку треба перейти в папку tests:
Звернув увагу, що в мене автоматично створюються файли Pipfile та Pipfile.lock, а також на хост машині буде створена папка .venv. Після зупинки проекту видалив їх.
Перевірив роботу сайту перейшовши головну сторінку.

7. Видалив файли які постворювались після тестового запуску.
Щоб моє середовище було чистим, все буде створюватись і виконуватись всередині Docker. Створив файли Dockerfile.app, Dockerfile.tests та Makefile який допоможе автоматизувати процес розгортання.
8. Скопіював вміст файлів Dockerfile.app, Dockerfile.tests та Makefile з репозиторію викладача та ознайомився із вмістом Dockerfile та Makefile та його директивами.
(Пояснення призначення окремих директив файлу) Директиви app та tests: Створення імеджів для сайту та тесту. Директива run: Запускає сайт. Директива test-app: Запуск тесту. Директива docker-prune: Очищення імеджів.

9. Для початку, використовуючи команду sudo make app створив Docker імеджі для додатку та для тестів sudo make tests.
Запустив додаток командою sudo make run та перейшовши в іншу вкладку шелу запустив тести командою sudo make test-app.
Запуск сайту:

77ee5b50695dc61f9ebea88a4bb413ea2a9c659d2ea5247fc0167a556482248f

Unable to find image 'redis:latest' locally

latest: Pulling from library/redis

eff15d958d66: Pull complete 

1aca8391092b: Pull complete 

06e460b3ba1b: Pull complete 

def49df025c0: Pull complete 

646c72a19e83: Pull complete 

db2c789841df: Pull complete 

Digest: sha256:619af14d3a95c30759a1978da1b2ce375504f1af70ff9eea2a8e35febc45d747

Status: Downloaded newer image for redis:latest

71adbfb9f8a4cb318c06eb0e176f92850cf8f456caa8996380d9412c4a4b3eef

60ab95b3f8debe9b345c16f0dc7f92e5855b10ab83c4f7e0a750d4006ba2f390


Проходження тесту:

============================= test session starts ==============================

platform linux -- Python 3.7.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0

rootdir: /tests

collected 4 items



test_app.py ....                                                         [100%]



============================== 4 passed in 0.10s ===============================

10. Зупинив проект натиснувши Ctrl+C та почистив всі ресурси Docker за допомогою make.
sudo make docker-prune

60ab95b3f8de

71adbfb9f8a4

e8dadbdffdad

1d5f35148868

Total reclaimed space: 0B

Deleted Volumes:

722bf54da2e559719cc77d8fb994f7f94f47384c029965b7a11050548b49cbe4



Total reclaimed space: 0B

Deleted Networks:

appnet



Total reclaimed space: 0B

11. Створив директиву PushToDocker в Makefile для завантаження створених імеджів у мій Docker Hub репозиторій.

12. Видалив створені та закачані імеджі. Створив директиву в Makefile яка автоматизує процес видалення моїх імеджів.

13. Перейшов до іншого варіанту з використанням docker-compose.yaml. Для цього створив даний файл у кореновій папці проекту та заповнив вмістом з прикладу.
Проект який я буду розгортити за цим варіантом трохи відрізняється від першого тим що у нього зявляється дві мережі: приватна і публічна.

14. Перевірив чи Docker-compose встановлений та працює у моїй системі, а далі просто запускаю docker-compose:
docker-compose --version
sudo docker-compose -p lab5 up

REPOSITORY            TAG             IMAGE ID       CREATED              SIZE

seidex/lab_5          compose-tests   a64f6ebf73ee   42 seconds ago       138MB

seidex/lab_5          compose-app     2646a2c66046   About a minute ago   137MB

redis                 alpine          3900abf41552   35 hours ago         32.4MB

python                3.7-alpine      a1034fd13493   36 hours ago         41.8MB

17. Зупинив проект натиснувши Ctrl+C і почистітив ресурси створені компоуз командою docker-compose down.

18. Завантажив створені імеджі до Docker Hub репозиторію за допомого команди sudo docker-compose push.

19. Що на Вашу думку краще використовувати Makefile чи docker-compose.yaml? - На мою думку краще використовувати docker-compose.yaml

20. (Завдання) Оскільки Ви навчились створювати docker-compose.yaml у цій лабораторній то потрібно:
Cтворив docker-compose.yaml для лабораторної №4.
Компоуз повинен створити два імеджі для Django сайту та моніторингу, а також їх успішно запустити. Файл docker-compose.yaml додаю в оновленні лабораторної №4

21. Після успішного виконання роботи я відредагував свій README.md у цьому репозиторію та створив pull request.