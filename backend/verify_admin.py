import bcrypt
from app.db.database import SessionLocal
from app.models.models import User

def check_admin():
    db = SessionLocal()
    user = db.query(User).filter(User.email == "admin@healthai.com").first()
    if not user:
        print("Admin user not found!")
        return

    print("Found user:", user.email, "Role:", user.role)

    # Check password
    salt = bcrypt.gensalt()
    # verify
    if bcrypt.checkpw("admin123".encode('utf-8'), user.password_hash.encode('utf-8')):
        print("Password matches!")
    else:
        print("Password DOES NOT MATCH. Updating password to admin123...")
        user.password_hash = bcrypt.hashpw("admin123".encode('utf-8'), salt).decode('utf-8')
        db.commit()
        print("Password updated successfully to admin123")

if __name__ == "__main__":
    check_admin()
