CAM_ACCESS = 1
MIC_ACCESS = 2
FILE_ACCESS = 4
safe_apps = ["python studio", "geometry app", "ebook reader", "physics lab"]
banned_apps = ["arcade game", "store app", "chat app"]
selected_app = input("Enter the app you want to access: ").lower()
print("\n--- Identity Operator Check ---")
user_age = 12
if type(user_age) is int:
    print("The student age is stored as a number.")
if type(user_age) is not str:
    print("The student age is not stored as text.")
print("\n--- Membership Operator Check ---")
if selected_app in safe_apps:
    print(selected_app, "is an approved student app.")
else:
    print(selected_app, "is not an approved student app.")
if selected_app not in banned_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")
print("\n--- App Permission Settings ---")
active_rights = CAM_ACCESS | MIC_ACCESS
print("Permission bits:", bin(active_rights))
if active_rights & CAM_ACCESS:
    print("Camera permission: Enabled")
if active_rights & MIC_ACCESS:
    print("Microphone permission: Enabled")
if active_rights & FILE_ACCESS:
    print("Storage permission: Enabled")
else:
    print("Storage permission: Disabled")
print("\n--- Bit Shift Demonstration ---")
print("Camera bit:", bin(CAM_ACCESS))
print("After left shift:", bin(CAM_ACCESS << 1))
print("Storage bit:", bin(FILE_ACCESS))
print("After right shift:", bin(FILE_ACCESS >> 1))
print("\n--- Final Access Result ---")
if selected_app in safe_apps and selected_app not in banned_apps:
    print("Access granted to", selected_app)
else:
    print("Access denied to", selected_app)
