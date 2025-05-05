# Примеры curl-команд для API Foodbook

Этот документ содержит примеры curl-команд для взаимодействия с API Foodbook. Используйте эти команды для тестирования и демонстрации работы сервиса из командной строки.

## Аутентификация

### Получение токена доступа (логин)

```bash
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=password123"
```

Пример ответа:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Для дальнейших примеров будем использовать переменную `$TOKEN` для хранения токена:
```bash
TOKEN=$(curl -s -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=password123" | grep -o '"access_token":"[^"]*' | sed 's/"access_token":"//')
```

## Пользователи

### Регистрация нового пользователя

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword123"
  }'
```

### Получение данных текущего пользователя

```bash
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer $TOKEN"
```

### Получение списка всех пользователей

```bash
curl -X GET "http://localhost:8000/users/" \
  -H "Authorization: Bearer $TOKEN"
```

### Получение данных конкретного пользователя

```bash
curl -X GET "http://localhost:8000/users/1" \
  -H "Authorization: Bearer $TOKEN"
```

## Рецепты

### Получение всех рецептов

```bash
curl -X GET "http://localhost:8000/recipes/"
```

### Получение рецептов текущего пользователя

```bash
curl -X GET "http://localhost:8000/recipes/user/" \
  -H "Authorization: Bearer $TOKEN"
```

### Получение конкретного рецепта

```bash
curl -X GET "http://localhost:8000/recipes/1"
```

### Создание нового рецепта

```bash
curl -X POST "http://localhost:8000/recipes/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Паста Карбонара",
    "description": "Классическое итальянское блюдо",
    "ingredients": "Спагетти, яйца, бекон, сыр пармезан, черный перец",
    "instructions": "1. Отварить пасту до состояния al dente. 2. Обжарить бекон до хрустящего состояния. 3. Смешать яйца с сыром. 4. Соединить все ингредиенты."
  }'
```

### Обновление рецепта

```bash
curl -X PUT "http://localhost:8000/recipes/1" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Паста Карбонара (обновленный)",
    "description": "Классическое итальянское блюдо с беконом и яйцами",
    "ingredients": "Спагетти, яйца, гуанчиале или бекон, сыр пармезан, черный перец",
    "instructions": "1. Отварить пасту до состояния al dente. 2. Обжарить бекон до хрустящего состояния. 3. Смешать яйца с тертым сыром. 4. Соединить все ингредиенты, быстро перемешав."
  }'
```

### Удаление рецепта

```bash
curl -X DELETE "http://localhost:8000/recipes/1" \
  -H "Authorization: Bearer $TOKEN"
```

## Дополнительные параметры

### Пагинация для списка рецептов

```bash
curl -X GET "http://localhost:8000/recipes/?skip=0&limit=10"
```

### Сохранение токена в переменную и использование в запросах

```bash
# Сохранить токен в переменную
TOKEN=$(curl -s -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=password123" | grep -o '"access_token":"[^"]*' | sed 's/"access_token":"//')

# Использовать токен в запросе
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer $TOKEN"
```

## Пример последовательности команд для демонстрации

```bash
# 1. Регистрация пользователя
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "demo_user",
    "email": "demo@example.com",
    "password": "password123"
  }'

# 2. Получение токена
TOKEN=$(curl -s -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo_user&password=password123" | grep -o '"access_token":"[^"]*' | sed 's/"access_token":"//')

# 3. Создание рецепта
curl -X POST "http://localhost:8000/recipes/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "title": "Борщ",
    "description": "Традиционный украинский суп",
    "ingredients": "Свекла, капуста, морковь, лук, картофель, говядина, томатная паста, сметана",
    "instructions": "1. Сварить бульон из говядины. 2. Обжарить овощи. 3. Добавить овощи в бульон и варить до готовности. 4. Подавать со сметаной."
  }'

# 4. Получение списка своих рецептов
curl -X GET "http://localhost:8000/recipes/user/" \
  -H "Authorization: Bearer $TOKEN"
``` 