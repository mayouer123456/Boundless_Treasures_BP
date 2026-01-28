import re
import os
import subprocess

# Define paths
md_file = "Data_Visualizations_Boundless_Treasures.md"
output_dir = "exported_charts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read markdown content
try:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: {md_file} not found.")
    exit(1)

# Regex to find mermaid blocks
# Matches ```mermaid ... ``` content
pattern = r"```mermaid\n(.*?)```"
matches = re.findall(pattern, content, re.DOTALL)

print(f"Found {len(matches)} mermaid charts.")

for i, code in enumerate(matches):
    code = code.strip()
    
    # Simple heuristic for naming
    chart_type = "chart"
    if "xychart-beta" in code: chart_type = "bar_line"
    elif "pie" in code: chart_type = "pie"
    elif "gantt" in code: chart_type = "gantt"
    elif "mindmap" in code: chart_type = "mindmap"
    
    # Try to extract title for filename if present
    title_match = re.search(r'title\s+"?(.*?)"?$', code, re.MULTILINE)
    safe_title = ""
    if title_match:
        # cleanup title for filename
        raw_title = title_match.group(1)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", raw_title).replace(" ", "_").strip()
        # limit length
        safe_title = safe_title[:20]
    
    filename_base = f"{i+1:02d}_{chart_type}"
    if safe_title:
        filename_base += f"_{safe_title}"
        
    mmd_path = os.path.join(output_dir, f"{filename_base}.mmd")
    png_path = os.path.join(output_dir, f"{filename_base}.png")
    
    # Write .mmd file
    with open(mmd_path, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f"Processing {filename_base}...")
    
    # Run mmdc
    # -p puppeteer config might be needed for some chars, but defaulting first.
    # -i input -o output -b transparent background
    cmd = f'cmd /c "npx -y @mermaid-js/mermaid-cli -i "{mmd_path}" -o "{png_path}" -b transparent"'
    
    try:
        # simple run
        subprocess.run(cmd, check=True, shell=True)
        print(f"SUCCESS: {png_path}")
    except subprocess.CalledProcessError:
        print(f"FAILURE: Could not generate {png_path}. Syntax might be unsupported by CLI.")

print("Batch export processing complete.")
