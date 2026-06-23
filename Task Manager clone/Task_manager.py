import psutil
import time
try:
    while True:
        print('\033c', end='')
        data = []
        memory = psutil.virtual_memory()

        #Header
        print(f"{'Process':<30} {'CPU%':>8} {'RAM%':>8} {'Disk Read (MB)':>15} {'Disk Write (MB)':>15}")
        print("-" * 78) 
        
        for process in psutil.process_iter(['name','cpu_percent','memory_percent','io_counters']):
            try:
                cpu = process.info['cpu_percent']
                name =  process.info['name'] or "Unknown"
                ram = process.info['memory_percent']
                disk = process.info['io_counters']
                if disk:
                   read_mb = disk.read_bytes / (1024*1024)
                   write_mb = disk.write_bytes / (1024*1024)
                if cpu > 0 or ram > 0.1 or read_mb > 0.01 or write_mb > 0.01:
                   data.append((name, cpu, ram, read_mb, write_mb))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        data.sort(key=lambda x: x[1], reverse=True)

        for name, cpu, ram,  read_mb, write_mb in data:
            print(f"{name[:28]:<30} {cpu:>7.1f}% {ram:>7.1f}% {read_mb:>14.1f}MB {write_mb:>14.1f}MB")
        mem = psutil.virtual_memory()
        print(f"\nLast update: {time.strftime('%H:%M:%S')} | RAM: {mem.percent}% used ({mem.used//1024//1024}MB / {mem.total//1024//1024}MB)")
        time.sleep(5)
except KeyboardInterrupt:
    print("\n\n[+] Monitoring stopped by user.")

