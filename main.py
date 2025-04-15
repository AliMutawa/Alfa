import os
import eel

# تحديد مجلد الملفات
eel.init("www")

# تشغيل Microsoft Edge كتطبيق بواجهة نظيفة
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# تشغيل eel بدون فتح متصفح تلقائيًا
eel.start('index.html', mode=None, host='localhost', block=True)
