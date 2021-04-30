while true
do
    sleep 15m #sleep NUMBER[SUFFIX]. SUFFIX= seconds (s), minutes (m), hours (h) and days (d). Given value 15m is 15 minutes.
    echo "Preventing site from idling..."
    wget -q -O/dev/null $BASE_URL_OF_BOT
done
