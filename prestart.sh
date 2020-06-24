#! /usr/bin/bash
# 文件路径：/app/prestart.sh 
echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"
 
echo "
#! /usr/bin/env bash
# Let the DB start
sleep 10;
# Run migrations
aerich upgrade
"
