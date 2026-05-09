import requests
from datetime import datetime
import heapq
API_URL = "http://4.224.186.213/evaluation-service/notifications"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJwcmFiaGF2YXRoaWtvbHVzdTJAZ21haWwuY29tIiwiZXhwIjoxNzc4MzA3Nzc1LCJpYXQiOjE3NzgzMDY4NzUsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI1NzAyNDBiMy0wNjMzLTQ4Y2MtYTcyYy01NWQ1NDI5MzY3YTUiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJrb2x1c3UgcHJhYmhhdmF0aGkiLCJzdWIiOiJlZTExZjJjZC02ZDE0LTQ0N2ItOWNmNi00ZTE0YzQ5OWUxYjYifSwiZW1haWwiOiJwcmFiaGF2YXRoaWtvbHVzdTJAZ21haWwuY29tIiwibmFtZSI6ImtvbHVzdSBwcmFiaGF2YXRoaSIsInJvbGxObyI6IjIzNDgxYTEyYjkiLCJhY2Nlc3NDb2RlIjoiZUpkQ3VDIiwiY2xpZW50SUQiOiJlZTExZjJjZC02ZDE0LTQ0N2ItOWNmNi00ZTE0YzQ5OWUxYjYiLCJjbGllbnRTZWNyZXQiOiJNREVIWWhaZnlBVHZOR2VUIn0.1-a0vwIJxlz9WA09r757fL7A8lCxmcL-RvQrzeaWDMk",
    "Content-Type": "application/json"
}
TOP_N = 10
TYPE_WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}
def fetch_notifications():
    response = requests.get(API_URL, headers=HEADERS)

    print("Status Code:", response.status_code)

    
    if response.status_code == 200:
        data = response.json()
        return data.get("notifications", [])

    
    print("API unavailable. Using sample notifications.")

    return [
        {
            "ID": "1",
            "Type": "Placement",
            "Message": "Google Hiring Drive",
            "Timestamp": "2026-04-25 10:00:00"
        },
        {
            "ID": "2",
            "Type": "Result",
            "Message": "Mid-Sem Results Published",
            "Timestamp": "2026-04-22 17:30:00"
        },
        {
            "ID": "3",
            "Type": "Event",
            "Message": "Hackathon Registration Open",
            "Timestamp": "2026-04-20 09:00:00"
        }
    ]
def calculate_priority(notification):

    weight = TYPE_WEIGHT.get(notification.get("Type"), 0)

    timestamp_str = notification.get(
        "Timestamp", "2000-01-01 00:00:00"
    )

    timestamp = datetime.strptime(
        timestamp_str,
        "%Y-%m-%d %H:%M:%S"
    )

    recency_score = timestamp.timestamp()

    return weight * 1_000_000_000 + recency_score
def get_top_notifications(notifications):

    heap = []

    for n in notifications:

        score = calculate_priority(n)

        if len(heap) < TOP_N:
            heapq.heappush(heap, (score, n))
        else:
            if score > heap[0][0]:
                heapq.heappushpop(heap, (score, n))

    return sorted(heap, reverse=True)
def display_notifications(top_notifications):

    print("\n===== PRIORITY INBOX (TOP 10) =====\n")

    for rank, (_, n) in enumerate(top_notifications, start=1):
        print(
            f"{rank}. [{n['Type']}] {n['Message']} - {n['Timestamp']}"
        )
if __name__ == "__main__":

    print("Fetching notifications...")

    notifications = fetch_notifications()

    print("Total Notifications Received:", len(notifications))

    if not notifications:
        print("No notifications received.")
    else:
        top_notifications = get_top_notifications(notifications)
        display_notifications(top_notifications)