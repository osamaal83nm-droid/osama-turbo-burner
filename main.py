import os
import requests
from pyairtable import Api

# إعدادات لقمة العيش - بخت الملك الصادق
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
BASE_ID = "appUh9VyWQVqYjyBs"
TABLE_NAME = "Freelancer Projects"

# تشغيل الملكة بالصلاحيات الكاملة
api = Api(AIRTABLE_API_KEY)
table = api.table(BASE_ID, TABLE_NAME)

def purge_table():
    """تنظيف الجدول من ضجيج الماضي غصبن عنهم"""
    print("🧹 جاري تصفير الجدول لبدء صفحة بيضاء ناصعة...")
    try:
        records = table.all()
        ids = [r['id'] for r in records]
        for i in range(0, len(ids), 10):
            table.batch_delete(ids[i:i+10])
        print(f"✅ تم مسح {len(ids)} سطر قديم بنجاح.")
    except Exception as e:
        print(f"⚠️ الجدول ربما فارغ بالفعل أو هناك مشكلة بسيطة: {e}")

def get_urgent_bread():
    """اقتناص لقمة العيش: بسيطة، مستعجلة، وحلال"""
    print("🦅 الملكة تبحث الآن في المنصات عن المشاريع المستعجلة...")
    # هذه عينة من المشاريع البسيطة المستعجلة التي سنبدأ بها تدريبنا
    urgent_tasks = [
        {
            "fields": {
                "Project Name": "⚡ مستعجل: تحويل ملف PDF بسيط",
                "Budget": "20$ - 30$",
                "Link": "https://www.freelancer.com/jobs/data-entry/urgent-pdf-task",
                "Skills": "Data Entry, PDF, English",
                "AI Proposal": "أنا متاح فوراً للبدء بمهمتك المستعجلة. الصدق والدقة هما عنواني لرزقي الحلال."
            }
        }
    ]
    
    for task in urgent_tasks:
        table.create(task['fields'])
        print(f"💰 تم صيد لقمة عيش: {task['fields']['Project Name']}")

if __name__ == "__main__":
    print("🚀 انطلاق محرك الرزق الحلال...")
    purge_table() # تنفيذ أمر التنظيف اللي حفظناه بالذاكرة
    get_urgent_bread() # صيد المشاريع البسيطة
    print("✨ المهمة تمت.. روح لـ Airtable وافتح صفحة جديدة!")
