# 🚀 Руководство по развертыванию

## Локальная разработка

### Быстрый старт

1. **Клонирование репозитория**
```bash
git clone <repository-url>
cd dance-chemp
```

2. **Запуск фронтенда**
```bash
cd frontend
npm install
npm run dev
# Откройте http://localhost:3000
```

3. **Запуск бэкенда**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Откройте http://localhost:8000
```

## Продакшн развертывание

### С Docker

```bash
# Сборка и запуск
docker-compose up --build -d

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down
```

### Без Docker

1. **Сборка фронтенда**
```bash
cd frontend
npm run build
```

2. **Настройка бэкенда**
```bash
cd backend
pip install -r requirements.txt
# Настройте переменные окружения при необходимости
```

3. **Запуск продакшн сервера**
```bash
# Через uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# Через gunicorn (рекомендуется для продакшна)
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Переменные окружения

Создайте `.env` файл в корне проекта:

```bash
# .env
NODE_ENV=production
PYTHONPATH=/path/to/app
```

## Настройка веб-сервера

### Nginx конфигурация

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /path/to/static/files/;
        expires 30d;
    }
}
```

## SSL сертификаты

Для HTTPS используйте Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Мониторинг

Рекомендуемые инструменты:
- **Prometheus + Grafana** для метрик
- **Sentry** для отслеживания ошибок
- **Uptime Robot** для проверки доступности

## Бэкапы

Настройте регулярные бэкапы:
- Собранных статических файлов фронтенда
- Конфигурационных файлов
- Баз данных (если есть)

## Обновление

```bash
git pull origin main
# Пересобрать и перезапустить контейнеры
docker-compose up --build -d
```

## Troubleshooting

### Частые проблемы

1. **Порт занят**
```bash
sudo lsof -i :8000
sudo kill -9 <PID>
```

2. **Права доступа к файлам**
```bash
chown -R www-data:www-data /path/to/app
```

3. **Проблемы с Docker**
```bash
docker system prune -f
docker-compose down -v
docker-compose up --build
```

### Логи

```bash
# Docker логи
docker-compose logs -f dance-chemp

# Системные логи
journalctl -u your-service-name -f
```

## Производительность

- Используйте CDN для статических файлов
- Настройте кэширование в браузере
- Оптимизируйте изображения
- Используйте compression middleware

## Безопасность

- Регулярно обновляйте зависимости
- Используйте HTTPS
- Настройте firewall
- Ограничьте доступ к административной панели
