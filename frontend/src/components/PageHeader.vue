<template>
  <header class="page-header" :class="variant">
    <h1 class="title">{{ title }}</h1>
    <p v-if="subtitle" class="subtitle">{{ subtitle }}</p>
  </header>
  
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: { type: String, required: true },
  subtitle: { type: String, default: '' },
  align: { type: String, default: 'center' }, // 'left' | 'center'
  accent: { type: Boolean, default: true } // включает декоративную линию/градиент
})

const variant = computed(() => props.align === 'left' ? 'left' : 'center')
</script>

<style scoped>
.page-header {
  margin: 8px auto 28px;
  max-width: 980px;
  padding: 24px 12px 10px;
  position: relative;
}

.page-header.center { text-align: center; }
.page-header.left { text-align: left; }

.title {
  margin: 0;
  font-size: 2.2rem;
  line-height: 1.15;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.subtitle { margin: 10px 0 0; color: #bbb; }

/* Декоративный акцент под заголовком */
.page-header::after {
  content: '';
  display: block;
  width: 120px;
  height: 4px;
  margin: 14px auto 0;
  background: linear-gradient(90deg, var(--accent-color), transparent);
}
.page-header.left::after {
  margin-left: 0;
}
</style>


