# Django First Project

این پروژه اولین پروژه من با **Django** است.  
هدف از این پروژه یادگیری مبانی جنگو و ساخت یک برنامه مدیریت کاربران و سیستم احراز هویت است.

---

## ویژگی‌ها

### مدیریت کاربران (User Management)
- کاربر می‌تواند **نام و فامیل** خود را وارد کند
- امکان **ویرایش اطلاعات کاربران**
- امکان **حذف کاربران**

### سیستم اکانت‌ها (Authentication)
- کاربران می‌توانند **ثبت‌نام (Sign Up)** کنند
- امکان **ورود (Login)** به حساب کاربری
- دسترسی به بخش‌های خصوصی بعد از ورود

---

## نصب و اجرا

 پروژه را کلون کنید:
```bash
git clone https://github.com/mahmoodidevs/django-first-project.git

وارد پوشه پروژه شوید:

cd django-first-project


محیط مجازی بسازید و فعال کنید:

python -m venv venv
# ویندوز
venv\Scripts\activate
# لینوکس / مک
source venv/bin/activate


نصب وابستگی‌ها (اگر requirements.txt اضافه کرده باشی):

pip install -r requirements.txt


اجرای سرور جنگو:

python manage.py runserver


مرورگر را باز کنید و بروید به:

http://127.0.0.1:8000/
