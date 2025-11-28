from datetime import datetime
import webbrowser
import os
import json
import time
import random
import sys

# ------------------------------
# AI CORE (ЭМУЛЯЦИЯ ИНТЕЛЛЕКТА)
# ------------------------------

def ai_analyze(data):
    time.sleep(2)

    score = random.randint(80, 95)

    analysis = f"""
AI-ОЦЕНКА ПРОЕКТА:
Уровень автоматизации: ВЫСОКИЙ
Потенциал оптимизации: 40–60%

Риски внедрения:
- Низкое качество входных данных
- Интеграция с legacy-системами
- Регуляторные ограничения

Рекомендуемые этапы внедрения:
1. Автоматизация скоринга
2. Интеграция с внешними источниками данных
3. Внедрение антифрода
4. Обучение ML-модели дефолтов

Бизнес-эффект:
- Снижение операционных затрат до 35%
- Ускорение обработки заявок в 2–3 раза
- Рост конверсии на 12–18%

Приоритет внедрения: КРИТИЧЕСКИЙ
"""

    return score, analysis


# ------------------------------
# ЭМУЛЯЦИЯ BACKEND API
# ------------------------------

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

    print("BACKEND RESPONSE:", result)
    return result


# ------------------------------
# СБОР ДАННЫХ
# ------------------------------

def collect_data_manual():
    print("AI-Business Analyst (Console MVP)")
    print("-----------------------------------")

    data = {}
    data["goal"] = input("1. Какова основная бизнес-цель задачи? ")
    data["problem"] = input("2. Какую проблему вы решаете? ")
    data["users"] = input("3. Кто основные пользователи? ")
    data["process"] = input("4. Опишите текущий процесс (AS-IS): ")
    data["scope"] = input("5. Что входит в scope? ")
    data["rules"] = input("6. Есть ли бизнес-правила? ")
    data["kpi"] = input("7. Какие KPI важны? ")

    return normalize_data(data)


def collect_data_demo():
    print("🚀 DEMO MODE ACTIVATED\n")

    demo_data = {
        "goal": "Сократить время обработки кредитных заявок на 40%",
        "problem": "Ручная проверка, высокая нагрузка, долгие сроки",
        "users": "Клиенты банка, кредитные менеджеры, служба безопасности",
        "process": "Клиент подаёт заявку, менеджер проверяет, скоринг, решение",
        "scope": "Онлайн-заявки, скоринг, проверки, уведомления",
        "rules": "Скоринг > 650 — автоодобрение, лимит до 3 млн тг",
        "kpi": "Время обработки, доля авто-решений, NPS"
    }

    time.sleep(1)
    print("✅ DEMO данные загружены автоматически\n")
    return normalize_data(demo_data)


def normalize_data(data):
    for key, value in data.items():
        if not value.strip():
            data[key] = "Не указано"
    return data


# ------------------------------
# СОХРАНЕНИЕ JSON-ЛОГА
# ------------------------------

def save_json(data):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    filename = f"logs/input_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return filename


# ------------------------------
# ГЕНЕРАЦИЯ HTML ОТЧЁТА
# ------------------------------

def generate_html(data, score, ai_analysis):
    html_content = f"""
<html>
<head>
<meta charset="utf-8">
<title>AI Business Requirements</title>
<style>
body {{
    font-family: Arial;
    margin: 40px;
}}
h1 {{
    text-align: center;
}}
h2 {{
    background: #f0f0f0;
    padding: 8px;
}}
.table {{
    width: 100%;
    border-collapse: collapse;
}}
.table td, .table th {{
    border: 1px solid #000;
    padding: 8px;
}}
.score {{
    font-size: 28px;
    font-weight: bold;
    color: green;
}}
pre {{
    background: #f9f9f9;
    padding: 15px;
}}
</style>
</head>

<body>

<h1>AI BUSINESS REQUIREMENTS</h1>

<h2>AI-Оценка проекта</h2>
<p class="score">{score} / 100</p>

<h2>Цель</h2><p>{data['goal']}</p>
<h2>Описание проблемы</h2><p>{data['problem']}</p>
<h2>Пользователи</h2><p>{data['users']}</p>
<h2>Текущий процесс (AS-IS)</h2><p>{data['process']}</p>
<h2>Scope</h2><p>{data['scope']}</p>
<h2>Бизнес-правила</h2><p>{data['rules']}</p>
<h2>KPI</h2><p>{data['kpi']}</p>

<h2>Use Case</h2>
<ol>
<li>Клиент подает заявку</li>
<li>AI выполняет проверку данных</li>
<li>Модуль скоринга рассчитывает риск</li>
<li>Формируется автоматическое решение</li>
<li>Результат отправляется клиенту</li>
</ol>

<h2>User Stories</h2>
<ul>
<li>Как клиент, я хочу быстро получить решение</li>
<li>Как менеджер, я хочу видеть статусы</li>
<li>Как руководитель, я хочу видеть аналитику</li>
</ul>

<h2>Лидирующие индикаторы</h2>
<table class="table">
<tr><th>Метрика</th><th>Описание</th></tr>
<tr><td>Заявки в час</td><td>Количество входящих заявок</td></tr>
<tr><td>Среднее время обработки</td><td>Время от заявки до решения</td></tr>
<tr><td>Доля авто-решений</td><td>% без участия менеджера</td></tr>
<tr><td>Процент ошибок</td><td>% некорректных заявок</td></tr>
</table>

<h2>AI-Анализ</h2>
<pre>{ai_analysis}</pre>

</body>
</html>
"""

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/business_requirements_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filename


# ------------------------------
# MAIN
# ------------------------------

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        data = collect_data_demo()
    else:
        data = collect_data_manual()

    print("\n⏳ AI анализирует проект...")
    score, ai_analysis = ai_analyze(data)

    backend_result = send_to_backend(data)

    json_file = save_json(data)
    html_file = generate_html(data, score, ai_analysis)

    webbrowser.open(os.path.abspath(html_file))

    print("\n--- MOCK CONFLUENCE API ---")
    print("POST /rest/api/content")
    print("STATUS: 200 OK")
    print("✅ Документ успешно создан")

    print(f"\n✅ Входные данные сохранены: {json_file}")
    print(f"✅ Отчет сформирован: {html_file}")
    print("➡ Откройте HTML → Ctrl + P → Сохранить как PDF")


if __name__ == "__main__":
    main()
