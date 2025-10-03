<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { ref, onMounted, computed, onBeforeUnmount } from 'vue'

const isMenuOpen = ref(false)

const route = useRoute()
const windowWidth = ref(window.innerWidth)

const isStaticFooter = computed(() => {
  // На мобильных устройствах статический футер везде
  const isMobile = windowWidth.value <= 768
  return isMobile || route.path === '/master-classes' || route.path === '/kgo'
})

onMounted(() => {
  setTimeout(() => {
    isMenuOpen.value = true
  }, 250)
  
  const handleResize = () => {
    windowWidth.value = window.innerWidth
  }
  
  window.addEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize)
})
</script>

<template>
  <button @click="isMenuOpen = !isMenuOpen" class="menu-toggle" :aria-expanded="isMenuOpen" aria-label="Открыть меню">
    <span class="hamburger" :class="{ 'is-open': isMenuOpen }"><span></span><span></span><span></span></span>
  </button>

  <div class="backdrop" :class="{ 'is-visible': isMenuOpen }" @click="isMenuOpen = false"></div>

  <nav class="main-nav" :class="{ 'is-open': isMenuOpen }">
    <RouterLink to="/" @click="isMenuOpen = false">Главная</RouterLink>
    <RouterLink to="/registration" @click="isMenuOpen = false">Регистрация</RouterLink>
    <RouterLink to="/master-classes" @click="isMenuOpen = false">Мастер-классы</RouterLink>
    <RouterLink to="/nominations" @click="isMenuOpen = false">Номинации</RouterLink>
    <RouterLink to="/kgo" @click="isMenuOpen = false">КГО</RouterLink>
    <RouterLink to="/regulations" @click="isMenuOpen = false">Положение</RouterLink>
    <RouterLink to="/contacts" @click="isMenuOpen = false">Контакты</RouterLink>
  </nav>

  <div :class="['layout', { 'layout--static': isStaticFooter }]">
    <RouterView />

    <footer class="main-footer">
    <a href="https://vk.com/dancechempten" target="_blank" title="Сообщество ВК">VK</a>
    <a href="https://t.me/dancechempten" target="_blank" title="Телеграм-канал">TG</a>
    <a href="mailto:dancechempten@mail.ru" title="Корпоративная почта">Email</a>
    </footer>
  </div>
</template>

<style scoped>
.menu-toggle {
  position: fixed;
  top: 20px;
  right: 24px;
  z-index: 1001;
  background: none;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.hamburger {
  display: inline-block;
  width: 28px;
  height: 22px;
  position: relative;
}
.hamburger span {
  display: block;
  position: absolute;
  height: 3px;
  width: 100%;
  background: var(--text-color);
  border-radius: 2px;
  left: 0;
  transition: transform 0.25s ease, opacity 0.2s ease, background-color 0.2s ease;
}
.hamburger span:nth-child(1) { top: 0; }
.hamburger span:nth-child(2) { top: 9px; }
.hamburger span:nth-child(3) { top: 18px; }

.hamburger.is-open span:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}
.hamburger.is-open span:nth-child(2) {
  opacity: 0;
}
.hamburger.is-open span:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

.backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.25s ease, visibility 0.25s ease;
  z-index: 999;
}
.backdrop.is-visible {
  opacity: 1;
  visibility: visible;
}

/* Боковая панель-меню (бургер) на всех экранах */
.main-nav {
  position: fixed;
  top: 72px;
  right: 32px;
  width: 280px;
  background: linear-gradient(180deg, rgba(25,25,25,0.96) 0%, rgba(18,18,18,0.96) 100%);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 14px 12px;
  border-radius: 12px 0 0 12px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.35);
  max-height: calc(100vh - 96px);
  overflow-y: auto;
  transform: translateX(104%);
  opacity: 0;
  transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.35s ease;
  will-change: transform;
}

.main-nav.is-open {
  transform: translateX(0);
  opacity: 1;
}

.main-nav a {
  color: var(--text-color);
  padding: 12px 18px 12px 22px;
  text-decoration: none;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  width: 100%;
  transform: translateX(8px);
  opacity: 0;
  transition: transform 0.35s ease, opacity 0.35s ease, color 0.2s ease;
  position: relative;
}

.main-nav a::before {
  content: "";
  position: absolute;
  left: 6px;
  top: 50%;
  transform: translateY(-50%);
  height: 60%;
  width: 0;
  background: var(--accent-color);
  border-radius: 2px;
  transition: width 0.25s ease;
}

.main-nav a:hover::before, .main-nav a.router-link-exact-active::before {
  width: 3px;
}

.main-nav a:hover { color: #ffffff; }

.main-nav.is-open a {
  transform: translateX(0);
  opacity: 1;
}

.main-nav a.router-link-exact-active {
  color: var(--accent-color);
}

/* Небольшие задержки появления пунктов меню */
.main-nav.is-open a:nth-child(1) { transition-delay: 0.05s; }
.main-nav.is-open a:nth-child(2) { transition-delay: 0.10s; }
.main-nav.is-open a:nth-child(3) { transition-delay: 0.15s; }
.main-nav.is-open a:nth-child(4) { transition-delay: 0.20s; }
.main-nav.is-open a:nth-child(5) { transition-delay: 0.25s; }
.main-nav.is-open a:nth-child(6) { transition-delay: 0.30s; }
.main-nav.is-open a:nth-child(7) { transition-delay: 0.35s; }

.layout { min-height: 100vh; }
.layout--static { display: flex; flex-direction: column; }

.main-footer {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  display: flex;
  gap: 20px;
}

.layout--static .main-footer {
  position: static;
  transform: none;
  margin-top: auto;
  padding: 20px 16px;
  justify-content: center;
}

.main-footer a {
  color: var(--text-color);
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
  position: relative;
  transition: color 0.3s ease;
}

.main-footer a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--accent-color);
  transition: width 0.3s ease;
}

.main-footer a:hover::after {
  width: 100%;
}

/* Мобайл версия: статический футер внизу */
@media (max-width: 768px) {
  .layout--static .main-footer {
    position: static;
    bottom: auto;
    left: auto;
    transform: none;
    position: relative;
    margin-top: auto;
    padding: 20px 16px;
    justify-content: center;
  }
  
  .layout {
    min-height: 100vh !important;
    display: flex !important;
    flex-direction: column !important;
  }
}

/* spacer больше не нужен */
</style>