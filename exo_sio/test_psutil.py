import psutil as ps

boot_time = ps.boot_time()
print("Time since system boot: ", boot_time / 60 / 60," hour(s)")

cpu_core = ps.cpu_count()
print("Number of core in the CPU: ", cpu_core)

cpu_core_phy = ps.cpu_count(False)
print("\t_physical core in the CPU: ", cpu_core_phy)

cpu_freq = ps.cpu_freq()
print("CPU frequency: ", cpu_freq)

cpu_percent = ps.cpu_percent()
print("CPU frequency: ", cpu_percent)
