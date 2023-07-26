
# <p align="center">Welcome to Cortex Parse Prefetch</p>
  
This project is an fork of w10 prefetch (https://github.com/bromiley/tools/blob/master/win10_prefetch/w10pf_parse.py).

During the forensic stages, it is not uncommon to retrieve the prefetch files used to find the times of the last executions of software present on a Windows system.


The cortex analyzer automates the extraction of data contained in a PF_DATA file.

We can run the parser from thehive or directly in cortex, or even run the script on its own.
    
## 🧐 Features    

- Run a cortex parse prefetch job on a PF_DATA 
- Run a cortex parse prefetch job on a  zip file which contains several PF_DATA  files

        
## 🛠️ Tech Stack
- [python](https://python.org/)
- [Cortex](https://docs.thehive-project.org/cortex/)


## 🛠️ Install  on python root package (depracated)
By default, when you install oython, you have a root environment that is global to the whole system.

Cortex presents different analyzers that are written with different versions of python and its dependencies, which may be incompatible with each other. 

If it's not a problem for us, you can simply make a :

```bash
pip3 install -r requirements.txt
```

And replace the first line of Cortex_Parse_Prefetch.py :like this

```
## before 
#!/home/debian/myenv/prefetch/bin/python3.9

## after
#!/usr/bin/env python3

```


## 🛠️ Install  on python virtual env
    

This is not explicitly mentioned in the Cortex documentation, which insists on using Docker, but you can (as I did) create a python environment and use the pip installer present in my environment.

For example, I've created a directory called myenv where I create a different environment for each analyzer :


```bash
mkdir -p /home/debian/myenv/prefetch
```

Then I create a python environment in the myenv directory : 

```bash
cd /home/debian/myenv
python3 -m venv prefetch
```

We can activate the environment :

```bash
source prefetch/bin/activate
````

We can use our environment's pip3 tool to install dependencies locally without impacting python's root environment


```bash
./prefetch/bin/pip3 install -r requirements.txt
````


As shown in the first line of the  Cortex_Parse_Prefetch.py file, you must point execution to the python binary local to the environment :

```
## before 
#!/home/debian/myenv/prefetch/bin/python3.9
```
           
## 🧑🏻‍💻 Usage Without Cortex
...comming soon

## 🧑🏻‍💻 Usage With Cortex
        
## 🙇 Author
#### hack'im
- Linkedin: [@hak'im](https://www.linkedin.com/in/hakim-djelili/)

