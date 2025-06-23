import os
import subprocess
import platform
import time

def change_directory(path):
    # Change directory based on the operating system
    if platform.system() == "Windows":
        os.system(f'cd "{path}"')
    else:
        os.chdir(path)

def install_dependencies():
    # Install npm dependencies
    print("Installing npm dependencies...")
    subprocess.run("npm install", shell=True)
    
    # Install pip dependencies
    print("Installing pip dependencies...")
    subprocess.run("pip install -r requirements.txt", shell=True)

def start_servers():
    # Start Flask backend server
    print("Starting Flask backend server...")
    backend_process = subprocess.Popen("flask run", shell=True)

    # Allow backend to start
    time.sleep(5)

    # Start React frontend server
    print("Starting React frontend server...")
    frontend_process = subprocess.Popen("npm start", shell=True)

    return backend_process, frontend_process

def main():
    project_path = "ENTER THE PROJECT PATH HERE"

    # Change to the project directory
    print(f"Changing directory to: {project_path}")
    change_directory(project_path)
    
    # Install all dependencies
    install_dependencies()
    
    # Start servers
    backend_process, frontend_process = start_servers()
    
    # Keep the servers running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()

if __name__ == "__main__":
    main()
