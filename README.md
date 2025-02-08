# **TB5 - Трекер задач сотрудников**
### **Описание**

РЕализовано серверное приложение для работы с базой данных, представляющее собой трекер задач сотрудников. Приложение обеспечивет CRUD операции для сотрудников и задач, а также предоставлять два специальных эндпоинта для получения информации о загруженности сотрудников и важных задачах.
Трекер задач позволит компании эффективно управлять заданиями, назначенными сотрудникам, и обеспечивать прозрачность процессов выполнения задач. Это поможет в равномерном распределении нагрузки между сотрудниками и своевременном выполнении ключевых задач.
>#### **Специальные эндпоинты:**
>- Занятые сотрудники:
> 
> Запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач.
>- Важные задачи:
> 
> Запрашивает из БД задачи сотрудников, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу.
> 
>  Реализует поиск по сотрудникам, которые могут взять такие задачи (менее загруженный сотрудник или сотрудник выполняющий родительску задачу, если ему назначено на 2 задачи больше чем у наименее загруженного).
> 
> Возвращает список объектов в формате: {Важная задача, Срок, [ФИО сотрудника]}.

### **Технологии**
- Python
- Django
- DRF
- PostgreSQL
- Docker

### **Запуск проекта в Docker:**
#### 1. Установка Docker
Установите Docker на вашей ОС.
#### 2. Клонирование репозитория
Склонируйте репозиторий с github с помощью команды `git clone`
#### 3. Настройка файла _.env_
Создайте файл _.env_ в корневой директории проекта. В файле необходимо внести переменные окружения, образец есть в [.env.sample](.env.sample)
#### 4. Запуск контейнеров Docker
- Откройте терминал и перейдите в корневую директорию проекта
- Введите команду:
>`docker compose build up -d --build`

Для запуска контейнеров описанных в [docker-compose.yaml](docker-compose.yaml) 

Дождитесь запуска всех контейнеров.
#### 5. Проверка
Откройте веб-браузер и перейдите по указанному вами адресу и порту, чтобы, убедиться что приложение работает.
#### 6. Остановка приложения
Чтобы остановить работу приложения, введите в терминал команду `docker-compose down` 

### **URL**
- **[GET]** http://localhost:8000/users/user/ - Просмотр списка юзеров.
- 
- **[POST]** http://localhost:8000/users/register/ - Создание юзера.

- **[POST]** http://localhost:8000/users/create_token/ - Создание JWT токена.

- **[POST]** http://localhost:8000/users/token/refresh/ - Обновление JWT токена.

- **[GET]** http://localhost:8000/tasks/employees/ - Просмотр списка сотрудников.

- **[GET]** http://localhost:8000/tasks/employees/{id}/ - Просмотр сотрудника.

- **[POST]** http://localhost:8000/tasks/employees/ - Создание сотрудника.

- **[PATCH]** http://localhost:8000/tasks/employees/{id}/ - Редактирование сотрудника.

- **[DELETE]** http://localhost:8000/tasks/employees/{id}/ - Удаление сотрудника.

- **[GET]** http://localhost:8000/task/task_list/ - Просмотр списка задач.

- **[GET]** http://localhost:8000/tasks/retrieve/{id}/ - Просмотр задачи.

- **[POST]** http://localhost:8000/tasks/create/ - Создание задачи.

- **[PATCH]** http://localhost:8000/tasks/update/{id}/ - Редактирование задачи.

- **[DELETE]** http://localhost:8000/tasks/delete/{id}/ - Удаление задачи.

- **[GET]** http://localhost:8000/tasks/employee_track/employee_track_list/ - Просмотр для подсчета активных задач работника.

- **[GET]** http://localhost:8000/tasks/important_tasks/important_tasks_list/ - Поиск менее загруженных сотрудников для важных задач.

- http://127.0.0.1:8000/swagger/, http://127.0.0.1:8000/redoc/ - документация для API