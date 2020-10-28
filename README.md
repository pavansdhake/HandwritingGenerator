# Handwriting Generator

Specially designed to solve IACV Assignment quickly.

  - Provide your handwriting sample as input
  - solve thresholding questions using script
  - copy handwritten images to word
  - convert word to pdf
  - rescan  pdf using camscanner to give realistic handwritten touch touch

# How to use this tool ?

### Step 1
  - Clone this repository into your PC
  - Make sure you have python 3.7 installed in your PC
  - Use Pycharm as IDE preferably

### Step 2
  - Project only requires Pillow as the third party library
  - Execute command:
 ```sh
    pip install pillow
```

### Step 3 
  - Load your handwriting into the dataset. For this, write 0 to 9 on a white paper 4 times and scan it using camscanner.
  - Crop each digit to equal height but width should be just equal to the width of digit. Sample dataset is already loaded in Dataset directory of project. Replace it with your handwriting dataset. Keep folder structure and naming convention as it is as in the sample dataset

### Step 4 
  - Open the file assignment_solver.py in the main directory. This is the script to solve all thresholding questions in assignment in one go.
  - Execute this file
  - In command window it will ask you to enter matrix A.Copy paste matrix A from assignment and press enter. Similarly it will ask for matix B, matrix C and matrix D. Once all the four matrices are entered, it will ask enter the command.
  - Use commands to all questions. Solution matrix in handwritten format will automatically be saved in solutions directory in this format - 1a.jpg, 1b.jpg, 1c.jpg and so on. 1a.jpg is final matrix after applying thresholding in question 1 to matrix a.

### Step 5
  - Copy Paste the images from solutions directory to ms word. Write question and draw graphs with hand and copy paste the image in word file. Trust me it wont take more than 30 minutes.
  - Use your MS Word skills and common sense to make this MS Word file look handwritten.
  - Save this file as PDF and then rescan this file using camscanner. Trust me nobody would recognize that the assignment is partially computer generated and not handwritten.


#### Commands:

- start: to start a new question. After entering this command, you will be asked to enter question number. Enter only number without space or any character and press enter
- Enter the curve data : after entering question number it will ask you this. Here you have to describe your thresholding curve. Just put description of line here
![image](https://user-images.githubusercontent.com/43084197/97430569-16bc3800-193f-11eb-8557-2e394e59f7f2.png)
- For example, curve description of above curve will be like this>
 ```sh
    line 0 0 127 0
    line 127 255 255 255
    end
```

General form of this description is like this:
 ```sh
    line x1 y1 x2 y2
 ```
 
 Command of all the questions in assignment is given in the ReadHere directory. You can simply copy commands from there in case you find it difficult to understand them.
 
 ### How long will it take ?
 If you have good MS Word skills and ability to quickly crop the images, entire assignment would be completed within less than 2 hours only!!! 
 
 ![image](https://user-images.githubusercontent.com/43084197/97431492-694a2400-1940-11eb-8f84-52c7a05393e4.png)
 
 ![image](https://user-images.githubusercontent.com/43084197/97431576-8f6fc400-1940-11eb-80a5-099ccbf2cd1d.png)

 
 
 ## All the best!!!
