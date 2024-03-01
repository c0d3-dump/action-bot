<script setup>
import { ref } from "vue";
import axios from "axios";

const newTask = ref("");
const formData = ref("");
const tasks = ref([]);

const addTask = () => {
  if (newTask.value.trim() !== "") {
    tasks.value.push(newTask.value.trim());
    newTask.value = "";
  }
};

const removeTask = (index) => {
  tasks.value.splice(index, 1);
};

const submitForm = () => {
  const form = new FormData();
  form.append("query", formData.value);

  axios
    .post("http://localhost:3000/api/todo", form, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    })
    .then((response) => {
      console.log("POST request successful:", response.data);

      const type = response.data.type;
      const content = response.data.content;

      switch (type) {
        case "add":
          tasks.value.push(content.trim());
          break;
        case "delete":
          const idx = tasks.value.findIndex((task) => task === content.trim());
          console.log(idx);
          tasks.value.splice(idx, 1);
          break;
        default:
          break;
      }
    })
    .catch((error) => {
      console.error("Error making POST request:", error);
    });
};
</script>

<template>
  <div id="todo">
    <h1>Todo App</h1>
    <div>
      <input
        v-model="newTask"
        @keyup.enter="addTask"
        placeholder="Add a new task"
      />
      <button id="add-todo" @click="addTask">Add</button>
    </div>
    <ul>
      <li v-for="(task, index) in tasks" :key="index">
        {{ task }}
        <button :id="`remove-${task}`" @click="removeTask(index)">
          Remove
        </button>
      </li>
    </ul>
  </div>

  <div>
    <form @submit.prevent="submitForm" class="floating-form">
      <textarea v-model="formData" placeholder="Enter your data"></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style>
#todo {
  text-align: center;
  color: white;
  margin: auto;
}

input {
  padding: 5px;
  margin-right: 5px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 5px;
}

button {
  cursor: pointer;
}

.floating-form {
  position: fixed;
  bottom: 10px;
  right: 10px;
  display: flex;
  flex-direction: column;
  background-color: #f0f0f0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

textarea {
  resize: none;
  height: 200px;
  width: 200px;
  margin-bottom: 10px;
}
</style>
