import subprocess, os

os.chdir('/home/arbot/obsidian-vault')
subprocess.run(['git', 'add', '03-Daily/2026-06-13.md', '00-Index/Projects.md'], check=True)
result = subprocess.run(['git', 'commit', '-m', 'Daily note 2026-06-13'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
print("Return code:", result.returncode)
