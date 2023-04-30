# the pomodoro technique 
    ## francesco 

1. figure out the task
2. set a time for 25 minutes
3. work for 25 minutes
4. 5 minute break
5. after 4 loops, take a 15 minute 

25 min work => 5 min break => 25 min work => 5 min break => 25 min work =>
5 min break => 25 min work => 20 min break

#insert image and overlay text
* tkinter.Canvas()
* allows for layering
* create_image() method
  * require x and y position
  * image parameter expects photoimage from tk.PhotoImage() class
  * canvas has its own bg that sits on top of the window
* use the fg= parameter to give widgets text a different color from the background
* bg for widget background
* the after() method can be used on a window object to call a function after a given interval
  * use after_cancel(widget) to suspend scheduling
* canvas.itemconfig(item_to_alter, **kwarg to alter)

# dynamic typing
~~~
count_sec = count % 60
if count_sec == 0:
  count_sec = "00"
~~~
### python lets you freely convert variables from one type to another
#### but its strongly typed when it comes to functions. if a function is
#### expecting an int but you pass it a string, you will get a
#  T Y P E E R R O R
