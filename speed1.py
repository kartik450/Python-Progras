import speedtest
import time

# Initialize the Speedtest object
test = speedtest.Speedtest()

# Record the start time
start_time = time.time()

# Continue measuring for 10 seconds
while time.time() - start_time < 10:
    # Perform the download and upload speed tests
    download_speed = test.download()
    upload_speed = test.upload()

    # Convert to megabytes
    download_speed_MB = download_speed / 8_388_608  # 8,388,608 = 1024 * 1024 * 8
    upload_speed_MB = upload_speed / 8_388_608

    # Display download speed
    if download_speed_MB < 1:
        print(f"Download speed: {download_speed_MB * 1024:.2f} kb/s")
    else:
        print(f"Download speed: {download_speed_MB:.2f} MB/s")

    # Display upload speed
    if upload_speed_MB < 1:
        print(f"Upload speed: {upload_speed_MB * 1024:.2f} kb/s")
    else:
        print(f"Upload speed: {upload_speed_MB:.2f} MB/s")

# Print a message after the 10 seconds are over
print("Speed test completed.")
