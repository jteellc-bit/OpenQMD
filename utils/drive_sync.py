# Optional helper to mount Google Drive and sync data

def mount_drive():
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print("Drive mounted successfully.")
    except Exception as e:
        print("Drive mount not available:", e)
