import os
import sys
import subprocess
import time
import threading


def loading_animation():
    animation = "|/-\\"
    idx = 0
    while not done:
        sys.stdout.write("\rScanning... " + animation[idx])
        sys.stdout.flush()
        idx = (idx + 1) % len(animation)
        time.sleep(0.1)
    sys.stdout.write("\rScanning... Done!\n")


def run_nmap_scan(target):
    global done
    try:
        # Replace 'your_scan_target' with the target IP or hostname you want to scan
        cmd = f'nmap  -T4 --openn -sC -sV {target} -oN internal_scan '
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
    except subprocess.CalledProcessError as e:
        print("Error running nmap:", e)
    done = True

def nmap_scanner(targeet):
    global done
    done = False
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    nmap_thread = threading.Thread(target=run_nmap_scan ,args=((targeet,)))
    nmap_thread.start()

    # Wait for the nmap scan to finish
    nmap_thread.join()

    # Ensure the loading animation thread stops
    done = True
    loading_thread.join()   

nmap_scanner('sunway.edu.np')
