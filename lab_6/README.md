# Chabak_IK-31  
DevOps labs of Chabak Oleh IK-31 group  
## lab_6


## Хід роботи  

1. У лабораторній 6 я буду налаштовувати CI/CD сервер. Інтеграція Travis з GitHub пройшла успішно.

2. Для того щоб Travis знав які кроки потрібно виконати над моїм кодом у кореневій папці мого репозиторію створюю файл .travis.yml.

3. Для того щоб налаштувати інтеграцію з Docker Hub прочитав документацію.
Додав в Travis змінні, які дозволять доступатись до Docker аккаунту.
![env var](https://github.com/OlehChabak/Chabak_IK-31/blob/main/lab_6/Screenshot_1.png "env")

4. (Завдання). Білд представлений у даному репозиторію не враховує мої попередні домашні завдання, тому:
Переписав білд lab 2 з використання кроків записаних у Makefile.
Переписав білд lab 4 де я створював ще один DockerFile для контейнера моніторингу.
Переписав білд lab 5 і додав кроки Makefile які робили push імеджів у Docker Hub репозиторій.
Посилання на мій Travis https://app.travis-ci.com/github/OlehChabak/Chabak_IK-31

5. Успішно виконав усі тести у Travis
![tests](https://github.com/OlehChabak/Chabak_IK-31/blob/main/lab_6/Screenshot_2.png "tst")

6. Відредагував свій персональний README.md у цьому репозиторію та створив pull request.