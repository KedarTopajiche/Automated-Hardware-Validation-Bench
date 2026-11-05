import serial
import time
import csv

PORT = '/dev/cu.usbserial-0001'
BAUD = 115200
OUTPUT_FILE = 'telemetry_validation_log.csv'

print(f"Connecting to {PORT} at {BAUD} baud...")
try:
    ser = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(1)

    with open(OUTPUT_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['SAMPLE_ID', 'TIMESTAMP_MS', 'DISTANCE_MM', 'TOUCH_EVENTS', 'RESULT'])
        print("Capturing 60 test cycles...")
        count = 0
        while count < 60:
            raw = ser.readline().decode('utf-8', errors='ignore').strip()
            parts = [p.strip() for p in raw.split(',')]
            if len(parts) == 5 and parts[0].isdigit():
                count += 1
                writer.writerow(parts)
                print(f"[{count}/60] {raw}")

    ser.close()
    print(f"\n[SUCCESS] Captured 60 samples into {OUTPUT_FILE}")
except Exception as e:
    print(f"Error: {e}")
