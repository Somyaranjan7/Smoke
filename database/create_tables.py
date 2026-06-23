from database.db import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS user(

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) UNIQUE NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL

)

""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS scan_history(

    id INT AUTO_INCREMENT PRIMARY KEY,

    target VARCHAR(100),

    scan_time VARCHAR(50),

    txt_report_path VARCHAR(255),

    pdf_report_path VARCHAR(255),

    user_id INT,

    FOREIGN KEY(user_id)
    REFERENCES user(id)

)

""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS port_result(

    id INT AUTO_INCREMENT PRIMARY KEY,

    port INT,

    state VARCHAR(20),

    service VARCHAR(100),

    version VARCHAR(100),

    risk VARCHAR(20),

    recommendation TEXT,

    scan_id INT,

    FOREIGN KEY(scan_id)
    REFERENCES scan_history(id)

)

""")

print("Tables created successfully")