while true
do
    sleep 5m #sleep NUMBER[SUFFIX]. SUFFIX= seconds (s), minutes (m), hours (h) and days (d). Given value 5m is 5 minutes.
    echo "Preventing site from idling..."
    wget -q -O/dev/null $BASE_URL_OF_BOT
done
