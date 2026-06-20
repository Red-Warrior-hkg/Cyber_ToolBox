\# Directory Monitor



\## Purpose



\*\*Directory Monitor\*\* is a lightweight Python script that continuously monitors a specified directory and detects file system changes in real time.



The script tracks:



\* File creation

\* File deletion

\* File modifications based on:



&#x20; \* File size changes

&#x20; \* Modification timestamp changes



It is designed as a simple and educational project to understand file systems, polling techniques, and basic system monitoring concepts.



\---



\## Features



\*  Monitor any existing directory.

\*  Detect newly created files.

\*  Detect deleted files.

\*  Detect modifications by comparing:



&#x20; - File sizes

&#x20; - Last modification timestamps

\*  Gracefully handles invalid paths and permission errors.

\*  Clean and lightweight implementation using only Python's standard library.

\*  Stop monitoring safely with `Ctrl + C`.



\---



\## Requirements



\* Python \*\*3.8+\*\*

\* No external dependencies.



The project uses only built-in Python modules:



\* `os`

\* `time`



\---



\## Installation







```bash

git clone https://github.com/Red-Warrior-hkg/Cyber\_ToolBox/directory-monitor.git

cd directory-monitor

python diectory\_monitor.py

```



\---



\## Usage



Start the program:



```bash

python diectory\_monitor.py


```



You will be prompted to enter a directory path:



```text

Enter the directory you want to monitor:

```



Example:



```text

Enter the directory you want to monitor: C:\\\\Users\\\\User\\\\Documents



The target directory C:\\\\Users\\\\User\\\\Documents is selected!



\[CREATED] : report.pdf has been created!

\[MODIFIED] : notes.txt Size has been modified

\[MODIFIED] : notes.txt Timestamp has been modified

\[DELETED] : old\\\_file.txt has been deleted!

```



Stop monitoring at any time by pressing:



```text

Ctrl + C

```



The program will exit gracefully.



\---



\## How It Works



The script periodically creates a \*\*snapshot\*\* of the target directory containing:



\* File names

\* File sizes

\* Last modification timestamps



Every 2 seconds, it compares the new snapshot with the previous one to identify:



\* Newly created files

\* Deleted files

\* Modified files



This approach is called \*\*polling\*\* and does not require any external libraries or operating system-specific APIs.



\---



\## License



This project is open source and available under the MIT License.

