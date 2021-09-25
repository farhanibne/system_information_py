import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system.Model}")
print(f"Name: {my_system.Name}")
print(f"Number of Processor: {my_system.NumberOfProcessors}")
print(f"System Type: {my_system.SystemType}")
print(f"System Family: {my_system.SystemFamily}")
