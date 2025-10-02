<template>
  <div v-if="show" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h3>Согласие на обработку персональных данных</h3>
      <p>Нажимая "Согласен", вы даете согласие на обработку ваших персональных данных...</p>
      <button @click="agree">Согласен</button>
      <button @click="close">Отмена</button>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['close', 'agree'])
defineProps({
  show: Boolean
})

function close() {
  emit('close')
}

function agree() {
  emit('agree')
}
</script>

<style scoped>
/* Стили для модального окна */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background: #2c2c2c;
  color: var(--text-color);
  padding: 20px;
  border-radius: 5px;
}
</style>