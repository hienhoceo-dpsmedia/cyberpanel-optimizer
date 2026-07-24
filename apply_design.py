import os
import sys
import re
import urllib.request

print("==========================================")
print("  DPS.MEDIA CyberPanel Design & Fix Tool  ")
print("==========================================")

VIEWS_PATH = '/usr/local/CyberCP/baseTemplate/views.py'

# 1. Patch views.py to fix 500 error on /base/design
if os.path.exists(VIEWS_PATH):
    print("[1/3] Checking and patching views.py...")
    with open(VIEWS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "headers={'User-Agent': 'CyberPanel'}" not in content:
        # Create backup
        os.system(f"cp {VIEWS_PATH} {VIEWS_PATH}.bak")
        print("  -> Backup created: views.py.bak")
        
        # Replace un-handled GitHub API call with safe try-except call
        old_pattern = r'sha_url = "https://api\.github\.com/repos/usmannasir/CyberPanel-Themes/commits".*?finalData\[\'tree\'\]\.append\(fres\.json\(\)\[\'tree\'\]\[i\]\[\'path\'\]\)'
        new_code = """    finalData['tree'] = []
    try:
        sha_url = "https://api.github.com/repos/usmannasir/CyberPanel-Themes/commits"
        sha_res = requests.get(sha_url, headers={'User-Agent': 'CyberPanel'}, timeout=5)
        if sha_res.status_code == 200 and isinstance(sha_res.json(), list) and len(sha_res.json()) > 0:
            sha = sha_res.json()[0]['sha']
            l = "https://api.github.com/repos/usmannasir/CyberPanel-Themes/git/trees/%s" % sha
            fres = requests.get(l, headers={'User-Agent': 'CyberPanel'}, timeout=5)
            if fres.status_code == 200 and 'tree' in fres.json():
                for item in fres.json()['tree']:
                    if item.get('type') == "tree":
                        finalData['tree'].append(item.get('path'))
    except Exception as e:
        pass"""
        
        if re.search(old_pattern, content, flags=re.DOTALL):
            content = re.sub(old_pattern, new_code, content, flags=re.DOTALL)
            with open(VIEWS_PATH, 'w', encoding='utf-8') as f:
                f.write(content)
            print("  -> Patched views.py successfully!")
        else:
            print("  -> views.py pattern not matched or already modified.")
    else:
        print("  -> views.py is already patched.")

# 2. Update Database with Custom CSS
print("[2/3] Updating Custom CSS in CyberPanel Database...")

CSS_URL = "https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/dps_design.css"

try:
    req = urllib.request.Request(CSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        css_content = response.read().decode('utf-8')
except Exception as e:
    print(f"  -> Error fetching CSS from GitHub: {e}")
    sys.exit(1)

# Django context setup
sys.path.append('/usr/local/CyberCP')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CyberCP.settings')

import django
django.setup()

from baseTemplate.models import CyberPanelCosmetic

try:
    cosmetic, created = CyberPanelCosmetic.objects.get_or_create(pk=1)
    cosmetic.MainDashboardCSS = css_content
    cosmetic.save()
    print("  -> Custom CSS applied to Database successfully!")
except Exception as e:
    print(f"  -> Error updating database: {e}")
    sys.exit(1)

# 3. Restart CyberPanel Service
print("[3/3] Restarting CyberPanel Service (lscpd)...")
os.system("systemctl restart lscpd")
print("==========================================")
print("  SUCCESS! CyberPanel design applied.    ")
print("==========================================")
