<template>
  <div class="page-view">
    <PageHeader title="Положение" subtitle="Основные правила и документы" />
    <div class="content-wrapper">
      <div class="summary">
        <p>Здесь располагается краткий текст положения о чемпионате. Основные цели, задачи, правила участия и ключевые моменты, которые должен знать каждый участник перед ознакомлением с полной версией документа.</p>
      </div>
      <a href="./docs/regulations.pdf" target="_blank" class="btn">Полное положение</a>
    </div>
  </div>
</template>

<script setup>
import PageHeader from '../components/PageHeader.vue'
</script>

<style scoped>
.content-wrapper { max-width: 980px; margin: 0 auto; text-align: center; }
.summary {
  background: #252525;
  padding: 24px;
  margin: 0 auto 24px;
  line-height: 1.6;
  border: 1px solid rgba(229,57,53,0.35);
  border-radius: 10px;
}
.page-view { text-align: center; }

/* Убираем подчеркивание с кнопки */
.btn {
  text-decoration: none !important;
}
</style>