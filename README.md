# Youtube-Data-Scraper
Scrapes popular youtube videos.

// ------->
function _getData(arg1, arg2)

Arg1 takes in the chrome driver url, while arg2 takes in the url of the youtube channels most popular section.
After running the function, it will return title names and urls.

// <----------

// ------->
function _getVideoData(arg1, arg2, arg3, arg)

Arg1 takes in the chrome driver url, arg2 sets the minium time for the timer, while arg3 sets the maximum time, and arg4 takes in the url of the youtube video.
After running the function, it will return the title, views, date, dislikes and likes.

Note. arg3 and arg4, if set for example arg2 = 2, arg3 = 5.
The timer will choose a random number between 2 and 5.

// <----------

