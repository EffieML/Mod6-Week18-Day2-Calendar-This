CREATE TABLE appointments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(200) NOT NULL,
  start_datetime TIMESTAMP NOT NULL,
  end_datetime TIMESTAMP NOT NULL,
  description TEXT NOT NULL,
  private BOOLEAN NOT NULL
);

INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
VALUES
('My appointment', '2022-11-11 14:00:00', '2022-11-11 15:00:00',
 'An appointment for me', false);


FLASK_ENV=development
SECRET_KEY=SADFSGIOKFDJBGOIDFJM
DB_FILE=dev.db
