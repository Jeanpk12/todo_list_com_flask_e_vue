<template>
  <div id="app">
      <h1>TODO List</h1>
    <TodoList />
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';

export default {
  name: 'App',
  components: {
    TodoList
  }
};
</script>
<style>

h1{
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  color: #007bff;
  text-transform: uppercase;
}

</style>