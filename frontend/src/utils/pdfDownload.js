/**
 * Утилита для скачивания PDF файлов
 * @param {string} filename - имя файла в папке docs
 * @param {string} downloadName - имя файла при скачивании
 */
export function downloadPDF(filename, downloadName) {
  try {
    // Создаем ссылку для скачивания файла
    const link = document.createElement('a');
    link.href = `/docs/${filename}`;
    link.download = downloadName;
    link.target = '_blank';
    
    // Добавляем ссылку в документ, кликаем и удаляем
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (error) {
    console.error('Ошибка при скачивании PDF:', error);
    // Fallback - прямая ссылка на файл
    window.open(`/docs/${filename}`, '_blank');
  }
}
