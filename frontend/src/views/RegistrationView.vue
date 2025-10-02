<template>
  <div class="page-view">
    <PageHeader title="Регистрация" subtitle="Выберите формат участия" />

    <div class="content-wrapper">
      <p class="intro-text">Скоро в РЭУ им. Г. В. Плеханова состоится один из самых ярких студенческих чемпионатов. Выберите номинацию и оформите участие.</p>

      <div class="reg-grid">
        <a class="reg-card" @click="openConsentModal('https://forms.gle/your-team-form')">
          <h3>Команды</h3>
          <p>Для коллективов от 8 человек</p>
        </a>
        <a class="reg-card" @click="openConsentModal('https://forms.gle/your-solo-form')">
          <h3>SOLO</h3>
          <p>Индивидуальная заявка</p>
        </a>
        <a class="reg-card" @click="openConsentModal('https://forms.gle/your-mini-team-form')">
          <h3>Мини-команды</h3>
          <p>От 2 до 7 человек</p>
        </a>
      </div>

      <div class="info-actions">
        <button class="btn" @click="openInfoModal('conditions')">Условия</button>
        <button class="btn" @click="openInfoModal('scoring')">Баллы</button>
      </div>
    </div>

    <transition name="fade">
      <div v-if="showConsentModal" class="modal-overlay" @click.self="showConsentModal = false">
        <div class="modal-content">
        <h3>Согласие на обработку персональных данных</h3>
        <p>Нажимая "Принимаю", вы подтверждаете свое согласие на обработку персональных данных в соответствии с политикой конфиденциальности.</p>
        <div class="modal-buttons">
          <button class="btn" @click="proceedToForm">Принимаю</button>
          <button class="btn-secondary" @click="showConsentModal = false">Отмена</button>
        </div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <div v-if="showInfoModal" class="modal-overlay" @click.self="showInfoModal = false">
        <div class="modal-content">
        <h3 v-if="modalContent === 'conditions'">Условия подачи анкет</h3>
        <p v-if="modalContent === 'conditions'">Здесь будет информация по подаче анкет на каждую номинацию.</p>

        <h3 v-if="modalContent === 'scoring'">Расчет баллов</h3>
        <p v-if="modalContent === 'scoring'">Здесь будет информация о расчетах баллов.</p>

        <div class="modal-buttons">
          <button class="btn" @click="showInfoModal = false">Закрыть</button>
        </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import PageHeader from '../components/PageHeader.vue'

const showConsentModal = ref(false)
const showInfoModal = ref(false)
const modalContent = ref('')
const targetUrl = ref('')

function openConsentModal(url) {
  targetUrl.value = url;
  showConsentModal.value = true;
}

function proceedToForm() {
  window.open(targetUrl.value, '_blank');
  showConsentModal.value = false;
}

function openInfoModal(type) {
  modalContent.value = type;
  showInfoModal.value = true;
}
</script>

<style scoped>
.content-wrapper { max-width: 980px; margin: 0 auto; }
.intro-text { font-size: 1.15rem; text-align: center; max-width: 760px; margin: 16px auto 28px; color: #cfcfcf; }
.reg-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 18px; }
.reg-card { display: block; text-decoration: none; color: var(--text-color); background: rgba(0,0,0,0.25); border: 1px solid rgba(229,57,53,0.35); padding: 20px; border-radius: 10px; text-align: center; }
.reg-card h3 { margin: 0 0 6px; text-transform: uppercase; letter-spacing: 0.06em; }
.reg-card p { margin: 0; color: #bbb; }
.info-actions { display: flex; gap: 12px; justify-content: center; margin-top: 18px; }

/* Стили для модальных окон */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: flex; justify-content: center; align-items: center; z-index: 1002; }
.modal-content { background: #2c2c2c; padding: 30px; border-radius: 10px; max-width: 520px; text-align: center; border: 1px solid rgba(229,57,53,0.35); }
.modal-buttons { margin-top: 20px; display: flex; justify-content: center; gap: 15px; }
.btn-secondary { background: transparent; border: 1px solid rgba(255,255,255,0.35); color: #fff; }
.btn-secondary:hover { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.5); }

/* Плавное появление модалок */
.fade-enter-from, .fade-leave-to { opacity: 0; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.25s ease; }
</style>