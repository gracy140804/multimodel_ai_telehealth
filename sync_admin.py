import sqlite3
import bcrypt

salt = bcrypt.gensalt()
hashed_pw = bcrypt.hashpw("admin123".encode('utf-8'), salt).decode('utf-8')

for db_path in [r"e:\final\backend\telehealth.db", r"e:\final\telehealth.db"]:
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        # Check if admin exists
        cur.execute("SELECT id FROM users WHERE email='admin@healthai.com'")
        row = cur.fetchone()
        if row:
            cur.execute("UPDATE users SET password_hash=? WHERE email='admin@healthai.com'", (hashed_pw,))
            print(f"Updated in {db_path}")
        else:
            cur.execute("INSERT INTO users (name, email, password_hash, role) VALUES ('System Admin', 'admin@healthai.com', ?, 'ADMIN')", (hashed_pw,))
            print(f"Inserted into {db_path}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error acting on {db_path}: {e}")
