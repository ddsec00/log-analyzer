failed_count = 0

with open("logs/sample.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            failed_count += 1

print(f"Failed login attempts: {failed_count}")
