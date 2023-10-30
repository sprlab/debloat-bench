sen = "I am a sentence."
with open("test.txt", "w") as f:
    f.write(sen)
    f.close()


# check if a file exits or not
# Path: test_exists.py
import os
if os.path.exists("test.txt"):
    exit(0)
else:
    print("File does not exist")
    exit(1)
