<template>
  <div class="scroll-container" ref="containerRef">
    <section class="screen main-screen">
      <div class="logo-container">
        <a href="https://vk.com/dancechempten" target="_blank" title="Перейти в VK-группу">
          <img src="@/assets/logo.png" alt="TENЬ Logo" class="logo">
        </a>
      </div>
      <div v-if="showProgress" class="side-rail" aria-hidden="true">
        <div class="progress-indicator__track">
          <div class="progress-indicator__fill" :style="{ height: fillHeight }"></div>
        </div>
        
        <div class="page-dots">
          <span :class="{ active: progress < 0.98 }"></span>
          <span :class="{ active: progress >= 0.98 }"></span>
        </div>
      </div>
    </section>

    <section class="screen about-screen">
      <div class="content-wrapper">
        <h2 class="title">О чемпионате</h2>
        <h3 class="slogan">«TENЬ. К свету — через движение»</h3>

        <div class="facts-grid">
          <div class="info-card">
            <p>Чемпионат «TENЬ» — пространство, где танец помогает раскрыть внутренний мир и выразить эмоции на сцене.</p>
            <p>Исследуй контрасты света и тени, попробуй себя в разных форматах и стань частью студенческого сообщества.</p>
          </div>

          <div class="info-card">
            <p><strong>DANCE STUDENT CHEMP «TENЬ» 25</strong></p>
            <p><strong>Даты:</strong> 24-26 ноября</p>
            <p><strong>Место:</strong> РЭУ им. Г. В. Плеханова, Стремянный пер., 36</p>
            <p><strong>Регистрация:</strong> с 13 октября до 1 ноября</p>
          </div>
        </div>
      </div>
    </section>
  </div>
  </template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const containerRef = ref(null)
const showProgress = ref(true)
const progress = ref(0)

const fillHeight = computed(() => `${Math.min(100, Math.max(0, Math.round(progress.value * 100)))}%`)

function handleScroll() {
  const container = containerRef.value
  if (!container) return
  const next = container.querySelector('.about-screen')
  if (!next) return
  const target = next.offsetTop
  const current = container.scrollTop
  const ratio = target > 0 ? current / target : 0
  progress.value = Math.max(0, Math.min(1, ratio))
  // Скрываем индикатор после перехода ко второму экрану
  showProgress.value = current < target - 4
}

onMounted(() => {
  const container = containerRef.value
  if (!container) return
  container.addEventListener('scroll', handleScroll, { passive: true })
  // Инициализация
  handleScroll()
})

onBeforeUnmount(() => {
  const container = containerRef.value
  if (container) container.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.scroll-container {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.screen {
  height: 100vh;
  width: 100%;
  scroll-snap-align: start;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

/* Фон страницы красный/чёрный */
.main-screen {
  background: radial-gradient(ellipse at center, #330000 0%, #000000 70%);
}

.logo-container {
  text-align: center;
}

.logo-container a {
  display: inline-block;
  text-decoration: none;
}

.logo {
  max-width: 80%;
  max-height: 80vh;
  opacity: 0.2; /* слегка на задний план */
  cursor: pointer;
  transition: transform 0.3s ease;
}

.logo:hover {
  animation: shake 0.5s ease-in-out;
}

.logo.animated {
  animation: pulse 4s ease-in-out infinite;
}

@keyframes pulse {
  0% { transform: scale(1); opacity: 0.9; }
  50% { transform: scale(1.03); opacity: 1; }
  100% { transform: scale(1); opacity: 0.9; }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-2px); }
  20%, 40%, 60%, 80% { transform: translateX(2px); }
}

.about-screen {
  background-color: #111;
  color: var(--text-color);
  text-align: center;
  padding: 40px 20px;
  box-sizing: border-box;
}



.content-wrapper { max-width: 980px; }

.title { font-size: 3rem; margin-bottom: 12px; letter-spacing: 0.06em; text-transform: uppercase; }

.slogan { font-size: 1.3rem; color: #cfcfcf; margin-top: 0; margin-bottom: 36px; font-style: italic; }

.facts-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
.info-card { border: 1px solid rgba(229,57,53,0.35); padding: 22px; background: rgba(0,0,0,0.25); border-radius: 8px; text-align: left; line-height: 1.7; }
.info-card strong { color: var(--accent-color); }

/* Вертикальный индикатор прогресса прокрутки */
.progress-indicator { display: none; }

.side-rail {
  position: fixed;
  left: 24px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  z-index: 900;
}

.progress-indicator__track {
  width: 4px;
  height: 160px;
  background: rgba(255, 255, 255, 0.12);
  border-radius: 3px;
  overflow: hidden;
}

.progress-indicator__fill {
  width: 100%;
  height: 0%;
  background: linear-gradient(180deg, var(--accent-color) 0%, rgba(229,57,53,0.65) 100%);
  box-shadow: 0 0 8px rgba(229,57,53,0.45);
  transition: height 0.15s ease;
}

/* удалена кнопка со стрелкой */

.page-dots {
  display: flex;
  flex-direction: column;
  gap: 6px;
  align-items: center;
}

.page-dots span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.page-dots span.active {
  background: var(--accent-color);
  box-shadow: 0 0 8px rgba(229,57,53,0.45);
  transform: scale(1.15);
}

/* Мобильная адаптация */
@media (max-width: 768px) {
  .scroll-container {
    height: auto !important;
    min-height: 100vh;
    scroll-snap-type: none !important;
  }
  
  .screen {
    min-height: 100vh !important;
    height: auto !important;
    padding: 40px 0 !important;
  }
  
  .logo {
    max-width: 60%;
    max-height: 50vh;
    opacity: 0.3;
  }
  
  .side-rail {
    left: 12px;
    gap: 8px;
    display: none !important; /* скрываем индикатор на мобильных */
  }
  
  .progress-indicator__track {
    width: 3px;
    height: 120px;
  }
  
  .page-dots span {
    width: 4px;
    height: 4px;
  }
  
  .about-screen {
    padding: 60px 20px !important;
    min-height: auto !important;
    height: auto !important;
  }
  
  .content-wrapper {
    max-width: 100%;
    padding: 0;
  }
  
  .title {
    font-size: 2rem;
    margin-bottom: 20px;
    line-height: 1.2;
  }
  
  .slogan {
    font-size: 1.1rem;
    margin-bottom: 32px;
    line-height: 1.3;
  }
  
  .facts-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .info-card {
    padding: 24px;
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 20px;
  }
  
  .info-card strong {
    font-size: 1.1rem;
    display: block;
    margin-bottom: 12px;
    color: var(--accent-color);
  }
  
  .info-card p {
    margin-bottom: 16px;
  }
}

@media (max-width: 480px) {
  .logo {
    max-width: 50%;
    max-height: 40vh;
  }
  
  .screen {
    padding: 20px 0 !important;
  }
  
  .about-screen {
    padding: 40px 16px !important;
  }
  
  .title {
    font-size: 1.8rem;
  }
      
  .slogan {
    font-size: 1rem;
    margin-bottom: 24px;
  }
  
  .info-card {
    padding: 20px;
    font-size: 0.95rem;
    line-height: 1.6;
  }
  
  .info-card strong {
    font-size: 1rem;
  }
  
  .side-rail {
    left: 8px;
  }
}
</style>