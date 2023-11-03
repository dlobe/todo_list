document.getElementById('todo-form').addEventListener('submit', async function(event) {
  event.preventDefault();

  const title = document.getElementById('title-input').value;
  const description = document.getElementById('description-input').value;
  const completed = document.getElementById('completed-checkbox').checked;

  const response = await fetch('/todos/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title, description, completed }),
  });

  const data = await response.json();

  if (response.ok) {
      alert('Todo added successfully!');
      // Optionally reset the form or do something else upon success
      document.getElementById('todo-form').reset();
      // Here you can also insert the new to-do item into the ul#todo-list if you want to update the list without reloading
  } else {
      alert('Failed to add todo: ' + (data.detail || 'Unknown Error'));
  }
});
