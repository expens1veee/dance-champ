<template>
  <div class="page-view">
    <PageHeader title="КГО" subtitle="Команда Главного Организатора" />
    <div class="content-wrapper">
      <p class="intro-text">Каждый участник команды главного организатора чемпионата фестиваля многогранен и неповторим</p>

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
import TaisiyaPhoto from '@/assets/kgo/Taisiya.jpg'
import VdovinaPhoto from '@/assets/kgo/Vdovina.jpg'
import ObraztsovaPhoto from '@/assets/kgo/Obraztsova.jpg'
import FrolovaPhoto from '@/assets/kgo/Frolova.jpg'
import PanovaPhoto from '@/assets/kgo/Panova.jpg'
import VishnyakovPhoto from '@/assets/kgo/Vishnyakov.jpg'
import StruninaPhoto from '@/assets/kgo/Strunina.jpg'
import AfanasyevPhoto from '@/assets/kgo/Afanasyev.jpg'
import DanilenkoPhoto from '@/assets/kgo/Danilenko.jpg'
import RakovaPhoto from '@/assets/kgo/Rakova.jpg'
import SavinovaPhoto from '@/assets/kgo/Savinova.jpg'
import Baimurzina from '@/assets/kgo/Baimurzina.JPG'
import Sogomonyan from '@/assets/kgo/Sogomonyan.JPG'


// Информация КГО
const kgoMembers = ref([
  { name: 'Шевченко Таисия', role: 'Главный Организатор Чемпионата', photo: TaisiyaPhoto },
  { name: 'Вдовина Александра', role: 'Заместитель ГО', photo: VdovinaPhoto },
  { name: 'Образцова Александра', role: 'Хореограф Чемпионата', photo: ObraztsovaPhoto },
  { name: 'Фролова Александра', role: 'Ответственная за менторов', photo: FrolovaPhoto },
  { name: 'Панова Юлия', role: 'Ответственная за дизайн', photo: PanovaPhoto },
  { name: 'Вишняков Егор', role: 'Ответственный за спонсорство', photo: VishnyakovPhoto },
  { name: 'Струнина Елена', role: 'Ответственная за фото', photo: StruninaPhoto },
  { name: 'Афанасьев Артём', role: 'Ответственный за видео', photo: AfanasyevPhoto },
  { name: 'Согомонян София', role: 'Ответственная за декор', photo: Sogomonyan },
  { name: 'Даниленко Анастасия', role: 'Ответственная за SMM', photo: DanilenkoPhoto },
  { name: 'Ракова Александра', role: 'Ответственная за внешние связи', photo: RakovaPhoto },
  { name: 'Баймурзина Дарина', role: 'Менеджер финала', photo: Baimurzina },
  { name: 'Савинова Алина', role: 'Технический куратор', photo: SavinovaPhoto }
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