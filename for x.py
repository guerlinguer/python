Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
range(10)
range(0, 10)
for x in range(10):
    print("3 x ", x, "=", 2 * x)

    
3 x  0 = 0
3 x  1 = 2
3 x  2 = 4
3 x  3 = 6
3 x  4 = 8
3 x  5 = 10
3 x  6 = 12
3 x  7 = 14
3 x  8 = 16
3 x  9 = 18
for x in range(10):
    print("3 x ", x, "=", 3 * x)

    
3 x  0 = 0
3 x  1 = 3
3 x  2 = 6
3 x  3 = 9
3 x  4 = 12
3 x  5 = 15
3 x  6 = 18
3 x  7 = 21
3 x  8 = 24
3 x  9 = 27
for x in range(11):
    print("3 x ", x, "=", 3 * x)

    
3 x  0 = 0
3 x  1 = 3
3 x  2 = 6
3 x  3 = 9
3 x  4 = 12
3 x  5 = 15
3 x  6 = 18
3 x  7 = 21
3 x  8 = 24
3 x  9 = 27
3 x  10 = 30
x
10
for x in range(100) :
    print("3 x ", x, "=", 3 *x)

    
3 x  0 = 0
3 x  1 = 3
3 x  2 = 6
3 x  3 = 9
3 x  4 = 12
3 x  5 = 15
3 x  6 = 18
3 x  7 = 21
3 x  8 = 24
3 x  9 = 27
3 x  10 = 30
3 x  11 = 33
3 x  12 = 36
3 x  13 = 39
3 x  14 = 42
3 x  15 = 45
3 x  16 = 48
3 x  17 = 51
3 x  18 = 54
3 x  19 = 57
3 x  20 = 60
3 x  21 = 63
3 x  22 = 66
3 x  23 = 69
3 x  24 = 72
3 x  25 = 75
3 x  26 = 78
3 x  27 = 81
3 x  28 = 84
3 x  29 = 87
3 x  30 = 90
3 x  31 = 93
3 x  32 = 96
3 x  33 = 99
3 x  34 = 102
3 x  35 = 105
3 x  36 = 108
3 x  37 = 111
3 x  38 = 114
3 x  39 = 117
3 x  40 = 120
3 x  41 = 123
3 x  42 = 126
3 x  43 = 129
3 x  44 = 132
3 x  45 = 135
3 x  46 = 138
3 x  47 = 141
3 x  48 = 144
3 x  49 = 147
3 x  50 = 150
3 x  51 = 153
3 x  52 = 156
3 x  53 = 159
3 x  54 = 162
3 x  55 = 165
3 x  56 = 168
3 x  57 = 171
3 x  58 = 174
3 x  59 = 177
3 x  60 = 180
3 x  61 = 183
3 x  62 = 186
3 x  63 = 189
3 x  64 = 192
3 x  65 = 195
3 x  66 = 198
3 x  67 = 201
3 x  68 = 204
3 x  69 = 207
3 x  70 = 210
3 x  71 = 213
3 x  72 = 216
3 x  73 = 219
3 x  74 = 222
3 x  75 = 225
3 x  76 = 228
3 x  77 = 231
3 x  78 = 234
3 x  79 = 237
3 x  80 = 240
3 x  81 = 243
3 x  82 = 246
3 x  83 = 249
3 x  84 = 252
3 x  85 = 255
3 x  86 = 258
3 x  87 = 261
3 x  88 = 264
3 x  89 = 267
3 x  90 = 270
3 x  91 = 273
3 x  92 = 276
3 x  93 = 279
3 x  94 = 282
3 x  95 = 285
3 x  96 = 288
3 x  97 = 291
3 x  98 = 294
3 x  99 = 297
for angulo in [0,90,180,270]:
    print(angulo)

    
0
90
180
270
import turtle


for x in range(100):
    turtle.forward(x * 5)
    turtle.right(90)

    
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3193, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    turtle.forward(x * 5)
  File "<string>", line 12, in forward
turtle.Terminator
for x in range(100):
    turtle.forward(x * 10)
    turtle.right(90)

    
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3193, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    turtle.forward(x * 10)
  File "<string>", line 12, in forward
turtle.Terminator

forfor x in range(100):
    turtle.forward(x * 2)
    turtle.right(90)
    
SyntaxError: invalid syntax
for x in range(100):
    turtle.forward(x * 2)
    turtle.right(90)

    
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3193, in _goto
    screen._drawline(self.drawingLineItem,
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    turtle.forward(x * 2)
  File "<string>", line 12, in forward
turtle.Terminator
for x in range(100):
    turtle.forward(x * 5)
    turtle.right(45)

    
Traceback (most recent call last):
  File "<pyshell#28>", line 3, in <module>
    turtle.right(45)
  File "<string>", line 8, in right
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
for x in range(100):
    turtle.forward(x * 5)
    turtle.right(360)

    
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    turtle.right(360)
  File "<string>", line 8, in right
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

for x in range(100):
    turtle.forward(x * 5)
    turtle.right(180)

    
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    turtle.forward(x * 5)
  File "<string>", line 5, in forward
turtle.Terminator
for x in range(100):
    turtle.forward(x * 5)
    turtle.right(45)

    
Traceback (most recent call last):
  File "<pyshell#34>", line 3, in <module>
    turtle.right(45)
  File "<string>", line 8, in right
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

for x in range(100):
    turtle.forward(x * 2)
    turtle.right(45)

    
Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    turtle.right(45)
  File "<string>", line 8, in right
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3293, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

for x in range(100):
    turtle.forward(x * 2)
    turtle.right(15)

    
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    turtle.right(15)
  File "<string>", line 8, in right
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1679, in right
    self._rotate(-angle)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3295, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

for x in range(100):
    turtle.forward(x * 2)
    turtle.right(91)

    
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    turtle.forward(x * 2)
  File "<string>", line 5, in forward
turtle.Terminator
for x in range(100):
    turtle.circle(x * 2)
    turtle.right(90)

    
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    turtle.circle(x * 2)
  File "<string>", line 8, in circle
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1994, in circle
    self._rotate(w)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3295, in _rotate
    self._update()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator

for x in range(100):
    turtle.retangle(x * 2)
    turtle.right(90)

    
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    turtle.retangle(x * 2)
AttributeError: module 'turtle' has no attribute 'retangle'. Did you mean: 'tiltangle'?
for x in range(100):
    turtle.forward(x * 2)
    turtle.right(90)
... 
...     
Traceback (most recent call last):
  File "<string>", line 8, in forward
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3198, in _goto
    screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)),
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\Softgraf\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 2822, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    turtle.forward(x * 2)
  File "<string>", line 12, in forward
turtle.Terminator
>>> for x in range(100):
...     turtle.forward(x * 2)
...     turtle.right(10)
... 
...     
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    turtle.forward(x * 2)
  File "<string>", line 5, in forward
turtle.Terminator
