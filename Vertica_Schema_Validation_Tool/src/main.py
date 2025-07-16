#!/usr/bin/python
import subprocess
import os
import time

GREEN = '\033[92m'
RESET = '\033[0m'
BLUE = '\033[94m'
RED = '\033[31m' 

def main():
#    print("=== Radcom Vertica Schema Validation Tool ===\n")
#    print("Version   : v1\n")
#    print("Developer : PSO DevOps\n")
#    print("Developed On : 22nd May 2025\n")
#    print("Changes   : v1 : Initial Draft\n")
#    print("###########################################################################################")
#    print("###########################################################################################")
    print("+--------------------------------------------------------------------------------------------+")
    print("| \033[94m        Welcome to Radcom Vertica Schema Validation Tool -- Developed By PSO-DevOps       \033[0m |")
    print("+--------------------------------------------------------------------------------------------+")
    print("+--------------------------------------------------------------------------------------------+\n")
    print("\033[4mType a number to choose the activity you want to perform.\033[0m\n")

    print("     1) Generate Schema Report for Pre Validation. (Note:: This step saves current schema of Vertica which can be taken reference further).")
    print("     2) Generate Schema Report for Post Validation. (Note:: This step generates file which can be compare with pre-validation file).")
    print("     3) Perform comparison b/w Pre-Validation & Post-validation Report .")
    print("     4) Exit.")

    choice = input("\nEnter Your Choice: ").strip()

    if choice == "1":
          print("\n\033[92mDo you want to continue on same stack ? Press Y or N(For Different Stack).\033[0m")
          stack_choice = input("\nEnter Your Choice: ").strip()
          if stack_choice == "Y":
              subprocess.run(["python3.11", "__internal_report_v0"])
          elif stack_choice == "N":
              print("\n+-------------------------------------------+")
              print("➡️ Building Pre Validation Schema Report ......")
              print("+-------------------------------------------+\n")
              subprocess.run(["python3.11", "__internal_report_v1"])
          else:
              print("\n\033[31mPlease enter only Y or N....\033[0m\n")
              print("\n➡️ Exiting the Program.......Goodbye! \n")
              exit()
    elif choice == "2":
          print("\n\033[92mDo you want to continue on same stack ? Press Y or N(For Different Stack).\033[0m")
          stack_choice = input("\nEnter Your Choice: ").strip()
          if stack_choice == "Y":
              subprocess.run(["python3.11", "__internal_report_v3"])
          elif stack_choice == "N":
              print("\n+-------------------------------------------+")
              print("➡️ Building Post Validation Schema Report ......")
              print("+-------------------------------------------+\n")
              subprocess.run(["python3.11", "__internal_report_v2"])
    elif choice == "3":
        print("\n➡️ Running Comparison ...\n")
        subprocess.run(["python3.11", "__core_validation"])
    elif choice == "4":
        print("\n➡️ Exiting the Program.......Goodbye! \n")
        time.sleep(1)
        exit()
    else:
        print("❌ Invalid choice. Please enter valid number")

if __name__ == "__main__":
    main()


