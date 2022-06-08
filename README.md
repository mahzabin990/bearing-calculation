# bearing-calculation

This is a program that converts forward bearing to backward bearing. [definitions](https://esenotes.com/fore-bearing-back-bearing-declination-angle-of-dip/#:~:text=Bearing%20measured%20from%20one%20station,a%20difference%20of%20180%C2%B0.) <br>
For now it supports Whole Circle Bearing. But I am also planning to add reduced bearing soon!

## Motivation

As currently I am learning python and my educational background is in Water Resource Engineering, I thought to combine my educational background knowledge with python
and make a simple tool. So here this is the product.

## What I've Practised through this project

* Object Oriented Programming with method overloading. see [wcb.py](./wcb.py) and [parse_csv.py](./parse_csv.py) files.
* csv module
* file operations
* functions
* dictionary
* list
* documenting functions and classes
* basic git and github operations

## How to use the program

Well using is pretty simple.<br>
One requirement: A [`forward_bearings.csv`](./forward_bearings.csv) file. where you need to put your forward bearings.<br>
Now simply run:

```bash
python main.py
```
This will generate a file called `solution.csv`. with an additional column that contains back bearings of each row.
