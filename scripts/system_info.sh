#!/bin/bash

echo "=== SYSTEM INFORMATION ==="

echo "Current User:"
whoami

echo ""

echo "Current Date:"
date

echo ""

echo "Current Directory:"
pwd

echo ""

echo "Kernel Information:"
uname -a

echo ""

echo "Disk Usage:"
df -h /
