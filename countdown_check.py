import time

# Calculate simple mock time left for a task cooldown
def check_cooldown(last_executed_time, cooldown_period=86400):
    current_time = time.time()
    time_passed = current_time - last_executed_time
    
    if time_passed >= cooldown_period:
        return "Ready to execute!"
    else:
        remaining = cooldown_period - time_passed
        return f"Cooldown active. {int(remaining // 3600)} hours remaining."

# Simulated timestamp of a task done 10 hours ago
mock_last_run = time.time() - (10 * 3600)
print(f"Task Status: {check_cooldown(mock_last_run)}")
