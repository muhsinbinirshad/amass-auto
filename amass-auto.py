import os

print("Select an Amass function to run:")
print("1. Enumeration")
print("2. Passive DNS")
print("3. Active DNS")
print("4. Brute Forcing")
print("5. All of the above")

choice = int(input("Enter a number: "))

domain = input("Enter domain to scan: ")
output_name = input("Enter a unique name for the output file: ")

if choice == 1:
    print("Running Amass Enumeration...")
    os.system(f"amass enum -d {domain} -o {output_name}_enum.txt")
elif choice == 2:
    print("Running Amass Passive DNS...")
    os.system(f"amass dns -d {domain} -passive -o {output_name}_passive_dns.txt")
elif choice == 3:
    print("Running Amass Active DNS...")
    os.system(f"amass dns -d {domain} -active -o {output_name}_active_dns.txt")
elif choice == 4:
    print("Running Amass Brute Forcing...")
    os.system(f"amass brute -d {domain} -o {output_name}_brute_force.txt")
elif choice == 5:
    print("Running all Amass functions...")
    os.system(f"amass enum -d {domain} -o {output_name}_enum.txt")
    os.system(f"amass dns -d {domain} -passive -o {output_name}_passive_dns.txt")
    os.system(f"amass dns -d {domain} -active -o {output_name}_active_dns.txt")
    os.system(f"amass brute -d {domain} -o {output_name}_brute_force.txt")
else:
    print("Invalid choice. Please enter a number from 1 to 5.")

