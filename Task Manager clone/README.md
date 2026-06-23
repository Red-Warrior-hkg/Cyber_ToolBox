# Task Manager

## Purpose
**Task Manager clone** is a lightweight Tool that runs directly in your terminal, providing real-time monitoring of all active system processes and overall memory usage.

The script tracks:
* Process name

* CPU usage percentage

* RAM usage percentage

* Disk Read activity (MB)

* Disk Write activity (MB)

It is designed as an educational project to understand system monitoring, process management, and resource tracking concepts.

---

## Features

* Real-time display of all active processes, refreshed every **5 seconds**.
* Processes sorted by **CPU usage** (highest first).
* Filters out idle processes to keep the output clean and focused.
* Displays a system-wide **RAM summary** at the bottom.
* Gracefully handles inaccessible or terminated processes.
* Clean terminal output with auto-clear on each refresh.
* Stop monitoring safely with `Ctrl + C`.

---

## Requirements

* Python **3.8+**

* [`psutil`](https://pypi.org/project/psutil/) library

## Installation

```bash

git clone https://github.com/Red-Warrior-hkg/Cyber_ToolBox.git
cd Task Manager clone
pip install psutil

python taskmanager.py

```

---

## Usage

Start the program:

```bash

python taskmanager.py

```

The terminal will auto-clear and display a live process table:

```text

Process                          CPU%     RAM%   Disk Read (MB)  Disk Write (MB)

------------------------------------------------------------------------------

chrome.exe                       15.3%    4.2%          0.5MB           0.1MB

python.exe                        8.1%    1.0%          0.0MB           0.0MB

explorer.exe                      2.4%    0.8%          0.2MB           0.0MB

...



Last update: 14:32:05 | RAM: 62.4% used (9984MB / 16384MB)

```



Press `Ctrl + C` to exit:

```text
[+] Monitoring stopped by user.
```



---

## How It Works

The script uses **psutil** to iterate over all running system processes every 5 seconds and collects:

* **CPU %** — percentage of CPU time consumed by the process.

* **RAM %** — percentage of total system memory used.

* **Disk I/O** — cumulative read and write bytes converted to megabytes.



Processes with no meaningful activity are **filtered out** to reduce noise. The remaining processes are **sorted by CPU usage** in descending order and printed in a formatted table.

The terminal is **cleared on each refresh** using an ANSI escape code (`\\033c`) for a smooth live-update feel

---

## License

This project is open source and available under the MIT License.

