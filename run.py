#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OJANTHA STORE - Secure Launcher for fb_reg
"""

import fb_reg

if __name__ == "__main__":
    try:
        # সাইথন কম্পাইলড মডিউল থেকে মেইন ফাংশন কল করা
        if hasattr(fb_reg, "main"):
            fb_reg.main()
        else:
            print("[!] Main function not found in compiled module.")
    except Exception as e:
        print(f"[!] Error: {e}")

