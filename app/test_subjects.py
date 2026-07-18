from documents.subject_manager import SubjectManager


manager = SubjectManager()

print("利用可能な科目:")
for subject in manager.get_subjects():
    print(f"- {subject}")

manager.select_subject("assembly")

print()
print("現在の科目:")
print(manager.current_subject)

print()
print("インデックス:")
for index_file in manager.get_index_files():
    print(index_file)
