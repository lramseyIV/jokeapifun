# jokeapifun
Sends you an email of a random joke pulled from the jokes API


This is just a little simple program I wrote in a few minutes just because. Good for beginners to learn and build upon.

NOTE: The config.json file is where you will replace the appropriate fields with your email and password.

Also note that if you are using anything other than gmail you must change the mail server. s = smtplib.SMTP('smtp.whatever.com', 587)


For Google users: If you have multifactor authentication built in you must follow the steps at the link below and place that app password in the json file.

https://support.google.com/accounts/answer/185833?hl=en

Apparently google now requires you to have a password for each application you use which is smart but a pain when you want to test some things out for fun like this.

You can schedule this task to run every so often using whatever tools your operating system provides to do so. I prefer Linux cron jobs but whatever floats your boat.
You can place scheduling within the script itself but that involves it running all of the time in the background in an infinite loop which seems a little over the top for a cute little number like this.

Have fun with it, it's nothing special but use it as a learning tool. :)
