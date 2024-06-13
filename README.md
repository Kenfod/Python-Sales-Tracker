<h1>Jipange Sales Tracker</h1>

Jipange Sales Tracker is a web application built with Flask and a mobile application designed with Flutter for front end to help users track their sales data. It allows users to register, log in, manage sales records, and view cumulative sales with targets. This project demonstrates a complete stack development process with user authentication, CRUD operations, and real-time data display.

<h2>Table of Contents</h2>

<li>Features</li>
<li>Technologies Used</li>
<li>Installation</li>
<li>Configuration</li>
<li>Usage</li>
<li>API Endpoints</li>
<li>Project Structure</li>
<li>Contributing</li>
<li>License</li>
<li>Contact</li>

<h2>Features</h2>

<li>User registration and authentication</li>
<li>Track sales with customer, product, and quantity details</li>
<li>View cumulative sales and monitor monthly targets</li>
<li>Responsive web interface using Flask</li>
<li>Mobile application interface using Flutter</li>
<li>API endpoints for integration with other applications</li>

<h2>Technologies Used</h2>
<li><b>Backend:</b> Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-CORS</li>
<li><b>Frontend:</b> Dart, Flutter, HTTP package</li>
<li><b>Database:</b> SQLite</li><br>

<h2>Installation</h2>
<h3>Backend (Flask)</h3>

1.Clone the repository:

```dart
git clone https:https://github.com/Kenfod/Python-Sales-Tracker.git
```
2.Create and activate a virtual environment:

```dart
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3.Install the required dependencies:

```dart
pip install -r requirements.txt
```

4.Set up the database:

```dart
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

5.Run the Flask application:

```dart
python app.py
```
The server will start on ' http://127.0.0.1:5000 '

<h3>Frontend (Flutter)</h3>

1.Install Flutter:
Follow the instructions on the Flutter website to install Flutter on your system.

2.Navigate to the Flutter project directory:

```dart
cd flutter_app
```

3.Install the required dependencies:

```dart
flutter pub get
```

4.Run the Flutter application:

```dart
flutter run
```

<h2>Configuration</h2>

<h3>Flask Configuration</h3>
<b>Database URI:</b> Update SQLALCHEMY_DATABASE_URI in app.py to point to your database.

<b>Secret Key:</b> Update SECRET_KEY in app.py with a strong secret key.<br>

<h3>Flutter Configuration</h3>
<b>API Base URL:</b> Update the API base URL in the Flutter app's source code to match the Flask server's URL.

<h2>Usage</h2>

<h3>Web Interface</h3>

1.<b>Register:</b> Create a new user account by navigating to <b>'/register'</b>.

2.<b>Login:</b> Log in to the application at <b>'/login'</b>.

3.<b>Dashboard:</b> View the sales dashboard, add new sales, and monitor targets.<br><br>

<h3>Mobile Interface</h3>

1.<b>Home Screen:</b> Displays the current user, cumulative sales, and a list of all sales.

2.<b>Add Sale:</b> Add new sales entries with customer and product details.

3.<b>Edit Sale:</b> Modify existing sales entries.

4.<b>Delete Sale:</b> Remove sales entries.

<h2>API Endpoints</h2>
<h3>User Management</h3>
<li><b>Register: ' POST /api/register '</b></li><br>

```dart
{
    "username": "user",
    "password": "password"
}
```

<li><b>Login: ' POST /api/login '</b></li><br>

```dart
{
    "username": "user",
    "password": "password"
}
```
<li><b>Get Username: ' GET /api/username'</b></li><br>

<h3>Sales Management</h3>

<li><b>Get Sales:</b> ' GET /api/sales '</li><br>
<li><b>Add Sale:</b> ' POST /api/sales '</li><br>
<li><b>Edit Sale:</b> ' PUT /api/sales/<id> '</li><br>
<li><b>Delete Sales:</b> ' DELETE /api/sales<id> '</li><br>

<h2>Project Structure</h2>

```dart
jipange-sales-tracker/
├── app.py                  # Flask application
├── models.py               # Database models
├── forms.py                # WTForms for registration and login
├── templates/              # HTML templates for Flask
│   ├── edit.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── static/                 # Static files (CSS, JS, images)
├── migrations/             # Database migrations
├── flutter_app/            # Flutter application
│   ├── lib/
│   │   ├── main.dart       # Main entry point for Flutter app
│   │   ├── screens/        # Flutter screens
│   │   └── widgets/        # Flutter widgets
│   └── pubspec.yaml        # Flutter dependencies
└── requirements.txt        # Python dependencies

```

<h2>Contributing</h2>
  
We welcome contributions to the Jipange Sales Tracker project!<br> Here are some ways you can contribute:

<li>Report bugs or issues.</li>
<li>Suggest new features.</li>
<li>Improve documentation.</li><br>

To contribute, follow these steps:

1.Fork the repository.

2.Create a new branch <b>(' git checkout -b feature/your-feature ')</b>.

3.Commit your changes <b>(' git commit -m "Add new feature" ')</b>.

4.Push to the branch <b>(' git push origin feature/your-feature ')</b>.

5.Create a new Pull Request.

<h2>License</h2>
This project is licensed under the MIT License. See the LICENSE file for more details.

<h2>Contact</h2>
For questions or feedback, please contact <b>kelvinnyagudi@yahoo.com</b>.
