# foosbot-results
Foosball results for the OpenCredo foosbot, summer 2016 - beginning of 2017.

The foosbot stores results in a pickle format that it stores on AWS. That pickle format is what is stored in `core.py`. This is a simple script that unpickles that and outputs it as json.

Note that foosbot identifies users not by their usernames, but by a unique user ID assigned to your user by Slack.
