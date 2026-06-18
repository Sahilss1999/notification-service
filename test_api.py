import requests



BASE_URL = "http://127.0.0.1:8000"

# 1. Register
print("---- REGISTER ----")
register_data = {"username": "testuser1", "password": "test1234"}
res = requests.post(f"{BASE_URL}/auth/register", json=register_data)
print(res.status_code, res.json())

# 2. Login
print("\n---- LOGIN ----")
login_data = {"username": "testuser1", "password": "test1234"}
res = requests.post(f"{BASE_URL}/auth/login", json=login_data)
print(res.status_code, res.json())
token = res.json().get("access_token")

headers = {"Authorization": f"Bearer {token}"}

# 3. Create Notification
print("\n---- CREATE NOTIFICATION ----")
notif_data = {"title": "Order Shipped", "message": "Your order is on the way", "channel": "SMS"}
res = requests.post(f"{BASE_URL}/notifications/", json=notif_data, headers=headers)
print(res.status_code, res.json())
notif_id = res.json().get("id")

# 4. Get All Notifications
print("\n---- GET ALL NOTIFICATIONS ----")
res = requests.get(f"{BASE_URL}/notifications/", headers=headers)
print(res.status_code, res.json())

# 5. Get by ID
print(f"\n---- GET NOTIFICATION BY ID ({notif_id}) ----")
res = requests.get(f"{BASE_URL}/notifications/{notif_id}", headers=headers)
print(res.status_code, res.json())

# 6. Update Status
print("\n---- UPDATE STATUS ----")
update_data = {"status": "Sent"}
res = requests.put(f"{BASE_URL}/notifications/{notif_id}", json=update_data, headers=headers)
print(res.status_code, res.json())

# 7. Delete
print("\n---- DELETE ----")
res = requests.delete(f"{BASE_URL}/notifications/{notif_id}", headers=headers)
print(res.status_code, res.json())