echo "Are you sure you want to populate the database with the entire JSONL? (yes/no):"
read response
if [ "$response" != "yes" ]; then
    echo "Aborting ..."
    exit 1
fi
