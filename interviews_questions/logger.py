import re
from datetime import datetime

log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ([A-Z]+) - (Entry #\d+): (.*)')
# Regex breakdown:
# (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) -> Grabs the ISO timestamp
# \s-\s([A-Z]+)\s-\s                         -> Grabs the Log Level (INFO, CRITICAL)
# (Entry\s#\d+):\s                           -> Grabs the Entry ID
# (.*)                                       -> Grabs the remaining message

parsed_logs = []

with open("simulation.log",'r') as f:
    for line in f.readlines():
        match = log_pattern.match(line)
        if match:
            ts_str, level, entry_id, message = match.groups()
            
            # Convert timestamp string to a Python datetime object for easy sorting/filtering
            timestamp = datetime.strptime(ts_str, '%Y-%m-%d %H:%M:%S,%f')
            
            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "id": entry_id,
                "message": message
            })

print(parsed_logs)