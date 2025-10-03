from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Создаем приложение FastAPI
app = FastAPI()

# Путь к папке со статическими файлами фронтенда
STATIC_DIR = os.path.abspath("../frontend/dist")

# 1. Монтируем статику (JS, CSS, изображения), чтобы FastAPI мог их находить по прямым ссылкам
app.mount(
    "/assets",
    StaticFiles(directory=os.path.join(STATIC_DIR, "assets")),
    name="assets"
)

# 2. Монтируем статику для документов (PDF, DOCX)
app.mount(
    "/docs",
    StaticFiles(directory=os.path.join(STATIC_DIR, "docs")),
    name="docs"
)

# Убедимся, что PDF файл доступен
@app.get("/docs/privacy-policy.pdf")
async def get_privacy_policy():
    pdf_path = os.path.join(STATIC_DIR, "docs", "privacy-policy.pdf")
    if os.path.exists(pdf_path):
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="privacy-policy.pdf"
        )
    else:
        return {"error": "PDF файл не найден"}

# 3. Создаем маршрут для главной страницы, который всегда будет отдавать index.html
@app.get("/{full_path:path}")
async def serve_vue_app(full_path: str):
    index_path = os.path.join(STATIC_DIR, "index.html")
    # Если index.html не существует (например, фронтенд еще не собран), возвращаем ошибку
    if not os.path.exists(index_path):
        return {"error": "Frontend not built yet. Run 'npm run build' in the /frontend directory."}
    return FileResponse(index_path)

# Запускаем сервер (для локальной проверки)
# В реальной работе сервер будет запускаться командой в терминале
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)