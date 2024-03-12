<script setup>
import { ref, defineEmits, nextTick } from "vue";
import axios from "axios";
const text = ref("");
const actions = ref([]);
const isAiBot = ref(true);
const emit = defineEmits(['doActions'])
const chatContainer = ref(null);

const chats = ref([]);

async function makePrediction() {
  if (!text.value) {
    return;
  }

  addChat(text.value, "me");

  const form = new FormData();
  form.append("query", text.value);

  const response = await axios
    .post("http://localhost:3000/api/todo", form, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

  const acts = response.data;

  if (acts.length <= 0) {
    addChat("Please enter valid prompt", "bot");
    text.value = "";
    return;
  }

  actions.value = acts;
  for (const action of acts) {
    if (!action['CNT']) {
      addChat(`Content is missing for '${getType(action.TYPE)}' action. please add here: `, "bot");
      isAiBot.value = false;
      text.value = "";
      return;
    }
  }

  addChat("All the actions have been performed successfully.", "bot");
  emit('doActions', actions.value);
  text.value = "";
}

function getType(todoType) {
  switch (todoType) {
    case "AT":
      return "Add todo"
    case "RT":
      return "Remove todo"
    case "CT":
      return "MarkI todo"
    default:
      break;
  }
}

function interactWithChat() {
  addChat(text.value, "me");

  for (const action of actions.value) {
    if (!action['CNT']) {
      action['CNT'] = text.value;
      text.value = "";
      continue;
    }
    if (!action['CNT']) {
      addChat(`Content is missing for '${action.TYPE}' action. please add here: `, "bot");
      text.value = "";
      return;
    }
  }

  addChat("All the actions have been performed successfully.", "bot");
  emit('doActions', actions.value);
  isAiBot.value = true;
  text.value = "";
}

function addChat(value, from) {
  if (value.trim() === "") {
    return;
  }

  chats.value.push({
    chat: value,
    from
  });

  nextTick(() => {
    scrollToBottom();
  })
}

function scrollToBottom() {
  const chatContainerRef = chatContainer.value;
  chatContainerRef.scrollTop = chatContainerRef.scrollHeight;
}

</script>

<template>
  <form @submit.prevent="isAiBot ? makePrediction() : interactWithChat()" class="floating-form">
    <ul class="chat-box" ref="chatContainer">
      <li v-for="chat in chats">
        <label :class="{ 'green': chat.from === 'me', 'orange': chat.from === 'bot' }">{{ chat.from }}: </label>
        <label>{{ chat.chat }}</label>
      </li>
    </ul>

    <div class="prediction-box">
      <textarea placeholder="e.g. add todo 'go to home!'" v-model="text" />
      <input type="submit" value="SUBMIT" />
    </div>
  </form>
</template>

<style scoped>
.floating-form .chat-box {
  height: 100%;
  width: 100%;
  margin-bottom: 8px;
  list-style-type: none;
  overflow-y: scroll;
}

.floating-form .chat-box li {
  color: black;
}

.floating-form .chat-box li .green {
  color: green;
}

.floating-form .chat-box li .orange {
  color: orange;
}

.floating-form {
  position: fixed;
  right: 10px;
  display: flex;
  flex-direction: column;
  background-color: #f0f0f0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  height: 500px;
  width: 300px;
}

.floating-form textarea {
  resize: none;
  height: 64px;
  width: 100%;
  margin-bottom: 10px;
  border: none;
  border-radius: 6px;
  padding: 6px;
}

.floating-form input[type="submit"] {
  display: block;
  width: 100%;
  font-size: 1.125rem;
  padding: 1rem 1.5rem;
  color: #fff;
  background-color: green;
  border-radius: 0.5rem;
  box-shadow: var(--personal-glow);
  cursor: pointer;
  transition: 0.2s ease-in-out;
}
</style>