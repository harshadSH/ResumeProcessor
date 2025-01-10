# ResumeProcessor Project

This project provides a Django-based REST API and a web interface for uploading resumes (PDF or Word documents) and extracting the candidate's first name, email ID, and mobile number. The extracted information is saved into a PostgreSQL database.

## Prerequisites

Ensure you have the following installed on your system:

- Python (>=3.10)
- PostgreSQL
- pip
- Django (>=4.0)
- Django REST Framework

## Setting up the Project Locally

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd ResumeProcessor
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL Database**

   - Create a new PostgreSQL database.
   - Update the `DATABASES` settings in `ResumeProcessor/settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/api/extract_resume/`.

## Testing the API Endpoint

1. **API Endpoint**

   The API endpoint is available at:

   ```
   POST /api/extract_resume/
   ```

2. **Uploading a Resume**

   Use tools like Postman or `curl` to upload a resume file. Example using `curl`:

   ```bash
   curl -X POST -F "resume=@/path/to/your/resume.pdf" http://127.0.0.1:8000/api/upload-resume/
   ```

   Expected Response:

   ```json
   {
       "data": {
           "first_name": "John",
           "email": "john.doe@example.com",
           "mobile_number": "123-456-7890"
       }
   }
   ```

## Testing the Web Interface

1. **Access the Web Page**

   Navigate to `http://127.0.0.1:8000/api/upload-resume/` in your browser.

2. **Upload a Resume**

   - Select a PDF or Word file.
   - Click the "Upload" button.
   - The extracted data will be saved in the database.

## Cleaning Temporary Files

Temporary files are created during the extraction process. To clean up these files manually:

```bash
find /tmp -name 'resume_processor_*' -delete
```

## Additional Notes

- Ensure the uploaded file is either a PDF or Word document.
- Error messages will indicate if the file type is unsupported or if no file is uploaded.


## Contributing

Feel free to raise issues or submit pull requests to improve the project.

## Contact

For queries or support, reach out to harshadhole04@gmail.com.

