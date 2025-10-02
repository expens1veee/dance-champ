<template>
  <div class="page-view">
    <PageHeader title="КГО" subtitle="Команда Главного Организатора" />
    <div class="content-wrapper">
      <p class="intro-text">«Каждый участник команды главного организатора чемпионата фестиваля многогранен и неповторим»</p>

      <div class="kgo-grid">
        <div v-for="member in kgoMembers" :key="member.name" class="kgo-card">
          <img :src="member.photo" :alt="member.name" class="member-photo">
          <h3 class="name">{{ member.name }}</h3>
          <p class="role">{{ member.role }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import PageHeader from '../components/PageHeader.vue'
// Информация КГО
const kgoMembers = ref([
  { name: 'Шевченко Таисия', role: 'Главный Организатор Чемпионата', photo: '/src/assets/kgo/Taisiya.jpg' },
  { name: 'Вдовина Александра', role: 'Заместитель ГО', photo: '/src/assets/kgo/Vdovina.jpg' },
  { name: 'Образцова Александра', role: 'Хореограф Чемпионата', photo: '/src/assets/kgo/Obraztsova.jpg' },
  { name: 'Фролова Александра', role: 'Ответственная за менторов', photo: '/src/assets/kgo/Frolova.jpg' },
  { name: 'Панова Юлия', role: 'Ответственная за дизайн', photo: '/src/assets/kgo/Panova.jpg' },
  { name: 'Вишняков Егор', role: 'Ответственный за спонсорство', photo: '/src/assets/kgo/Vishnyakov.jpg' },
  { name: 'Струнина Елена', role: 'Ответственная за медиа', photo: '/src/assets/kgo/Strunina.jpg' },
  { name: 'Афанасьев Артём', role: 'Ответственный за медиа', photo: '/src/assets/kgo/Afanasyev.jpg' },
  { name: 'Пока неизвестно кто будет', role: 'Ответственный за декор', photo: '/src/assets/kgo/placeholder.jpg' },
  { name: 'Даниленко Анастасия', role: 'Ответственная за SMM', photo: '/src/assets/kgo/Danilenko.jpg' },
  { name: 'Ракова Александра', role: 'Ответственная за внешние связи', photo: '/src/assets/kgo/Rakova.jpg' },
  { name: 'Баймурзина Дарина', role: 'Менеджер финала', photo: '/src/assets/kgo/Baimurzina.jpg' },
  { name: 'Савинова Алина', role: 'Технический куратор', photo: '/src/assets/kgo/Savinova.jpg' }
]);
</script>

<style scoped>
.content-wrapper { max-width: 980px; margin: 0 auto; }
.intro-text { text-align: center; font-style: italic; margin-bottom: 36px; font-size: 1.2rem; color: #cfcfcf; }
.kgo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
}
.kgo-card { text-align: center; background: rgba(0,0,0,0.25); border: 1px solid rgba(229,57,53,0.35); border-radius: 10px; padding: 18px; }
.member-photo {
  width: 190px;
  height: 190px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
  border: 2px solid var(--accent-color);
}
.kgo-card .name { margin: 6px 0 4px; font-size: 1.1rem; letter-spacing: 0.02em; }
.kgo-card .role { margin: 0; color: #bbb; }
</style>