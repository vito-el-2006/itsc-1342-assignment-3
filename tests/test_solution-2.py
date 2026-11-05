# [Your Full Name] - Assignment 3 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import format_alert

# Test 1: Standard critical alert formatting
res1 = format_alert("CRITICAL", "10.0.0.15", "Port scan detected")
assert res1 == "[CRITICAL] - 10.0.0.15: Port scan detected", "Failed Test 1: Check your brackets, dashes, and colons"

# Test 2: Warning alert formatting
res2 = format_alert("WARNING", "192.168.1.100", "Failed login attempt")
assert res2 == "[WARNING] - 192.168.1.100: Failed login attempt", "Failed Test 2"

# Test 3: Info alert formatting (Note: Check the arguments passed here!)
res3 = format_alert("INFO", "127.0.0.1", "Service restarted successfully")
assert res3 == "[INFO] - 127.0.0.1: Service restarted successfully", "Failed Test 3"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 3")
