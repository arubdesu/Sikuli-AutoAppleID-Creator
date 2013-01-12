Sikuli-AutoAppleID-Creator
==========================
[Sikuli](http://www.sikuli.org "Home of the Sikuli Script project") is a screen-reading automation tool which can be hooked into with Java or Python.
This repo has a csv and sikuli script to drive iTunes and batch-create Apple IDs, inspired by [http://www.enterpriseios.com/wiki/Batch_Apple_ID_Creator](http://www.enterpriseios.com/wiki/Batch_Apple_ID_Creator)
Just like that predecessor, this creates IDs without a credit card, perfect for training or educational situations.

Currently, there are limitations versus the previous, applescript-based method: SikuliScript uses java, requires focus(it assumes you have iTunes open, and are browsing the store), and I did not code in all conditionals to satisfy every permutation of the security questions Apple presents. I will discuss more of the design behind these choices on [my company's blog](http://techjournal.318.com).

In the repo you'll find AppleIDcreate.sikuli and ids.csv. You must modify the ids.csv file to customize the IDs you'll be creating, and place it in /Users/Shared. Then you must have Sikuli downloaded and installed to run it.

NOTE: Apple may throttle the amount of IDs you can create at once. Please see the thread on enterpriseiOS for more info. Also, this has only been tested in the US version of iTunes, please submit pull requests, or contact me with screenshots of the options for other stores around the world!

Also, if you CAN have people put in a credit card to use the IDs you're tasked with creating, consider using [Fake](http://Fakeapp.com) on [Apple's site](https://appleid.apple.com/cgi-bin/WebObjects/MyAppleId.woa/wa/createAppleId?localang=en_US)
