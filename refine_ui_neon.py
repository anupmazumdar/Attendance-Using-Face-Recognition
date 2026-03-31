import os
import re

files_to_update = [
    "attendance.py",
    "automaticAttedance.py",
    "show_attendance.py",
    "takemanually.py"
]

replacements = [
    # Dark themes to deeper black / dark gray
    (r'bg=["\']#1E1E1E["\']', 'bg="#000000"'),
    (r'bg=["\']#2B2B2B["\']', 'bg="#050505"'),
    (r'background=["\']#1E1E1E["\']', 'background="#000000"'),
    
    # Foregrounds to Neon Cyan / Green
    (r'fg=["\']#E0E0E0["\']', 'fg="#00FFFF"'),   # Cyan
    (r'fg=["\']#4CAF50["\']', 'fg="#39FF14"'),   # Neon Green
    
    # Button colors
    (r'bg=["\']#C2185B["\']', 'bg="#1A3636"'),    # Dark cyan/green back
    (r'bg=["\']#388E3C["\']', 'bg="#112222"'),
    (r'bg=["\']#D32F2F["\']', 'bg="#330000"'),    # Warn dark red back
    (r'bg=["\']#1976D2["\']', 'bg="#0B192C"'),
    (r'activebackground=["\']#D32F2F["\']', 'activebackground="#FF0000"'),
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for p, r in replacements:
            content = re.sub(p, r, content)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"{filename} not found.")

print("UI Refinement done.")
