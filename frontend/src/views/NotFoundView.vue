<template>
  <div class="page-view">
    <PageHeader title="404" subtitle="Страница не найдена" />
    <div class="content-wrapper">
      <div class="error-content">
        <div class="error-icon">
          <svg width="120" height="120" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="currentColor"/>
          </svg>
        </div>
        
        <h2>Ой! Такой страницы не существует</h2>
        <p>Возможно, вы перешли по неправильной ссылке или страница была перемещена.</p>
        
        <div class="suggestions">
          <h3>Что можно сделать:</h3>
          <ul>
            <li>Проверьте правильность адреса</li>
            <li>Вернитесь на <RouterLink to="/">главную страницу</RouterLink></li>
            <li>Используйте меню для навигации</li>
          </ul>
        </div>
        
        <div class="action-buttons">
          <RouterLink to="/" class="btn btn-primary">На главную</RouterLink>
          <RouterLink to="/contacts" class="btn btn-secondary">Контакты</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import PageHeader from '../components/PageHeader.vue'
</script>

<style scoped>
.content-wrapper {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  padding: 40px 20px;
}

.error-content {
  background: rgba(0,0,0,0.25);
  border: 1px solid rgba(229,57,53,0.35);
  border-radius: 15px;
  padding: 40px 30px;
}

.error-icon {
  color: var(--accent-color);
  margin-bottom: 30px;
  opacity: 0.8;
}

.error-icon svg {
  width: 80px;
  height: 80px;
}

h2 {
  color: var(--text-color);
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0 0 20px 0;
}

p {
  color: #cfcfcf;
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0 0 30px 0;
}

.suggestions {
  text-align: left;
  background: rgba(0,0,0,0.15);
  border-radius: 10px;
  padding: 25px;
  margin: 30px 0;
}

.suggestions h3 {
  color: var(--accent-color);
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0 0 15px 0;
}

.suggestions ul {
  margin: 0;
  padding-left: 20px;
  color: #cfcfcf;
}

.suggestions li {
  margin-bottom: 8px;
  line-height: 1.5;
}

.suggestions a {
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 500;
}

.suggestions a:hover {
  text-decoration: underline;
}

.action-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-top: 30px;
}

.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.btn-primary {
  background: var(--accent-color);
  color: white;
  border-color: var(--accent-color);
}

.btn-primary:hover {
  background: rgba(229,57,53,0.8);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(229,57,53,0.3);
}

.btn-secondary {
  background: transparent;
  color: var(--text-color);
  border-color: rgba(229,57,53,0.35);
}

.btn-secondary:hover {
  background: rgba(229,57,53,0.1);
  border-color: rgba(229,57,53,0.6);
  transform: translateY(-2px);
}

/* Адаптивность */
@media (max-width: 768px) {
  .content-wrapper {
    padding: 20px 15px;
  }
  
  .error-content {
    padding: 30px 20px;
  }
  
  h2 {
    font-size: 1.5rem;
  }
  
  .action-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 200px;
  }
}
</style>
