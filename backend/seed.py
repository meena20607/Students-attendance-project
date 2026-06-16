from app import create_app
from app.extensions import db
from app.models.admin import Admin

app = create_app()

with app.app_context():
    db.create_all()

    # Create admin only if not exists
    if not Admin.query.filter_by(username="admin").first():
        admin = Admin(username="admin", email="admin@college.com")
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("Admin seeded: admin@college.com / admin123")
    else:
        print("Admin already exists.")