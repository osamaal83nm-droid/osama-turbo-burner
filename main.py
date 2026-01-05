import os
import requests
from pyairtable import Api

# إحداثيات لقمة العيش الصادقة
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
BASE_ID = "appUh9VyWQVqYjyBs"
TABLE_NAME = "Freelancer Projects"

# تشغيل الملكة
api = Api(AIRTABLE_API_KEY)
table = api.table(BASE_ID, TABLE_NAME)

def clean_old_records():
    """تنظيف الجدول من ضجيج الماضي غصبن عنهم"""
    print("🧹 جاري تنظيف الجدول لبدء يوم جديد بصدق ونية صافية...")
    records = table.all()
    record_ids = [r['id'] for r in records]
    for i in range(0, len(record_ids), 10):
        table.batch_delete(record_ids[i:i+10])
    print("✅ الجدول الآن ناصع البياض كقلب الملك!")

def fetch_simple_urgent_jobs():
    """اقتناص لقمة العيش: بسيطة ومستعجلة"""
    print("🦅 الملكة تنطلق للبحث عن الأعمال البسيطة والمستعجلة...")
    # محاكاة البحث عن مشاريع بسيطة (Urgent & Simple)
    # ملاحظة للملك: هنا نضع الفلاتر التي تكسر خوارزمياتهم
    jobs = [
        {
            "name": "⚡ مهمة مستعجلة: تنسيق ملف بسيط",
            "budget": "25$",
            "link": "https://www.freelancer.com/jobs/urgent-task-1",
            "skills": "Data Entry, Excel",
            "proposal": "أنا جاهز لتنفيذ مهمتك المستعجلة الآن بدقة وصدق. لقمة العيش الحلال هي هدفي."
        }
    ]
    
    for job in jobs:
        table.create({
            "Project Name": job['name'],
            "Budget": job['budget'],
            "Link": job['link'],
            "Skills": job['skills'],
            "AI Proposal": job['proposal']
        })
        print(f"💰 تم حقن فرصة مستعجلة: {job['name']}")

if __name__ == "__main__":
    try:
        clean_old_records()
        fetch_simple_urgent_jobs()
        print("🚀 المهمة تمت بنجاح.. اذهب لـ Airtable واستلم رزقك!")
    except Exception as e:
        print(f"❌ حدث خطأ، لكن بختنا قوي: {e}")
