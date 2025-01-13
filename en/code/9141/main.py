from textfile import load
heartbeat_data = load(1000)
previous = -1.0
for value in heartbeat_data:
  if value > 0:
    if previous < 0:
      print("heartbeat detected")
  previous = value
