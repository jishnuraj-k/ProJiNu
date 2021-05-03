# ProJiNu

In this assignment I had first extracted the xlxs files separately from the workbook with the help of visual basics 
and I stored this dataset at a particular location. Then I wrote a python code (Task1) for accessing details,detailTemp
and detailVol xlxs files separately and I combined all the xlxs file that belongs to details as one dataframe, all the
xlxs file that belongs to detailsTemp as one csv file and all the xlxs file that belongs to detailsVol as another csv 
file and I saved these as csv files. Then I wrote a python code (Task 2) for down sampling each of the csv files that we
saved befored by making Absolute time or Real time as index columns and I saved these files as detailDownsampled.csv, 
DetailTempDownsampled.csv and DetailVolDownsampled.csv. The I created a jupyter notebook (Task 3) for applying low pass
filter for noise reduction and I visualised it using a plot functiom. Then I used profiling (Cprofile) (Task 4) for running
the functions that I created in this program and the results are stored into a text file(cprofile2.txt). In the task 5 
(unittest) I made every function to return a Boolean value and I tested whether its returning true value using assert value
function. Then in the task6 I checked whether the code that I wrote follow PEP-8 using pylint and I stored the results to text
file (unittestresult.txt). 
