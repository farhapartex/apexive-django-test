# Apexive Django Project Documentation

This document provides instructions on how to set up and use the Django application for managing pilot logs. It covers the creation of a virtual environment, installation of required packages, running the Django server, and details on how to use the provided APIs.

## Setup Instructions

### 1. Creating a Virtual Environment

To create a virtual environment, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to your project directory using the `cd` command.
3. Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

1. Activate the virtual environment:
```bash
source venv/bin/activate
```
2. Installing Packages from requirements.txt
```bash
pip install -r requirements.txt
```
3. Running the Server: To run the Django server, execute the following command:
```bash
python manage.py runserver
```
This command starts the development server on http://127.0.0.1:8000/. You can access the application through this URL in your web browser.

## API Documentation
The application provides three main APIs for managing pilot logs:

1. Create and List Pilot Logs

* Endpoint: `/api/v1/pilotlogs/`
* Method: GET for listing, POST for creating
* Data Parameters for POST:
  * `file`: a valid json file
* Success Response:
  * Code: 200 OK for GET, 201 Created for POST

2. Pilot Log Details

* Endpoint: `/api/v1/pilotlogs/:id`
* Method: GET
* URL Parameters:
  * `id`: a valid pilot log ID
  * Success Response:
  * Code: 200 OK

3. Download Pilot Log as CSV
* Endpoint: `/api/v1/pilotlogs/:id/download`
* Method: GET
* URL Parameters:
  * `id`: a valid pilot log ID
  * Success Response:
  * Code: 200 OK