<template>
  <div class="page-view">
    <PageHeader title="Контакты" subtitle="Свяжитесь с командой чемпионата" />
    <div class="content-wrapper">
      <p class="intro-text">«По всем вопросам обращаться:…»</p>

      <ul class="contacts-list">
        <li><span>Главный организатор</span> — Таисия Шевченко: <a href="https://vk.com/taisia_shevchenko" target="_blank">VK</a></li>
        <li><span>Регистрация и вопросы</span> — <a href="mailto:dancechempten@mail.ru">dancechempten@mail.ru</a></li>
        <li><span>VK-группа</span> — <a href="https://vk.com/dancechempten" target="_blank">https://vk.com/dancechempten</a></li>
      </ul>

      <div class="privacy-link">
        <a @click="downloadPolicyPDF">Офёрта и политика конфиденциальности</a>
      </div>
    </div>

    <!-- PDF файл скачивается при клике -->
  </div>
</template>

<script setup>
import PageHeader from '../components/PageHeader.vue'
import { downloadPDF } from '../utils/pdfDownload.js'

function downloadPolicyPDF() {
  downloadPDF('privacy-policy.pdf', 'Офёрта_и_политика_конфиденциальности_TENЬ.pdf');
}
</script>

<style scoped>
.page-view { text-align: center; }
.content-wrapper { max-width: 820px; margin: 0 auto; }
.intro-text { font-size: 1.15rem; margin-bottom: 24px; color: #cfcfcf; }
.contacts-list { list-style: none; padding: 0; margin: 0 auto; display: inline-block; text-align: left; font-size: 1.1rem; line-height: 1.85; }
.contacts-list span { color: var(--accent-color); font-weight: 700; }
.privacy-link { margin-top: 26px; }

/* стили модального окна больше не нужны */
</style>