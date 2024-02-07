import json

def create_config():
    print("Please enter your configuration settings. Press enter to accept default values.")
    
    # Provide a suggested default for the bulb IP and set default values for other settings
    bulb_ip = input("Bulb IP Address [suggested: 192.168.1.1]: ") or "192.168.1.1"
    start_temp = input("Start Temperature (default 2000): ") or 2000
    end_temp = input("End Temperature (default 6500): ") or 6500
    duration = input("Duration in seconds (default 1800 for 30 minutes): ") or 1800
    steps = input("Number of steps (default 300): ") or 300

    # Create a dictionary with the configuration
    config = {
        "bulb_ip": bulb_ip,
        "start_temp": int(start_temp),
        "end_temp": int(end_temp),
        "duration": int(duration),
        "steps": int(steps)
    }

    # Write the configuration to a json file
    with open("src/config.json", "w") as f:
        json.dump(config, f, indent=4)

    print("Configuration saved to src/config.json")

if __name__ == "__main__":
    create_config()
