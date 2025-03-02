# Flask Books API

This project is a simple Flask-based API that allows users to manage a collection of books via GET and POST requests. The frontend consists of an HTML page with a form for adding books and a button for fetching book data.

### Images of Website
![Fetch Books](https://imgur.com/mXMdfKm.png)

![Post Books](https://imgur.com/WFLAnDE.png)
## Features
- **GET Request**: Fetch all books stored in the API.
- **POST Request**: Add a new book by providing its ID, title, author, and publication date.
- **DELETE Request**: Remove a book using its ID.
- **PUT Request**: Update book details using its ID.
- **Modern UI**: A clean and responsive user interface for interacting with the API.

## Technologies Used
- Flask (Python backend)
- HTML, CSS, JavaScript (Frontend)
- Fetch API (for making API requests)
- Flask-CORS (for handling cross-origin requests)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-books-api.git
   cd flask-books-api
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage
1. Open `http://127.0.0.1:5000` in your browser.
2. Click the **Fetch Books** button to retrieve the list of books.
3. Fill in the form and click **Add Book** to add a new book.
4. The responses will be displayed in the respective sections.
5. Use DELETE and PUT requests to modify book entries.

## API Endpoints
### `GET /`
Fetches all books stored in the API.

### `POST /`
Adds a new book to the API.
#### Request Body (JSON):
```json
{
    "ID": "002",
    "TITLE": "Harry Potter",
    "AUTHOR": "J.K. Rowling",
    "PUBLICATION_DATE": "1997-06-26"
}
```
#### Response:
```json
{
    "message": "Book added successfully"
}
```

### `DELETE /`
Removes a book from the API.
#### Request Body (JSON):
```json
{
    "ID": "002"
}
```
#### Response:
```json
{
    "message": "Book with ID 002 deleted successfully"
}
```

### `PUT /`
Updates an existing book in the API.
#### Request Body (JSON):
```json
{
    "ID": "002",
    "TITLE": "Harry Potter and the Sorcerer's Stone",
    "AUTHOR": "J.K. Rowling",
    "PUBLICATION_DATE": "1997-06-26"
}
```
#### Response:
```json
{
    "message": "Book with ID 002 updated successfully"
}
```

## Future Enhancements
- Improve error handling and validation.
- Implement a database for persistent storage.
- Enhance UI for better user experience.
- Implement authentication for secure API access.

## License
This project is open-source and available under the MIT License.

