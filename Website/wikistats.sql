create database wikistats;

use wikistats;
CREATE USER 'wikiview'@'localhost' IDENTIFIED BY '%jswP^YkqV#rne';
GRANT ALL PRIVILEGES ON wikistats.* to 'wikiview'@'localhost';
CREATE TABLE user( user_id INT NOT NULL AUTO_INCREMENT, username VARCHAR(64) NOT NULL, password VARCHAR(64) NOT NULL, primary key(user_id));
INSERT INTO user VALUES('', 'demo', 'demopass');
FLUSH PRIVILEGES;

