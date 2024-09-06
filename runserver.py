import subprocess
def main():
    command = "python manage.py runserver 192.168.45.211:8080"
    subprocess.run(command, shell=True)
    
if __name__ == "__main__":
    main()