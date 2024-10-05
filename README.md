
## API Data Display Webpage
This project is a simple Django application that demonstrates how to fetch data from a database and display it on a webpage using HTML and CSS. The project consists of a viewset for handling API requests, as well as a traditional Django view for rendering the data in a styled HTML table.

### Features
Django REST Framework (DRF) ViewSet: Provides an API to interact with the APIModel, which includes fetching, creating, updating, and deleting records via RESTful endpoints.
HTML Data Rendering: Displays the database entries in a responsive, modern HTML table format with hover effects and a clean layout.
Responsive Design: The page is fully responsive, adapting to various screen sizes. The table collapses into a more readable format on mobile devices.
Styling: The design includes:
Modern font and color schemes.
Hover effects on table rows for better user interaction.
Shadow and rounded corner effects for a card-like layout.
Responsive breakpoints for mobile-friendly design.
### Technologies Used
Django: A high-level Python web framework for backend functionality.
Django REST Framework (DRF): Handles the API endpoints for the APIModel data.
HTML5 and CSS3: Frontend structure and styling for rendering the data table.
### How It Works
APIViewSet: A Django REST Framework ModelViewSet is implemented to manage CRUD operations on the APIModel.
HTML Rendering: A separate Django view fetches the data and renders it on an HTML page (api_data.html). The table lists the data with columns for ID, Title, and Description.
Responsive Table: The table design adapts to different screen sizes. On larger screens, it displays as a full-width table, while on smaller screens, it collapses into individual rows for better readability.

![Screenshot 2024-10-05 121542](https://github.com/user-attachments/assets/0028ef8e-0ff1-44e6-8b45-dcb3d6f92575)
![Screenshot 2024-10-05 121440](https://github.com/user-attachments/assets/16cd1ed7-1d20-4b69-a538-a67c27c1754a)
