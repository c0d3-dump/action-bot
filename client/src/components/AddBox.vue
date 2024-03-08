<script setup>
import { ref, defineEmits } from "vue";
const text = ref("");
const emit = defineEmits(['submit'])

function addTodo() {
  emit("submit", text.value);
  text.value = "";
}

</script>

<template>
  <div class="input-section">
    <section class="create-todo">
      <form @submit.prevent="addTodo">
        <h3>What do you plan on doing🙂?</h3>
        <div class="todo-box">
          <input type="text" placeholder="e.g. email your boss" v-model="text" />
          <input type="submit" value="ADD" />
        </div>
      </form>
    </section>
  </div>
</template>

<style scoped>
.input-section,
.todo-section {
  border: 1px solid rgb(47, 47, 47);
  border-radius: 10px;
  margin-top: 30px;
}

.create-todo h3 {
  text-align: center;
}

.create-todo input[type="text"] {
  display: block;
  width: 100%;
  font-size: 1.125rem;
  padding: 1rem 1.5rem;
  color: black;
  background-color: whitesmoke;
  border-radius: 0.5rem;
  border: none;
  box-shadow: none;
}

section {
  margin-top: 2rem;
  margin-bottom: 2rem;
  padding-left: 1.5rem;
  padding-right: 1.5em;
}

.create-todo .todo-box {
  margin-top: 12px;
  display: flex;
  align-items: center;
}

.create-todo input[type="submit"] {
  display: block;
  width: 16%;
  font-size: 1.125rem;
  padding: 1rem 1.5rem;
  color: #fff;
  background-color: green;
  border-radius: 0.5rem;
  box-shadow: var(--personal-glow);
  cursor: pointer;
  transition: 0.2s ease-in-out;
}

.create-todo input[type="submit"]:hover {
  opacity: 0.75;
}
</style>
