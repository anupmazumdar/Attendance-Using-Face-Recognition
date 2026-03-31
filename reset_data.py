import os
import shutil

# Reset Student Details CSV
csv_path = r'StudentDetails/studentdetails.csv'
if os.path.exists(csv_path):
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write("Enrollment,Name\n")
    print("Reset master Student Details CSV.")

# Clear Training Images
image_path = r'TrainingImage'
if os.path.exists(image_path):
    for filename in os.listdir(image_path):
        filepath = os.path.join(image_path, filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print(f'Failed to delete {filepath}. Reason: {e}')
    print("Cleared Training Images.")

# Clear the trainer model
trainer_path = r'TrainingImageLabel/Trainner.yml'
if os.path.exists(trainer_path):
    os.remove(trainer_path)
    print("Removed trained recognition model.")

# Clear Generated Attendance files
attendance_path = r'Attendance'
if os.path.exists(attendance_path):
    for filename in os.listdir(attendance_path):
        filepath = os.path.join(attendance_path, filename)
        try:
            if os.path.isfile(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            pass
    print("Cleared tracked Attendance folders.")

print("All Database / Data files reset successfully!")
