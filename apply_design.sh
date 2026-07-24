#!/bin/bash
# CyberPanel DPS.MEDIA Auto Fix & Custom Design Installer
set -e

if [ "$EUID" -ne 0 ]; then
  echo "Error: Please run as root!"
  exit 1
fi

echo "================================================="
echo " Fetching & Executing CyberPanel Design Installer"
echo "================================================="

/usr/local/CyberCP/bin/python <(curl -sSL https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/apply_design.py)
