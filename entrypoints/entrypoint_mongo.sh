# #!/bin/bash

# # Start MongoDB in the background
# mongod &

# # Wait for MongoDB to start
# until mongosh --eval "print(\"waited for connection\")"; do
#   echo "Waiting for MongoDB to start..."
#   sleep 1
# done

# # Read environment variables from .env file
# DB_NAME=${MONGO_DB:-aidb}            # Default to 'aidb' if not set
# COLLECTION_NAME=${MONGO_COLLECTION:-tokens}  # Default to 'tokens' if not set

# # Initialize the database and collection if they do not exist
# mongosh <<EOF
# use $DB_NAME
# db.createCollection("$COLLECTION_NAME")
# EOF

# echo "Database '$DB_NAME' and collection '$COLLECTION_NAME' initialized."

# # Keep the MongoDB process running in the foreground
# wait

