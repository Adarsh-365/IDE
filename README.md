# Python IDE with Django  

An online Python IDE built with Django, allowing users to run Python files directly in the browser. The platform also includes (or will include) a curated set of programming problems for practice.  

## Features  
- **Run Python Code Online:** Execute Python code using `subprocess` for real-time results.  
- **Future Enhancements:** A growing set of coding problems to challenge and improve programming skills.  
- **Efficient Deployment:** Hosted on [Vercel](https://vercel.com), ensuring scalability and ease of deployment.  
- **Static File Handling:** Integrated with [WhiteNoise](http://whitenoise.evans.io/) for efficient serving of static files.  

## Tech Stack  
- **Backend Framework:** Django  
- **Deployment:** Vercel  
- **Static File Management:** WhiteNoise  
- **Python Execution:** `subprocess` module  

## Installation  

### Prerequisites  
- Python 3.8+  
- Django  
- Pip  

### Steps to Set Up Locally  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/your-repo.git  
   cd your-repo 
   ```
2.Install dependencies:
  ```bash
  pip install -r requirements.txt  
  ```

3.Configure the environment:

Set the DJANGO_SETTINGS_MODULE environment variable to point to the settings file (default: IDE.settings).


4. **Run migrations:**
```bash
python manage.py migrate
```


5. **Start the development server:**
```bash
python manage.py runserver
```
Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).





How It Works
Python Code Execution:
The subprocess module is used to safely execute Python code entered by the user. It captures the output or errors generated during execution and displays them on the frontend.

Static Files:
WhiteNoise is used to serve static assets (e.g., CSS, JS, images) in production without requiring a separate web server.

Future Plans
Add a comprehensive set of coding problems with varying difficulty levels.
Integrate user authentication for saving code and tracking progress.
Enhance the editor with syntax highlighting, autocomplete, and debugging tools.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or suggestions, feel free to reach out to `[https://github.com/Adarsh-365]`.

Feel free to modify the placeholders like `[https://github.com/your-username/your-repo.git](https://github.com/Adarsh-365/IDE)` or contact information to suit your project. Let me know if you'd like any additional features or sections!
