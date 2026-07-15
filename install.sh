#!/bin/bash
# CyberPanel & OLS Optimizer Installer
# Automatically configures Swap Directory and registers Daily Log Cleaner cron job.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Starting CyberPanel & OLS Optimization Setup ===${NC}"

# 1. Detect OS LiteSpeed Group (nogroup for Debian/Ubuntu, nobody for CentOS/AlmaLinux)
echo -e "${YELLOW}[1/5] Detecting OS group configuration...${NC}"
if grep -q 'nogroup' /etc/group; then
    GROUP="nogroup"
else
    GROUP="nobody"
fi
echo -e "Group detected: ${GREEN}$GROUP${NC}"

# 2. Setup the custom swapping directory for OpenLiteSpeed
echo -e "${YELLOW}[2/5] Setting up persistent swapping directory...${NC}"
mkdir -p /lswstmp/lshttpd/swap
chmod 750 /lswstmp/lshttpd
chmod 700 /lswstmp/lshttpd/swap
chown -R nobody:$GROUP /lswstmp/lshttpd
echo -e "${GREEN}Swapping directory configured at /lswstmp/lshttpd/swap${NC}"

# 3. Update OLS configurations to use the new Swapping Directory
echo -e "${YELLOW}[3/5] Updating OpenLiteSpeed configuration files...${NC}"
CONF_UPDATED=0

# Update httpd_config.conf (Newer OLS versions)
if [ -f "/usr/local/lsws/conf/httpd_config.conf" ]; then
    if grep -q "/tmp/lshttpd/swap" "/usr/local/lsws/conf/httpd_config.conf"; then
        sed -i 's|/tmp/lshttpd/swap|/lswstmp/lshttpd/swap|g' /usr/local/lsws/conf/httpd_config.conf
        echo -e "-> Updated ${GREEN}/usr/local/lsws/conf/httpd_config.conf${NC}"
        CONF_UPDATED=1
    fi
fi

# Update httpd_config.xml (Older OLS versions)
if [ -f "/usr/local/lsws/conf/httpd_config.xml" ]; then
    if grep -q "/tmp/lshttpd/swap" "/usr/local/lsws/conf/httpd_config.xml"; then
        sed -i 's|/tmp/lshttpd/swap|/lswstmp/lshttpd/swap|g' /usr/local/lsws/conf/httpd_config.xml
        echo -e "-> Updated ${GREEN}/usr/local/lsws/conf/httpd_config.xml${NC}"
        CONF_UPDATED=1
    fi
fi

if [ $CONF_UPDATED -eq 1 ]; then
    echo -e "${YELLOW}Reloading OpenLiteSpeed to apply configuration changes...${NC}"
    systemctl reload lsws >/dev/null 2>&1 || /usr/local/lsws/bin/lswsctrl restart >/dev/null 2>&1 || true
    echo -e "${GREEN}OpenLiteSpeed reloaded.${NC}"
else
    echo -e "Swapping Directory configuration was already updated or config files not found."
fi

# 4. Create the Log Cleaner script
echo -e "${YELLOW}[4/5] Creating log cleaner script at /root/logscleaner.sh...${NC}"
cat << 'EOF' > /root/logscleaner.sh
#!/bin/bash
# Optimized CyberPanel Logs & Cache Cleaner

# Truncate (empty) OLS log files instead of deleting to avoid broken file descriptors
if [ -d "/usr/local/lsws/logs" ]; then
    find /usr/local/lsws/logs/ -type f -name "*.log" -exec truncate -s 0 {} +
fi

# Clear OpenLiteSpeed cache files (LSCache)
if [ -d "/usr/local/lsws/cachedata" ]; then
    rm -rf /usr/local/lsws/cachedata/*
fi

# Truncate CyberPanel main debug logs
if [ -f "/home/cyberpanel/error-logs.txt" ]; then
    truncate -s 0 /home/cyberpanel/error-logs.txt
fi

# Remove temporary switch and error files
rm -f /home/cyberpanel/switchLSWSStatus
rm -f /home/cyberpanel/stderr.log

# vacuum systemd journal logs to max 500M
if command -v journalctl >/dev/null 2>&1; then
    journalctl --vacuum-size=500M >/dev/null 2>&1
fi

# Gracefully reload OLS to free up deleted handles
systemctl reload lsws >/dev/null 2>&1 || true

echo "=== Log Cleaner Execution Completed ==="
echo "System Disk usage status:"
df -h /

echo ""
echo "=== Disk Waste Scan (Top 20 Backup Files & Trash in /home) ==="
# Find large back up files in home folder
find /home -maxdepth 3 -type f \( -name "*.sql" -o -name "*.gz" -o -name "*.tar.gz" \) -exec ls -lh {} + 2>/dev/null | awk '{print $5, $9}' | head -n 20 || true

# Find trash folders (File Manager trash)
find /home -maxdepth 3 -type d -name ".trash" -exec du -sh {} + 2>/dev/null || true

# Find staging sites
find /home -maxdepth 3 -type d -name "staging.*" -exec du -sh {} + 2>/dev/null || true
EOF

chmod +x /root/logscleaner.sh
echo -e "${GREEN}Log cleaner script created and set to executable.${NC}"

# 5. Create Daily Cron Job
echo -e "${YELLOW}[5/5] Creating daily cron job at /etc/cron.d/cyberpanel_logcleaner...${NC}"
cat << 'EOF' > /etc/cron.d/cyberpanel_logcleaner
# Daily log cleaner for CyberPanel - Runs at 3:00 AM
0 3 * * * root /bin/bash /root/logscleaner.sh >/dev/null 2>&1
EOF
chmod 644 /etc/cron.d/cyberpanel_logcleaner
echo -e "${GREEN}Daily cron job registered successfully at 3:00 AM.${NC}"

# Running the cleaner immediately for the first time
echo -e "${GREEN}=== Running Log Cleaner for the first time... ===${NC}"
/bin/bash /root/logscleaner.sh || true

echo -e "${GREEN}=== All optimizations applied successfully! ===${NC}"
