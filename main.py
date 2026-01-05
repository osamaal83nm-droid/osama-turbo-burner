import os
import requests
from pyairtable import Api

# إعدادات لقمة العيش
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
BASE_ID = "appUh9VyWQVqYjyBs"
TABLE_NAME = "Freelancer Projects"

def start_mission():
    print("🧹 جاري تنظيف الجدول وبحث لقمة العيش...")
    try:
        table = Api(AIRTABLE_API_KEY).table(BASE_ID, TABLE_NAME)
        # هنا يبدأ العمل الصادق
        print("✅ تم بنجاح يا مَلِك!")
    except Exception as e:
        print(f"❌ عائق بسيط: {e}")

if __name__ == "__main__":
    start_mission()
