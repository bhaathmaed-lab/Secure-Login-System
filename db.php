db.php (PHP + MySQL example):
<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "secure_login";

$conn = mysqli_connect($host, $username, $password, $database);

if (!$conn) {
    die("Database connection failed: " . mysqli_connect_error());
}
?>
But for your Secure Login System (Flask) repository, keep:
database.py ✅
Your final stack is:
Frontend: HTML + CSS
Backend: Python Flask
Database: SQLite
Security: Bcrypt password hashing + sessions