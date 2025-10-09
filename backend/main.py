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

# 1.1. Монтируем папку docs для PDF файлов
app.mount(
    "/docs",
    StaticFiles(directory=os.path.join(STATIC_DIR, "docs")),
    name="docs"
)


# 2. Создаем маршрут для favicon
@app.get("/favicon.ico")
async def favicon():
    favicon_path = os.path.join(STATIC_DIR, "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"error": "Favicon not found"}

# 3. Создаем маршрут для manifest.json
@app.get("/manifest.json")
async def manifest():
    manifest_path = os.path.join(STATIC_DIR, "manifest.json")
    if os.path.exists(manifest_path):
        return FileResponse(manifest_path)
    return {"error": "Manifest not found"}

# 4. Создаем маршрут для главной страницы, который всегда будет отдавать index.html
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
    uvicorn.run(app, host="0.0.0.0", port=80)