<template>
  <div class="page-view">
    <PageHeader :title="title" subtitle="Подробные критерии и правила" />
    <div class="content-wrapper">
      <RouterLink to="/nominations" class="back-link">← Назад к номинациям</RouterLink>

      <div class="cards-grid">
        <section class="criteria card">
          <h3>Критерии оценки</h3>
          <ul>
            <li v-for="(criterion, idx) in criteria" :key="idx">{{ criterion }}</li>
          </ul>
        </section>

        <section v-if="rules && rules.length" class="rules card">
          <h3>Правила</h3>
          <ul>
            <li v-for="(rule, idx) in rules" :key="idx">{{ rule }}</li>
          </ul>
        </section>
      </div>

      <section v-if="notes" class="notes card">
        <h3>Примечания</h3>
        <p>{{ notes }}</p>
      </section>
    </div>
  </div>
  
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import PageHeader from '../components/PageHeader.vue'

const route = useRoute()

// Примеры данных по номинациям (можно заменить на загрузку с бэкенда)
const nominationData = {
  'solo-dance': {
    title: 'SOLO DANCE',
    criteria: [
      'Техника исполнения',
      'Музыкальность и ритм',
      'Артистизм и подача',
      'Оригинальность номера',
      'Сценическое поведение'
    ],
    rules: [
      'Продолжительность до 1:30',
      'Музыка без нецензурной лексики',
      'Костюм должен соответствовать стилю'
    ],
    notes: 'Участник выходит один, допускается реквизит.'
  },
  'best-dance-team': {
    title: 'BEST DANCE TEAM',
    criteria: [
      'Синхронность команды',
      'Комбинаторика и формации',
      'Динамика и энергетика',
      'Стилевая чистота',
      'Сценография'
    ],
    rules: [
      'Состав от 8 до 30 человек',
      'Продолжительность 3:30 мин',
      'Музыка без нецензурной лексики',
      'Единая концепция номера'
    ],
    notes: 'Допускаются подгруппы и соло-вставки.'
  },
  'best-dance-mini-team': {
    title: 'BEST DANCE MINI TEAM',
    criteria: [
      'Синхронность команды',
      'Комбинаторика и формации',
      'Динамика и энергетика',
      'Стилевая чистота',
      'Сценография'
    ],
    rules: [
      'Состав от 2 до 7 человек',
      'Продолжительность 2:30 мин',
      'Музыка без нецензурной лексики',
      'Единая концепция номера'
    ],
    notes: 'Допускаются подгруппы и соло-вставки.'
  }
}

const slug = computed(() => String(route.params.slug || ''))
const current = computed(() => nominationData[slug.value] || null)

const title = computed(() => current.value?.title || 'Номинация')
const criteria = computed(() => current.value?.criteria || [])
const rules = computed(() => current.value?.rules || [])
const notes = computed(() => current.value?.notes || '')
</script>

<style scoped>
.content-wrapper { max-width: 980px; margin: 0 auto; }
.back-link {
  display: inline-block;
  margin-bottom: 16px;
  text-decoration: none;
  color: var(--accent-color);
}

.cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin-bottom: 18px; }
.card { background: rgba(0,0,0,0.25); border: 1px solid rgba(229,57,53,0.35); border-radius: 10px; padding: 18px; }
.criteria, .rules, .notes { margin-top: 0; }

ul {
  margin: 0;
  padding-left: 18px;
}
</style>


