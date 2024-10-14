<template>
    <div class="todo-container">
      <div class="input-group">
        <input v-model="newTodo" placeholder="Add a new task" @keyup.enter="addTodo" />
        <button @click="addTodo"><i class="ri-add-line"></i></button>
      </div>
      <ul class="todo-list">
        <li v-for="todo in todos" :key="todo.id" class="todo-item">
          <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)" />
          <input type="text" v-model="todo.title" @blur="updateTodo(todo)" class="todo-title" />
          <button @click="deleteTodo(todo.id)" class="delete-button"><i class="ri-delete-bin-line"></i></button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        todos: [],
        newTodo: ''
      };
    },
    methods: {
      fetchTodos() {
        axios.get('http://localhost:5000/api/todos')
          .then(response => {
            this.todos = response.data;
          });
      },
      addTodo() {
        if (this.newTodo.trim()) {
          axios.post('http://localhost:5000/api/todos', { title: this.newTodo })
            .then(response => {
              this.todos.push(response.data);
              this.newTodo = '';
            });
        }
      },
      updateTodo(todo) {
        axios.put(`http://localhost:5000/api/todos/${todo.id}`, todo)
          .then(response => {
            console.log('Todo updated:', response.data);
          });
      },
      deleteTodo(todoId) {
        axios.delete(`http://localhost:5000/api/todos/${todoId}`)
          .then(() => {
            this.todos = this.todos.filter(todo => todo.id !== todoId);
          });
      }
    },
    mounted() {
      this.fetchTodos();
    }
  };
  </script>
  
  <style>
  .todo-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px;
  }
  
  .input-group {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .input-group input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ced4da;
    border-radius: 4px;
  }
  
  .input-group button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .input-group button:hover {
    background-color: #085ec5;
  }
  
  .todo-list {
    list-style: none;
    padding: 0;
  }
  
  .todo-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .todo-item:last-child {
    border-bottom: none;
  }
  
  .todo-title {
    flex: 1;
    margin: 0 10px;
    padding: 5px;
    font-size: 16px;
    border: 1px solid #ced4da;
    border-radius: 4px;
  }
  
  .delete-button {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 8px 10px;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .delete-button:hover {
    background-color: #b7192c;
  }
  </style>
  