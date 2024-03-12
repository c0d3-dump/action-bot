<script setup>
import { defineEmits, defineProps } from "vue";
const emit = defineEmits(['deleteTodo', 'markTodo'])
const props = defineProps(['todo'])

function delTodo() {
  emit('deleteTodo', props.todo);
}

function markTodo(e) {
  emit('markTodo', props.todo);
}

</script>

<template>
  <label>
    <input type="checkbox" :checked="todo.done" @change="markTodo" />
  </label>
  <div class="todo-content">
    {{ todo.todo }}
  </div>
  <div class="actions">
    <button class="delete" @click="delTodo">Delete</button>
  </div>
</template>

<style scoped>
input:not([type="radio"]):not([type="checkbox"]),
button {
  appearance: none;
  border: none;
  outline: none;
  background: none;
  cursor: initial;
}

input[type="checkbox"] {
  height: 25px;
  width: 25px;
  color: green;
}

.bubble.personal::after {
  background-color: var(--personal);
  box-shadow: var(--personal-glow);
}

input:checked~.bubble::after {
  width: 10px;
  height: 10px;
  opacity: 1;
}

label {
  display: block;
  margin-right: 1rem;
  cursor: pointer;
}

.todo-content {
  flex: 1 1 0%;
}

.todo-content input {
  color: white;
  font-size: 1.125rem;
}

.actions {
  display: flex;
  align-items: center;
}

.actions button {
  display: block;
  padding: 0.5rem;
  border-radius: 0.25rem;
  color: #fff;
  cursor: pointer;
  transition: 0.2s ease-in-out;
}

.actions button:hover {
  opacity: 0.75;
}

.actions .edit {
  margin-right: 0.5rem;
  background-color: var(--primary);
}

.actions .delete {
  background-color: var(--danger);
}

.done .todo-content input {
  text-decoration: line-through;
  color: rgba(165, 165, 165, 0.752);
}
</style>
