# Week 2 - Project 1 - Installing Python

## Install Python on Windows

Installing Python on Windows is relatively easy when using [chocolatey](https://community.chocolatey.org/) as package manager.

1. [Install Chocolatey](https://docs.chocolatey.org/en-us/choco/setup)
   - In Powershell:  
     `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
   - In CMD:  
     `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`
2. Install Python with the following command:  
   `choco install python -y`
3. Check if python is installed by running:  
   `python --version`
4. Check if pip is correctly installed:  
   `pip --version`

### Configure Virtual Environment on Windows

A virtual environment encapsulates all changes made by python within a separate space so it does not effect our whole computer.
This is very handy as we can change settings or install packages that will not interfere with anything running currently on our system and therefore is also easily disposable.

To set up our virtual environment we need to follow these steps:

1. Create a new directory for your virtual environment:  
   `mkdir pythonvenv`
2. Create the virtual environment within that directory:  
   `python -m venv .\pythonvenv\`
3. Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. We will use the PS script for this:

   ```Powershell
       cd .\pythonvenv
       .\Scripts\Activate.ps1
   ```
