#!/usr/bin/env python3

# Memory Forensics with Volatility
# This is a guide for analyzing memory dumps

print("""
Memory Forensics Challenge

You have a memory dump from a running system.
Use Volatility to analyze it.

Common Volatility commands:
- volatility pslist             # List processes
- volatility psscan             # Scan for processes
- volatility dumpfiles          # Extract files from memory
- volatility vadinfo            # Show memory regions
- volatility netscan            # Network connections

The flag might be in:
- Process memory
- Network connections
- Running executables
- Strings in memory
""")
