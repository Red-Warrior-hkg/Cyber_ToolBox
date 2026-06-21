# Directory Monitor


## Purpose
**Directory Monitor** is a lightweight Python script that continuously monitors a specified directory and detects file system changes in real time.

The script tracks:
* File creation

* File deletion

* File modifications based on:
    -  File size changes
    - Modification timestamp changes

It is designed as an educational project to understand file systems, polling techniques, and system monitoring concepts.



---



## Features

*  Monitor any existing directory.

*  Detect newly created files.

*  Detect deleted files.

*  Detect modifications by comparing:
     - File sizes
     - Last modification timestamps

*  Gracefully handles invalid paths and permission errors.

*  Clean and lightweight implementation using only Python's standard library.

*  Stop monitoring safely with `Ctrl + C`.

---

## Requirements
* Python **3.8+**

* No external dependencies.

## Installation

```bash

git clone https://github.com/Red-Warrior-hkg/Cyber_ToolBox.gti

cd directory-monitor

python diectory_monitor.py

```

---



## Usage

Start the program:

```bash
python diectory_monitor.py
```
You will be prompted to enter a directory path:

```text
Enter the directory you want to monitor:
```

Example:

<img width="910" height="172" alt="image" src="https://github.com/user-attachments/assets/56cf2048-c130-4123-b630-dab625a8572d" />

The program will exit gracefully.

---

## How It Works

The script periodically creates a **snapshot** of the target directory containing:

* File names

* File sizes

* Last modification timestamps



Every 2 seconds, it compares the new snapshot with the previous one to identify:



* Newly created files

* Deleted files

* Modified files



This approach is called **polling** and does not require any external libraries or operating system-specific APIs.



---



## License



This project is open source and available under the MIT License.

