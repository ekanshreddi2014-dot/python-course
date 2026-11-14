records = {
    "id1": {"name": "Sara", "class": "V", "subject": ["english", "math", "science"]},
    "id2": {"name": "David", "class": "V", "subject": ["english", "math", "science"]},
    "id3": {"name": "Sara", "class": "V", "subject": ["english", "math", "science"]},
    "id4": {"name": "Surya", "class": "V", "subject": ["english", "coding", "math"]},
}
print("Original Student Records:")
print(records)
print("Details of id1:")
print(records.get("id1", "Not Found"))
print("Details of id5:")
print(records.get("id5", "Not Found"))
records["id5"] = {"name": "Anaya", "class": "V", "subject": ["english", "art", "science"]}
print("After adding id5:")
print(records)
records["id2"]["subject"] = ["english", "math", "coding"]
print("After updating id2 subject:")
print(records["id2"])
unique_records = {}
seen = []
for sid, info in records.items():
    key = (info["name"], info["class"], tuple(info["subject"]))
    if key not in seen:
        seen.append(key)
        unique_records[sid] = info
records = unique_records
print("After removing duplicate records:")
print(records)
deleted_record = records.pop("id4", "Student not found")
print("Removed student:")
print(deleted_record)
print("Total student records left:", len(records))
print("===== FINAL STUDENT SUBJECT RECORDS =====")
for sid, info in records.items():
    print(sid, ":", info)
print("==========================================")
