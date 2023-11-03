// script.js

// Function to add a to-do item to the list
const addTodo = (todo) => {
  const listItem = document.createElement('li');
  listItem.textContent = todo;
  list.appendChild(listItem);
};

// Handle form submission
document.getElementById('todo-form').onsubmit = async (e) => {
  e.preventDefault();
  const input = document.getElementById('todo-input');
  const todo = input.value;
  const list = document.getElementById('todo-list');

  // Send a POST request to the FastAPI backend
  const response = await fetch('http://44.204.45.74:5000/todos', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title: todo })
  });

  if (response.ok) {
    // Clear the input field
    input.value = '';
    // Add the to-do item to the list
    addTodo(todo);
  } else {
    // Handle errors (e.g., display an error message)
    console.error('Failed to add to-do item');
  }
};
