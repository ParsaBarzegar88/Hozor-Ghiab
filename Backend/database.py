from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# تنظیمات اتصال به دیتابیس
username = "AyandehComputer"
password = "Parsa@3287"
database_name = "AyandehConputer_Hozor-Ghiab_db"

# رمز عبور را encode می‌کنیم چون حاوی @ است
encoded_password = quote_plus(password)
DATABASE_URL = f"postgresql://{username}:{encoded_password}@localhost:5432/{database_name}"

# ایجاد موتور اتصال
engine = create_engine(DATABASE_URL)

# ساخت session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# پایه برای مدل‌ها
Base = declarative_base()