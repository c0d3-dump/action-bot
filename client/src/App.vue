<script setup>
import Dashboard from "./components/Dashboard.vue";
</script>

<template>
  <main>
    <Dashboard></Dashboard>
  </main>
</template>

<style>
:root {
  --primary: #3ca7bf;
  --business: #b347d4;
  --personal: var(--primary);
  --light: black;
  --grey: #888;
  --dark: #313154;
  --danger: #ff5b57;

  --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "montserrat", sans-serif;
}

body {
  background: var(--light);
  color: white;
}
</style>