# Campus Notification Priority Inbox

A Python-based Priority Inbox system that fetches campus notifications from an API and displays the Top 10 most important unread notifications using a Min Heap (Priority Queue).

---

##  Problem Statement

Students receive many notifications daily and may miss important updates.

This project solves the problem by:
- Fetching notifications from an API
- Assigning priority based on notification type and recency
- Displaying the Top 10 highest-priority notifications

---

##  Features

- Fetch notifications from REST API
- Priority-based sorting
- Latest notifications ranked higher
- Efficient Top-N management using Min Heap
- Scalable for real-time notification streams

---

## 🛠 Technologies Used

- Python 3
- Requests Library
- Heapq (Priority Queue)

---

## Project Structure

```bash
campus-notification-priority-inbox/
│
├── priority_inbox.py
├── requirements.txt
├── Notification_System_Design.md
├── README.md
└── output_screenshot.png
