# Chabak_IK-31  
DevOps labs of Chabak Oleh IK-31 group  
## lab_4


## Хід роботи  

1. Ознайомився з Docker.

2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустив команди sudo docker -v,
 sudo docker --help, sudo docker run docker/whalesay cowsay Docker is fun. Вивід цих команд перенаправив у файл my_work.log.

3. Docker працює з Імеджами та Контейнерами. Створив імедж з якого буде запускатись контейнер.

4. Для знайомства з Docker створив імедж із Django сайтом зробленим у попередній роботі.
Використовую команду docker pull python:3.8-slim, щоб завантажити базовий імедж з репозиторію.
 Переглядаю створеного вміст імеджа командою docker inspect python:3.8-slim
Перевіряю чи добре встановився даний імедж командою sudo docker images
Створив файл з іменем Dockerfile та скопіював туди вміст такого ж файлу з репозиторію викладача.

5. Створив власний репозиторій на Docker Hub.

6. Виконав білд (build) Docker імеджа та завантажтажив його до репозиторію. Для цього я повинен вказати правильну назву репозиторію та TAG.
Команда білду: sudo docker build -t seidex/chabak_ik-31:django .
Команда пушу: sudo docker push seidex/chabak_ik-31:django
Посилання на мій Docker Hub репозиторій: https://hub.docker.com/repository/docker/seidex/chabak_ik-31

7. Для запуску веб-сайту виконав команду sudo docker run -it --name=django --rm -p 8000:8000 seidex/chabak_ik-31:django:

8.(Захист) Оскільки веб-сайт готовий і працює, потрібно створит ще один контейнер із програмою моніторингу нашого веб-сайту:
Створив ще один Dockerfile з назвою Dockerfile.mon в якому помістив програму моніторингу.

Виконав білд даного імеджа та дав йому тег monitoring командами:
sudo docker build -f Dockerfile.mon -t seidex/chabak_ik-31:monitoring .
docker push seidex/chabak_ik-31:monitoring

Запустив два контейнери одночасно (у різних вкладках) та переконався що програма моніторингу успішно доступається до сторінок мого веб-сайту.
Запуск серевера:
sudo docker run -it --name=django --rm -p 8000:8000 seidex/chabak_ik-31:django
Запуск моніторингу:
sudo docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log seidex/chabak_ik-31:monitoring

Відредагував README.md файл та закомітив зміни до репозиторію.