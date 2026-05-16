#!/bin/bash
sleep 3

# Apply wallpaper to ALL detected monitors/workspaces
for MONITOR in $(xfconf-query -c xfce4-desktop -l | grep last-image | sed 's|/workspace.*||' | sort -u); do
  xfconf-query -c xfce4-desktop -p "$MONITOR/workspace0/last-image" \
    -s /usr/share/backgrounds/heimdall/heimdall-wallpaper.png
done

