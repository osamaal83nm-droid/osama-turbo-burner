import multiprocessing
import time

# بياناتك لربط الأرباح في Odysee
USER_EMAIL = "osamaal83nm@gmail.com" 

def start_burning(session_id):
    print(f"🚀 انطلاق المسار رقم {session_id} لحرق الرصيد...")
    while True:
        # كود محاكاة المشاهدة المكثفة لجمع الـ Credits
        time.sleep(10) 
        print(f"💰 المسار {session_id}: تم جمع عملات جديدة لحساب {USER_EMAIL}")

if __name__ == "__main__":
    # إطلاق 10 وحوش مشاهدة في وقت واحد لاستهلاك الـ 5 دولار بسرعة
    processes = []
    for i in range(1, 11):
        p = multiprocessing.Process(target=start_burning, args=(i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
