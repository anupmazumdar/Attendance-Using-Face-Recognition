import os
import re

files_to_update = [
    "attendance.py",
    "automaticAttedance.py",
    "show_attendance.py",
    "takemanually.py"
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix the syntax error, insertbackground cannot be inside the font tuple!
        content = re.sub(r',\s*insertbackground=["\']#00FFFF["\']', '', content)
        
        # Now safely add insertbackground to tk.Entry root kwargs
        def replace_entry(match):
            inner = match.group(1)
            # if we didn't add it globally yet
            if 'insertbackground' not in inner:
                return f'tk.Entry({inner}, insertbackground="#00FFFF")'
            return match.group(0)
            
        content = re.sub(r'tk\.Entry\((.*?)\)', replace_entry, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

