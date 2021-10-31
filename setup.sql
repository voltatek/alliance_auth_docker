CREATE USER 'aauth'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PASSWORD';
CREATE DATABASE aauth CHARACTER SET utf8mb4;
GRANT ALL PRIVILEGES ON aauth . * TO 'aauth'@'localhost';