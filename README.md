# Graph visualization app - tim02

This is a django application for parsing and visualizing data with graph data structure.

## Installation
### First step
1. Choose a directory
2. Open CMD or Bash 
3. Create a virtual environment
4. Activate it

To achieve this follow below.

#### For Windows users:
```bash
python -m venv venv
```
If you’re using Python on Windows and you haven’t configured the PATH and PATHEXT variables, then you might need to provide the full path to your Python executable:
```bash
C:\Users\Name\AppData\Local\Programs\Python\Python310\python -m venv venv
```
For activation run following command:
```bash
venv\Scripts\activate
```
#### For Linux and MacOS users:
```bash
python3 -m venv venv
```
For activation run following command:
```bash
source venv/bin/activate
```
### Second step
Clone this repository in current directory by typing following command:

```bash
git clone https://gitlab.com/sok_2022_2023/tim02.git
```
### Third step
Change location directory location
```bash
cd ./tim02
```
### Fourth step
For all required packages to be installed in your venv run the following.
#### For Windows users:
```bash
python -m pip install -r requirements.txt
```
#### For Linux and MacOS users:
```bash
python3 -m pip install -r requirements.txt
```
### Fifth step
Run installation script:
#### For Windows users:
```bash
.\run.bat
```
#### For Linux and MacOS users:
```bash
./run.sh
```
### Sixth step
Open your browser on [http://localhost:8000/](http://localhost:8000/) and check it out!
#