import sys

path = '/Users/masteraj/InteractiveLecture/graphs/kinematics_stopping_v1.html'
with open(path) as f:
    lines = f.readlines()

# Find the <select ... onchange="setTheme..."> line
insert_idx = None
for i, line in enumerate(lines):
    if 'onchange="setTheme(this.value)"' in line:
        insert_idx = i + 1
        break

if insert_idx is None:
    print("ERROR: could not find setTheme select")
    sys.exit(1)

# Remove old option lines (currently from insert_idx onwards until </select>)
# First find the </select> line
end_idx = None
for i in range(insert_idx, len(lines)):
    if '</select>' in lines[i]:
        end_idx = i
        break

if end_idx is None:
    print("ERROR: could not find </select>")
    sys.exit(1)

# Replace old options with new ones
new_options = [
    '      <option value="dark">\U0001f319 Classic Dark</option>\n',
    '      <option value="neon">\U0001f303 Cyberpunk Neon</option>\n',
    '      <option value="vintage">\U0001f4dc Vintage Dark</option>\n',
    '      <option value="cosmic">\U0001f30c Cosmic Void</option>\n',
    '      <option value="onedark">\U0001f535 One Dark</option>\n',
    '      <option value="light">\u2600\ufe0f Classic White</option>\n',
    '      <option value="warm">\U0001f305 Warm Taupe</option>\n',
    '      <option value="sage">\U0001f33f Soft Sage</option>\n',
    '      <option value="mist">\U0001f32b\ufe0f Mist Blue</option>\n',
    '      <option value="clay">\U0001f3fa Warm Clay</option>\n',
]

# Replace lines from insert_idx to end_idx with new options + the </select> line
new_lines = lines[:insert_idx] + new_options + lines[end_idx:]
with open(path, 'w') as f:
    f.writelines(new_lines)

print(f"Done. Replaced lines {insert_idx+1}-{end_idx} with new options.")