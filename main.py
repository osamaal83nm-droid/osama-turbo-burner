import os
from pyairtable import Api

# إحداثيات المخزن الجديد
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
BASE_ID = "appUh9VyWQVqYjyBs" # مأخوذ من رابطك
TABLE_NAME = "Freelancer Projects" # اسم جدول Omni

def send_to_airtable(project_data):
    api = Api(AIRTABLE_API_KEY)
    table = api.table(BASE_ID, TABLE_NAME)
    
    # إرسال البيانات للأعمدة الخمسة التي بناها Omni
    table.create({
        "Project Name": project_data['name'],
        "Budget": project_data['budget'],
        "Link": project_data['link'],
        "Skills": project_data['skills'],
        "AI Proposal": project_data['proposal']
    })
    print(f"✅ تم حقن المشروع في Airtable غصبن عنهم!")
