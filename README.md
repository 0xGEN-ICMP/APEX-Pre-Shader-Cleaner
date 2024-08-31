
# APEX Pre-Shader Cleaner






#### Why?

I wrote the Python script because, in APEX Legends, when playing through Steam, there is an issue where the preshader cache frequently gets redownloaded—sometimes daily or even after a restart. For users with slow internet connections, downloading over 8GB of preshader cache each time is frustrating and prevents them from playing immediately. A workaround was to manually clear the cache and redownload it, which seemed to resolve the issue. However, simply disabling the precache function in Steam never worked. As more people, including Linux newcomers, faced this problem, I decided to create a Python script that checks whether the cache exists, verifies if Steam is running, and properly clears the cache.

#### Can I use this script without using the Steam version?

This script is not suited and tested on the non-steam APEX version


#### Which Steam version has been tested?

Currently just the normal .deb package - ~~havent tested it with the flatpak version~~

#### Can I use this script to delete other precached shader?

Yes absolutly! Just change the Game ID - you will find the Game IDs on SteamDB for instance

#### Could I just simply use the rm command to do that after closing Steam?

Yes... but remember there are always confused users here and there. This script is just the convenient way to do so because it covers up simple things like "Have you stopped your Steam client instead of just closes the window?" etc. - think you will get it.

As Linux community members, we want to make it as easy as possible for new users to get started and resolve any issues they might encounter with minimal effort.




## How to use it

- Go to your Steam Settings --> Downloads --> deactivate Shader Pre-Caching

- Close Steam

- Download the Python File and simply run it

```bash
  chmod +x steam-precache-cleaner.py
  python3 ./steam-precache-cleaner.py
```


- Start Steam and activate Shader Pre-Caching in the Settings again
