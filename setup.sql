CREATE USER 'aauth'@'localhost' IDENTIFIED BY 'PASSWORD';
CREATE DATABASE aauth CHARACTER SET utf8mb4;
GRANT ALL PRIVILEGES ON alliance_auth . * TO 'aauth'@'localhost';