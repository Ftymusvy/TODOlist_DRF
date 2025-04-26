# پروژه Todo List با Django و API

یک اپلیکیشن ساده وب برای مدیریت کارها (Todo List) که با معماری API-محور توسعه داده شده است. بک‌اند با استفاده از Django پیاده‌سازی شده و APIهای لازم را برای فرانت‌اند فراهم می‌کند.

![تصویر اپلیکیشن Todo List](https://github.com/Ftymusvy/TODOlist_DRF/blob/main/main.png)

![تصویر اپلیکیشن Todo List](https://github.com/Ftymusvy/TODOlist_DRF/blob/main/detail.png)
## قابلیت‌ها

* افزودن کار جدید با عنوان، تاریخ و دسته‌بندی از طریق فراخوانی API.
* نمایش لیست کارهای ثبت‌شده که از API دریافت می‌شوند.
* ارتباط بین فرانت‌اند (HTML/CSS/JS) و بک‌اند (Django) کاملاً مبتنی بر API است.


* `GET /api/todos/`: دریافت لیست کارها
* `POST /api/todos/`: افزودن کار جدید
