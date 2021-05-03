import cProfile
import pstats
import io
# importing two programs that we wrote before
import Task1 as t1 

import Task2 as t2 

#method for calling all the methods in the two programs that we wrote before
def main():
    t1.detail()
    t1.detailTemp()
    t1.detailVol()
    t2.detailDownsampled()
    t2.detailTempDownsampled()
    t2.detailVol_resample()
    return True #returning true value so that this can be used by the assert method(unittest) whether this
    #            methodhave been executed successfully

#Using cprofile and saving the results into a text file
def func1():
    result = []
    for i in range(10000):
        result.append(i)

    return result

pr = cProfile.Profile()
pr.enable()

my_result = main()

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('cprofile2.txt', 'w+') as f:
    f.write(s.getvalue())


func1()
