@echo off
title RMBSend v0.0.1
echo RMBSend v0.0.1 is running!

python main.py

:wait_for_file

rd /s /q __pycache__
