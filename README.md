# Graph visualization app

Have you ever wondered is it possible to combine software code like puzzles?🧩🤔 In this project we "turned our brains on" to wire independent components into a masterpiece.✨

## All in One

https://user-images.githubusercontent.com/62771420/224481512-7edb7458-643a-4e59-bc37-9f93f4a4561a.mp4

## Software components
### Parsers
Parsers are components that convert specific data into a graph structure. In this app, we provided three different parser options: **Wikipedia Parser**, **XML Parser**, and **JSON Parser**.✂️
### Main Component
Main Component is the central view where the selected graph is displayed. It is a placeholder for the other three components that can visualize graphs in distinct ways: **Simple Visualization**, **Advanced Visualization**, and **AR Visualization**. 🎯 

![MainComponent](https://user-images.githubusercontent.com/62771420/224480697-de501363-71c3-41a3-a76d-9c4687abc232.gif)

### AR Visualizator
AR Visualizator component lets the user to view his/her graph in augmented reality mode. 😲

![ArVisualizator](https://user-images.githubusercontent.com/62771420/224480743-eee0bae5-d8a4-4a5e-83b5-509485e94c59.gif)

### Bird View
Bird View component is minimized graph visualization shown from the bird's perspective, and additionally provides zoom in/out functions. 🐥

![BirdView](https://user-images.githubusercontent.com/62771420/224480767-83fbbe42-cccb-4a1a-a906-969e0204f930.gif)

### TreeView
TreeView is tree data structure component that unfolds dynamically, lets user to see parent-child relationship and overcomes cycles in graph. 🌴

![TreeView](https://user-images.githubusercontent.com/62771420/224480838-12d6c667-316a-4ad3-968d-f7847a205fdc.gif)

### Search And Filter
Search And Filter component lets the user apply filters on graph and keyword searches, and as a result, displays a graph based on those needs.🔍

![SearchFilter](https://user-images.githubusercontent.com/62771420/224480899-69701645-3885-44f8-adaf-ed33e91a6e2e.gif)


### Applied Filters List
Applied Filters List is a component that enables the user to see all applied filters and searches and to remove them dynamically so the node selection meets his new criteria.🧾

![AppliedFiltersList](https://user-images.githubusercontent.com/62771420/224480908-24995179-6633-470c-b154-c2ad2a7c12b3.gif)

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
Open your browser on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and check it out!
#
