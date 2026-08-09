camera = 1
microphone = 2
storage = 4
location = 8
approved_apps = [coding apps,maths app,reading app,science app]
ristricted_apps = [gaming apps,social media apps,shopping apps]
name = input("name : ")
requested_app = input("app : ")
lower = requested_app.lower()
if lower in approved_apps:
    print("the app is in approved list")
else:
    print("the app is not in approved list")
if lower in not restricted_apps:
    print("the app is in approved list")
else:
    print("the app is not in approved list")
if type(name) is str:
    print("the name is string")
if type(requested_app):
    print("the requested app is not stored in int")
print("app persmision settings")