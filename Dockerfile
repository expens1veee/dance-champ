# Мультистадийная сборка для фронтенда и бэкенда

# Стадия 1: Сборка фронтенда
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production

COPY frontend/ ./
RUN npm run build

# Стадия 2: Финальный образ с бэкендом
FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей Python
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бэкенда
COPY backend/ ./

# Копируем собранный фронтенд из предыдущей стадии
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Создаем непривилегированного пользователя
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
