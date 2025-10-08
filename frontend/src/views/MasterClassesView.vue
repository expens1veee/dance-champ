<template>
  <div class="page-view">
    <PageHeader title="Мастер-классы" subtitle="Лучшие педагоги" />
    <div class="content-wrapper">
      <transition-group name="cards" tag="div" class="teachers-grid">
        <div v-for="teacher in teachers" :key="teacher.name" class="teacher-card">
          <div class="card-header">
            <img :src="teacher.photo" alt="Фото педагога" :class="['teacher-photo', teacher.photoClass]">
            <div class="teacher-info">
              <h3 class="name">{{ teacher.name }}</h3>
            </div>
          </div>
          
          <div class="achievements">
            <h4>Достижения:</h4>
            <ul class="achievements-list">
              <li v-for="achievement in teacher.achievements" :key="achievement">
                {{ achievement }}
              </li>
            </ul>
          </div>
          
          <div class="experience">
            <p class="exp-text">{{ teacher.experience }}</p>
            <p class="description">{{ teacher.description }}</p>
          </div>
        </div>
      </transition-group>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import PageHeader from '../components/PageHeader.vue'
import markPhoto from '@/assets/teachers/mark_gorodilkin.jpg'
import ekaterinaPhoto from '@/assets/teachers/ekaterina_beleva.jpg'
import arrrPhoto from '@/assets/teachers/arrr.jpg'
import tinaPhoto from '@/assets/teachers/tina_khanova.jpg'

const teachers = ref([
  {
    name: 'Марк Городилкин',
    photo: markPhoto,
    photoClass: 'mark-photo',
    achievements: [
      'Хореограф двух филиалов MDC NRG',
      'Выступление с Егором Кридом на ВТБ Арене (40000 зрителей)',
      'Победитель Всемирной танцевальной олимпиады (solo)',
      'Чемпион World Of Dance в Португалии 2019',
      'Финалист чемпионата Европы в Чехии',
      'Многократный чемпион ЦФО Московской области'
    ],
    experience: 'Режиссер клипов и сниппетов для артистов',
    description: 'Работал с артистами: Егор Крид, Сергей Лазарев, Artik&Asti, МОТ, Женя Лизогуб, Кристина Асмус и др. Участвовал в концертах: Жара, Жара Фест, Муз ТВ, Премьера ТНТ.'
  },
  {
    name: 'Екатерина Белёва',
    photo: ekaterinaPhoto,
    achievements: [
      'Кандидат в Мастера Спорта по художественной гимнастике',
      'Тренер по стретчингу в студии Stretching Space',
      'Член танцевального объединения Firsov The Company',
      'Призёр RELEASE CONTEST в номинации BEST SOLO',
      'Призёр VOLGA CHAMP в составе команды 262',
      'Бывший член команды Escape и команды 262'
    ],
    experience: 'Профессиональная растяжка и пластика',
    description: 'Участница творческих и режиссерских проектов, клипов и концертов. Специалист по современной хореографии.'
  },
  {
    name: 'Ар',
    photo: arrrPhoto,
    achievements: [
      'Участник команды «А+» под руководством Алинучи',
      'Участник команды «Reborn» под руководством Элиши',
      'Основатель и руководитель команды «tvARi»',
      'Призёр Волга Чемп и других чемпионатов',
      'Экс-специалист по AFRO стилям',
      'Множественные призовые места соло и в команде'
    ],
    experience: 'Танцевальный стаж: 10 лет • Преподавательский стаж: 3 года',
    description: 'Сейчас развивает собственный уникальный стиль, не привязываясь к конкретным направлениям. Ищет свой танец.'
  },
  {
    name: 'Тина Ханова',
    photo: tinaPhoto,
    achievements: [
      'Состояла в команде Red Haze; участница Country Haze Show и Rema Dance Love Show',
      'Состояла в команде Hot Collection',
      'Состою в команде OFFSIDE FAM',
      'Участник Volga Champ и Лига Танца (полуфинал)',
      'Создала команду HUNTI; сотрудничество с исполнителями и коммерческие выступления',
      'Организатор собственного танцевального контеста'
    ],
    experience: 'Преподает High Heels и Girly Hip Hop. Более 150 учеников на регулярных группах ежемесячно',
    description: 'Развивает женственный и драйвовый стиль. Ведёт регулярные группы и проекты с артистами.'
  }
])
</script>

<style scoped>
.content-wrapper { max-width: 1200px; margin: 0 auto; }
.teachers-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
  gap: 30px; 
  margin-top: 20px;
}

.teacher-card { 
  background: rgba(0,0,0,0.25); 
  border: 1px solid rgba(229,57,53,0.35); 
  padding: 25px; 
  border-radius: 15px; 
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.teacher-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  border-color: rgba(229,57,53,0.6);
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  gap: 15px;
}

.teacher-photo {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center center;
  border: 2px solid var(--accent-color);
  flex-shrink: 0;
}

.teacher-photo.mark-photo {
  object-position: center top;
}

.teacher-info {
  flex: 1;
  text-align: left;
}

.name { 
  margin: 0; 
  font-size: 1.3rem; 
  font-weight: 700;
  color: var(--text-color);
}

.achievements {
  margin-bottom: 20px;
  text-align: left;
}

.achievements h4 {
  margin: 0 0 10px 0;
  font-size: 1rem;
  color: var(--accent-color);
  font-weight: 600;
}

.achievements-list {
  margin: 0;
  padding-left: 18px;
  list-style: none;
}

.achievements-list li {
  position: relative;
  margin-bottom: 6px;
  color: #cfcfcf;
  font-size: 0.9rem;
  line-height: 1.4;
}

.achievements-list li::before {
  content: "•";
  color: var(--accent-color);
  position: absolute;
  left: -15px;
  font-weight: bold;
}

.experience {
  text-align: left;
}

.exp-text {
  margin: 0 0 8px 0;
  color: var(--accent-color);
  font-weight: 600;
  font-size: 0.9rem;
}

.description {
  margin: 0;
  color: #bbb;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* Плавная анимация карточек */
.cards-enter-from, .cards-leave-to { 
  opacity: 0; 
  transform: translateY(20px) scale(0.95); 
}
.cards-enter-active, .cards-leave-active { 
  transition: all 0.4s ease; 
}

/* Адаптивность */
@media (max-width: 768px) {
  .teachers-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .teacher-card {
    padding: 20px;
  }
  
  .card-header {
    flex-direction: column;
    text-align: center;
    gap: 10px;
  }
  
  .teacher-info {
    text-align: center;
  }
  
  .teacher-photo {
    width: 110px;
    height: 110px;
  }
  
  .achievements, .experience {
    text-align: center;
  }
}
</style>