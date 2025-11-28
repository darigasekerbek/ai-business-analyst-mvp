import time
import random

def send_to_backend(data):
    print("\n📡 Отправка данных в AI Backend...")
    time.sleep(1.5)

    print("POST /api/ai/analyze")
    print("STATUS: 200 OK")

    result = {
        "risk_score": random.randint(10, 35),
        "approval_probability": random.randint(70, 95),
        "fraud_flag": random.choice([True, False])
    }

    return result
