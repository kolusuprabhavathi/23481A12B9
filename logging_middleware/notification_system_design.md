# Notification System Design

## 1. Introduction

The Campus Notification System is designed to manage and prioritize notifications received from different campus services such as placements, examination results, and events.

The main goal of the system is to ensure that important notifications are displayed first so that students do not miss critical updates.

---

## 2. Problem Statement

Traditional notification systems display messages only in chronological order.
As the number of notifications increases, important announcements may be overlooked.

This system addresses the problem by assigning priorities and displaying only the most relevant notifications.

---

## 3. System Architecture

### Components

**Notification API**

* Provides notification data in JSON format.

**Priority Inbox Module**

* Fetches notifications from API.
* Calculates priority scores.
* Maintains Top N notifications.

**Display Interface**

* Shows prioritized notifications through command-line output.

---

## 4. System Workflow

1. Application requests notifications from the API.
2. Notifications are received in JSON format.
3. Priority score is calculated for each notification.
4. Min Heap stores only Top 10 notifications.
5. Sorted notifications are displayed to the user.

---

## 5. Data Model

Each notification contains:

* **Type** – Category of notification
* **Message** – Notification content
* **Timestamp** – Time of creation

Example:

```
{
  "Type": "Placement",
  "Message": "Company Hiring Drive",
  "Timestamp": "2026-04-25 10:00:00"
}
```

---

## 6. Priority Calculation Strategy

### Notification Type Priority

* Placement → High Priority
* Result → Medium Priority
* Event → Normal Priority

### Recency Factor

Recent notifications receive higher priority.

### Final Priority Score

Priority Score = Type Weight + Timestamp Score

---

## 7. Algorithm Used

The system uses a **Min Heap (heapq)** data structure.

Advantages:

* Efficient Top-N selection
* Time complexity of O(log N)
* Avoids sorting large datasets
* Suitable for real-time notification streams

---

## 8. Error Handling

The application handles:

* Invalid authorization token
* API service failure
* Empty notification responses

If API access fails, sample notifications are used for demonstration.

---

## 9. Scalability Considerations

The system supports scalability by:

* Processing notifications incrementally
* Maintaining constant memory usage
* Filtering important data efficiently

---

## 10. Future Enhancements

* Web-based dashboard
* Database integration
* Personalized notification ranking
* Real-time push notifications
* Mobile application support

---

## 11. Conclusion

The Priority Inbox system improves notification management by presenting only important updates to users.
Using efficient algorithms and a simple architecture, the system provides a scalable solution for campus notification management.

---
