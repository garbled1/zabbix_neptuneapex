# zabbix_neptuneapex
Zabbix 4.0 template for Neptune Apex

# What is the point of this?
Maybe you are like me and want to just be able to easily graph data off the
Apex on a multi-year scale?

Maybe you don't trust Fusion to send you alerts?  (seems paranoid)

One idea is to watch for the names of variable speed profiles to change back to something like PF1, to know when the Apex lost it's programming?

You like doing pointless things?

# Notes
* Currently no triggers defined, the Apex itself does this, not sure what
  to trigger on yet.
* The histories are set to massive values, 1 year for history, 5 years for trend
* If you have modified your apex password/username, set them with the macros {$APEX.USER} and {$APEX.PASS}
* Autodiscovery runs every 24 hours. Any less than this seems silly.
* Classic Apexs don't have a model number.  Huh.
* The default username on my classic was "admin", but "Admin" on my new one.

# How to install
Place the apex_discovery.py script in your externalscripts directory, and make
it mode 755.

Import the template, and apply it to an Apex. I also like to apply the basic
http template, just for fun.
