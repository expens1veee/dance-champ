<template>
  <div class="page-view">
    <PageHeader title="Номинации" subtitle="Выберите номинацию" />
    <div class="content-wrapper">
      <div class="nominations-grid">
        <RouterLink
          v-for="nomination in nominations"
          :key="nomination.slug"
          :to="{ name: 'nomination-detail', params: { slug: nomination.slug } }"
          class="nomination-button"
        >
          {{ nomination.title }}
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import PageHeader from '../components/PageHeader.vue'

// ЗАМЕНИТЕ НА СВОИ ДАННЫЕ
const nominations = ref([
  {
    slug: 'solo-dance',
    title: 'SOLO DANCE',
    description: 'Подробная информация о номинации соло. Требования, критерии оценки, временные рамки и т.д.'
  },
  {
    slug: 'best-dance-team',
    title: 'BEST DANCE TEAM',
    description: 'Подробная информация о номинации для команд. Требования к количеству участников, стилю, музыке и т.д.'
  },
  {
    slug: 'best-dance-mini-team',
    title: 'BEST DANCE MINI TEAM',
    description: 'Подробная информация о номинации для мини-команд. Критерии оценки, временные рамки и требования.'
  }
]);
</script>

<style scoped>
.nomination-item {
  background: #252525;
  margin-bottom: 10px;
  border-radius: 5px;
}
.nomination-header {
  padding: 20px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nomination-header h3 { margin: 0; }
.nomination-details {
  padding: 0 20px 20px;
  border-top: 1px solid #444;
}

.details-link {
  display: inline-block;
  margin-top: 10px;
  color: var(--accent-color);
  text-decoration: none;
}

.content-wrapper { max-width: 980px; margin: 0 auto; }
.nominations-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 20px; }

.nomination-button {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80px;
  text-align: center;
  background: rgba(0,0,0,0.25);
  border-radius: 10px;
  text-decoration: none;
  color: var(--text-color);
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  border: 1px solid rgba(229,57,53,0.35);
  transition: transform 0.15s ease, box-shadow 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
}

.nomination-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.35);
  background: rgba(0,0,0,0.35);
  border-color: rgba(229,57,53,0.55);
}
</style>