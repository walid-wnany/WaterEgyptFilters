# المصرية للفلاتر — Streamlit Ready

هذه النسخة مخصصة للنشر على Streamlit Community Cloud.

## الإصلاح الأساسي
تم تغيير أسماء ملفات الصفحات إلى أسماء إنجليزية/ASCII لتجنب مشاكل ترميز أسماء الملفات العربية التي قد تؤدي إلى `StreamlitPageNotFoundError` عند استخدام `st.Page`.

## بنية المشروع
- `app.py` هو ملف التشغيل الرئيسي.
- `home.py` الصفحة الرئيسية.
- `pages/` تحتوي الصفحات بأسماء ملفات ASCII.
- `assets/logo.png` اللوجو.
- `.streamlit/config.toml` إعدادات Streamlit.
- `requirements.txt` المتطلبات.

## النشر
ارفع محتويات هذه الحزمة إلى جذر مستودع GitHub، ثم اجعل Main file هو `app.py`.
