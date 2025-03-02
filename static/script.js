function getBooks() {
     fetch('/books')
         .then(response => response.json())
         .then(data => {
             document.getElementById('getResponse').textContent = JSON.stringify(data, null, 2);
         })
         .catch(error => console.error('Error:', error));
 }
 
 document.getElementById('postForm').addEventListener('submit', function(event) {
     event.preventDefault();
     const bookData = {
         ID: document.getElementById('id').value,
         TITLE: document.getElementById('title').value,
         AUTHOR: document.getElementById('author').value,
         PUBLICATION_DATE: document.getElementById('pub_date').value
     };
 
     fetch('/books', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify(bookData)
     })
     .then(response => response.json())
     .then(data => {
         document.getElementById('postResponse').textContent = JSON.stringify(data, null, 2);
     })
     .catch(error => console.error('Error:', error));
 });
 