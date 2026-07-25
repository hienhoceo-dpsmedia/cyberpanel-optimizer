import os
import sys
import re
import time
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

CSS_URL = f"https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/dps_design.css?v={int(time.time())}"

try:
    req = urllib.request.Request(CSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        css_content = response.read().decode('utf-8')
except Exception as e:
    css_content = ""

# Strip any non-ASCII characters completely to avoid MySQL 1366 encoding error
css_content = re.sub(r'[^\x00-\x7F]+', '', css_content)

if not css_content.strip():
    # Embedded pure ASCII CSS fallback
    css_content = """
.notification-shown.ai-scanner-shown .htaccess-feature-banner { display: none !important; }
.notification-shown .ai-scanner-banner { display: none !important; }
.notification-banner.show { display: none !important; }
.sidebar-logo .logo-icon img { opacity: 0 !important; }
.sidebar-logo .logo-icon {
    background-image: url('https://dps.media/wp-content/uploads/2023/08/dpsmedia.svg') !important;
    background-size: contain !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
}
.sidebar-logo .logo-text { display: none !important; flex-direction: column; flex: 1; }
.sidebar-logo .logo-icon { width: 100% !important; }
#header { display: none !important; }
.notification-shown.ai-scanner-shown.htaccess-shown #main-content { padding-top: 30px !important; }
.remote-table td { padding: 1rem !important; }
img.center-block.text-center.my-20 { display: none !important; }
.login-wrapper::before {
    content: "";
    display: block;
    width: 120px;
    height: 120px;
    margin: 20px auto;
    background-image: url("https://dps.media/wp-content/uploads/2023/08/dpsmedia.svg");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
}
h1.text-transform-upr.text-center.panel-body.text-bold { font-size: 0 !important; position: relative; }
h1.text-transform-upr.text-center.panel-body.text-bold::after {
    content: "DPS.MEDIA";
    font-size: 38px;
    font-weight: 600;
    color: #33CCCC;
    letter-spacing: 2px;
    display: block;
    text-align: center;
}
a.login-changelogs { display: none !important; }
.col-login-left * { display: none !important; }
.col-login-left {
    background-image: url("https://dps.media/wp-content/uploads/2025/11/chrome_6AkkKmSNBI.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center center;
}
.overview-section { display: none !important; }
.domain-hero, .quick-actions { display: none !important; }
.notification-shown.ai-scanner-shown #main-content { padding-top: 40px !important; }

@media screen and (min-width: 1920px) {
    body, #main-content { font-size: 16.5px !important; }
    .form-control, input, select, label, button, td, th { font-size: 16.5px !important; }
    .form-control { height: 46px !important; padding: 10px 16px !important; }
}

@media screen and (min-width: 2200px) {
    body, #main-content { font-size: 19.5px !important; }
    .form-control, input, select, label, button, td, th, .nav-tabs > li > a { font-size: 19px !important; }
    .form-control { height: 52px !important; padding: 12px 20px !important; font-size: 18.5px !important; }
    .btn { padding: 12px 28px !important; font-size: 18.5px !important; }
    #sidebar { width: 300px !important; }
    #sidebar a { font-size: 18px !important; }
}

.website-screenshot, img.website-screenshot, .screenshot-section img { display: none !important; }
.website-details { padding: 16px 20px !important; background: #ffffff !important; border-radius: 10px !important; }
.info-table { border: 1px solid #e1e8e3 !important; border-radius: 8px !important; }
.info-cell { padding: 10px 16px !important; border-right: 1px solid #e1e8e3 !important; }
.info-label { font-size: 11px !important; font-weight: 700 !important; color: #6b7783 !important; text-transform: uppercase !important; }
.info-value { font-size: 13.5px !important; font-weight: 600 !important; color: #202938 !important; }

#navBar { background: #ffffff !important; border-bottom: 1px solid #e1e8e3 !important; }
.header-logo .logo-icon { background: #e8f6ed !important; color: #151577 !important; border-radius: 8px !important; }
.header-logo .brand { color: #151577 !important; font-weight: 700 !important; }
.header-logo .domain { background: #e8f6ed !important; color: #32b561 !important; font-weight: 600 !important; }
#navBar .nav-link { color: #202938 !important; font-weight: 600 !important; }
#navBar .nav-link i { color: #151577 !important; }
#navBar .nav-link:hover { background: #e8f6ed !important; color: #151577 !important; }
#treeView .content-box { background: #ffffff !important; border: 1px solid #e1e8e3 !important; border-radius: 10px !important; }
#currentPath { border: 1px solid #e1e8e3 !important; background: #f7f9fb !important; font-family: monospace !important; color: #151577 !important; }
.col-sm-9 .nav { background: #ffffff !important; border: 1px solid #e1e8e3 !important; border-radius: 10px !important; }
.col-sm-9 .nav-item a { color: #202938 !important; font-weight: 600 !important; }
.col-sm-9 .nav-item a i { color: #151577 !important; }
.col-sm-9 .nav-item a:hover { background: #e8f6ed !important; color: #151577 !important; }
#tableHead, .col-sm-9 table thead, .col-sm-9 table thead th { background: #151577 !important; color: #ffffff !important; border: none !important; }
.col-sm-9 table tbody tr:hover { background: #e8f6ed !important; }
.col-sm-9 table td i.fa-folder { color: #151577 !important; }
.col-sm-9 table td i.fa-file { color: #32b561 !important; }
"""


# Django context setup
sys.path.append('/usr/local/CyberCP')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CyberCP.settings')

import django
django.setup()

from baseTemplate.models import CyberPanelCosmetic

try:
    cosmetic, created = CyberPanelCosmetic.objects.get_or_create(pk=1)
    cosmetic.MainDashboardCSS = css_content.strip()
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
