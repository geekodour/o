#!/usr/bin/env python3
import subprocess
import csv
import time
import json
import sys
from datetime import datetime

def get_ping_latency(host="8.8.8.8", count=1):
    """Measure ping latency to a host"""
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), host],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            # Parse ping output to extract latency
            lines = result.stdout.split('\n')
            for line in lines:
                if "time=" in line:
                    # Extract time value (e.g., "time=23.4 ms")
                    time_part = line.split("time=")[1].split()[0]
                    return float(time_part)
        return None
    except Exception as e:
        print(f"Ping error: {e}")
        return None

def get_location():
    """Get GPS coordinates using termux-location"""
    try:
        result = subprocess.run(
            ["termux-location", "-p", "gps"],
            capture_output=True,
            text=True,
            timeout=15
        )
        
        if result.returncode == 0:
            location_data = json.loads(result.stdout)
            return location_data.get("latitude"), location_data.get("longitude")
        return None, None
    except Exception as e:
        print(f"Location error: {e}")
        return None, None

def log_to_csv(timestamp, latitude, longitude, latency_ms, filename="ping_data.csv"):
    """Append data to CSV file"""
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(['timestamp', 'latitude', 'longitude', 'latency_ms'])
        
        writer.writerow([timestamp, latitude, longitude, latency_ms])

def main():
    print("Starting ping monitor...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            timestamp = datetime.now().isoformat()
            
            # Get ping latency
            latency = get_ping_latency()
            
            # Get GPS coordinates
            lat, lon = get_location()
            
            # Log to CSV
            log_to_csv(timestamp, lat, lon, latency)
            
            # Print status
            status = f"{timestamp} | Lat: {lat} | Lon: {lon} | Ping: {latency}ms"
            print(status)
            
            # Wait 5 seconds
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nStopping ping monitor...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

