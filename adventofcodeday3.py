Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
[5, 10, 25]
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
[5, 10, 25]
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
[5, 10, 25]
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <module>
    numbers = [int(number) for number in line.split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <listcomp>
    numbers = [int(number) for number in line.split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <module>
    numbers = [int(number.strip()) for number in line.split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <listcomp>
    numbers = [int(number.strip()) for number in line.split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
  775  785  361

Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <module>
    numbers = [int(number.strip()) for number in line.split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <listcomp>
    numbers = [int(number.strip()) for number in line.split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
['', '775', '785', '361\n']
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <module>
    numbers = [int(number.strip()) for number in line.split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <listcomp>
    numbers = [int(number.strip()) for number in line.split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 12, in <module>
    print("result:" + numbers);
TypeError: Can't convert 'list' object to str implicitly
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 14, in <module>
    print("result:" + count);
TypeError: Can't convert 'int' object to str implicitly
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
3
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
[361, 775, 785]
[125, 375, 622]
[297, 375, 839]
[38, 245, 891]
[463, 503, 849]
[482, 731, 759]
3
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
[361, 775, 785]
[125, 375, 622]
[297, 375, 839]
[38, 245, 891]
[463, 503, 849]
[482, 731, 759]
[29, 734, 734]
[245, 269, 771]
[261, 315, 904]
[96, 581, 669]
[156, 570, 745]
[124, 678, 684]
[73, 360, 472]
[174, 251, 926]
[406, 408, 976]
[238, 413, 571]
[22, 375, 554]
[211, 379, 590]
[271, 821, 847]
[116, 253, 696]
[513, 959, 972]
[539, 557, 752]
[168, 362, 550]
[236, 284, 690]
[91, 434, 818]
[393, 779, 859]
[56, 313, 620]
[188, 783, 983]
[573, 799, 900]
[359, 565, 932]
[69, 357, 670]
[52, 71, 525]
[43, 640, 654]
[695, 781, 907]
[676, 680, 938]
[63, 507, 570]
[492, 587, 985]
[34, 333, 984]
[25, 399, 489]
[43, 158, 470]
[491, 617, 715]
[412, 508, 607]
[365, 446, 743]
[189, 378, 504]
[225, 424, 517]
[45, 473, 649]
[424, 847, 927]
[455, 697, 889]
[64, 230, 846]
[368, 579, 881]
[74, 536, 639]
[433, 803, 943]
[14, 629, 963]
[136, 432, 481]
[323, 625, 781]
[201, 215, 836]
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 9, in <module>
    print(numbers)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1343, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <module>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 6, in <listcomp>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <module>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 5, in <listcomp>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 4, in <module>
    errorLine;
NameError: name 'errorLine' is not defined
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
  849    4  295

Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 8, in <module>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 8, in <listcomp>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
  849    4  295

Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 9, in <module>
    print(line.strip.split("  "))
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
['849', '4', '295']
['849', '', '4', '295']
 

 

8
8
4
4
9
9
 

 

 

 

4
4
 

 

2
2
9
9
5
5



  849    4  295

Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 13, in <module>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 13, in <listcomp>
    numbers = [int(number.strip()) for number in line.strip().split("  ")]
ValueError: invalid literal for int() with base 10: ''
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
1
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
882
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
882
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
882
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
882
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
3
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
3
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
245 38 891
3
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
245 38 891
261 315 904
174 251 926
406 408 976
211 379 590
168 362 550
434 91 818
63 507 570
473 45 649
64 230 846
14 629 963
20 41 648
99 119 584
175 40 994
8 234 831
184 254 958
380 109 842
84 192 465
180 130 726
88 273 735
310 532  310  532  897

Traceback (most recent call last):
  File "/Users/HPDeskjetPrinter/Desktop/adventofcode.py", line 18, in <module>
    print(numbers[0],numbers[1],numbers[2])
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1343, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
882
>>> 
========== RESTART: /Users/HPDeskjetPrinter/Desktop/adventofcode.py ==========
1032
>>> 
