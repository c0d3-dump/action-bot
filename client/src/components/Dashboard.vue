<script setup>
import { ref, nextTick } from "vue";
import AddBox from "./AddBox.vue";
import Todo from "./Todo.vue";
import Action from "./Action.vue";

const todos = ref([]);

function addTodo(value) {
  if (value.trim() === "") {
    return;
  }

  todos.value.unshift({
    todo: value,
    done: false,
  });
}

function deleteTodo(todo) {
  todos.value = todos.value.filter((x) => x.todo !== todo.todo);
}

function markTodo(tod) {
  todos.value = todos.value.map((x) => ({ todo: x.todo, done: x.todo === tod ? !x.done : x.done }));
}

function doActions(actions) {
  for (const action of actions) {
    switch (action.TYPE) {
      case "AT":
        addTodo(action["CNT"]);
        break;
      case "RT":
        deleteTodo({
          todo: action["CNT"],
          done: false
        });
        break;
      case "CT":
        markTodo(action["CNT"],);
        break;
      default:
        break;
    }
  }
}

</script>

<template>
  <Action @doActions="doActions"></Action>

  <div class="base">
    <AddBox @submit="addTodo"></AddBox>

    <div class="todo-section">
      <section class="todo-list">
        <h2 v-show="todos.length === 0">No Todos Here😞</h2>
        <div class="list">
          <div v-for="todo in todos" :class="`todo-item ${todo.done && 'done'}`">
            <Todo :todo="todo" @deleteTodo="deleteTodo" @markTodo="markTodo"></Todo>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.base {
  max-width: 50%;
  margin-left: auto;
  margin-right: auto;
}

section {
  margin-top: 2rem;
  margin-bottom: 2rem;
  padding-left: 1.5rem;
  padding-right: 1.5em;
}

h2 {
  text-align: center;
}

.greeting .title {
  display: flex;
}

.greeting .title input {
  margin-left: 0.5rem;
  flex: 1 1 0%;
  min-width: 0;
}

.greeting .title,
.greeting .title input {
  color: white;
  font-size: 2rem;
  font-weight: 700;
}

.todo-list .list {
  margin: 1rem 0;
}

.todo-list .todo-item {
  display: flex;
  align-items: center;
  background-color: #17181d;
  padding: 1rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  margin-bottom: 1rem;
}
</style>
