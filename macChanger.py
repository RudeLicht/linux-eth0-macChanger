import os
import re
import subprocess

def change_mac():
    while True:
        newMac = input("Enter new MAC address (e.g., 00:11:22:33:44:55): ")
        
        # Check if the input matches the expected MAC address format
        if re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", newMac):
            return newMac
        else:
            print("Invalid MAC address format. Please try again.")

def main():
    choice = input("Are you sure? [Y] [N]: ")

    if choice.lower() == 'y':
        print("Shutting eth0 down")
        os.system("ifconfig eth0 down")
        
        newMac = change_mac()

        try:
            os.system(f"ifconfig eth0 hw ether {newMac}")
        except Exception as e:
            print(f"Error setting new MAC address: {e}")
            return

        print("Updated new MAC address")
        print("Starting eth0")

        try:
            os.system("ifconfig eth0 up")
        except Exception as e:
            print(f"Error starting eth0: {e}")
            return

        # Use subprocess to capture the output of ifconfig
        result = subprocess.run(["ifconfig", "eth0"], capture_output=True, text=True)
        
        if newMac.lower() in result.stdout:
            print("MAC address changed successfully")
            print(result.stdout)
        else:
            print("Failed to change MAC address")
            print(result.stdout)

    elif choice.lower() == 'n':
        print("Bye")

    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()



