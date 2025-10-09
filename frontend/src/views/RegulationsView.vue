<template>
  <div class="page-view">
    <PageHeader title="Положение" subtitle="Основные правила и документы" />
    <div class="content-wrapper">
      <div class="summary">
        <h3>О чемпионате TENЬ</h3>
        <p><strong>TENЬ</strong> — это студенческий танцевальный чемпионат, объединяющий талантливых танцоров из различных учебных заведений. Наша цель — создать платформу для творческого самовыражения, обмена опытом и развития танцевального искусства среди студенческой молодежи.</p>
        
        <h4>Основные номинации:</h4>
        <ul>
          <li><strong>SOLO</strong> — индивидуальные выступления</li>
          <li><strong>КОМАНДЫ</strong> — групповые номера (8-30 человек)</li>
          <li><strong>МИНИ-КОМАНДЫ</strong> — малые группы (2-7 человек)</li>
        </ul>
        
        <h4>Критерии оценки:</h4>
        <ul>
          <li>Техника исполнения и синхронность</li>
          <li>Музыкальность и ритм</li>
          <li>Артистизм и подача</li>
          <li>Оригинальность номера</li>
          <li>Сценическое поведение</li>
        </ul>
        
        <h4>Участие:</h4>
        <p>К участию приглашаются студенты всех курсов и специальностей. Регистрация открыта до начала чемпионата. Все участники получают сертификаты, а победители — дипломы и призы.</p>
        
        <p><em>Для получения подробной информации о правилах, требованиях и процедурах участия скачайте полное положение.</em></p>
      </div>
      <a @click="downloadRegulationsPDF" class="btn">Полное положение</a>
    </div>
  </div>
</template>

<script setup>
import PageHeader from '../components/PageHeader.vue'
import { downloadPDF } from '../utils/pdfDownload.js'

function downloadRegulationsPDF() {
  downloadPDF('polozhenie.pdf', 'Полное_положение_TENЬ.pdf');
}
</script>

<style scoped>
.content-wrapper { max-width: 980px; margin: 0 auto; text-align: center; }
.summary {
  background: rgba(0,0,0,0.25);
  padding: 30px;
  margin: 0 auto 30px;
  line-height: 1.6;
  border: 1px solid rgba(229,57,53,0.35);
  border-radius: 10px;
  text-align: left;
}

.summary h3 {
  color: var(--accent-color);
  margin: 0 0 20px 0;
  font-size: 1.4rem;
  font-weight: 700;
}

.summary h4 {
  color: var(--accent-color);
  margin: 20px 0 10px 0;
  font-size: 1.1rem;
  font-weight: 600;
}

.summary ul {
  margin: 10px 0 20px 0;
  padding-left: 20px;
}

.summary li {
  margin-bottom: 8px;
  color: #cfcfcf;
}

.summary p {
  margin: 0 0 15px 0;
  color: #cfcfcf;
}

.summary strong {
  color: var(--accent-color);
}

.summary em {
  color: #bbb;
  font-style: italic;
}
.page-view { text-align: center; }

/* Убираем подчеркивание с кнопки */
.btn {
  text-decoration: none !important;
}
</style>