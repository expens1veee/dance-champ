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
        <a @click="openPolicyPDF">Офёрта и политика конфиденциальности</a>
      </div>
    </div>

    <!-- модальное окно удалено, теперь открываем PDF файл -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import PageHeader from '../components/PageHeader.vue'

const showPolicyModal = ref(false);

function openPolicyPDF() {
  window.open('/docs/privacy-policy.pdf', '_blank');
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