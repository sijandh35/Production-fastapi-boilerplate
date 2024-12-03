// Variables
const dbName = process.env.MONGO_INITDB_DATABASE || 'mydatabase';
const adminUser = process.env.MONGO_INITDB_ROOT_USERNAME || 'admin';
const adminPassword = process.env.MONGO_INITDB_ROOT_PASSWORD || 'password';
const userRole = 'readWrite';

console.log("DB Name:", dbName);

// Sleep function (to simulate delay)
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Async function to handle MongoDB initialization
async function initMongoDB() {
    console.log("Starting MongoDB initialization...");

    // Delay to ensure MongoDB is fully up and running
    await sleep(5000);  // Delay for 5 seconds (5000 ms)
    console.log("Waited for 5 seconds to ensure MongoDB readiness.");

    // Connect to the target database
    db = db.getSiblingDB(dbName);

    // Explicitly create the database by inserting a dummy document
    db.testCollection.insertOne({ initialized: true });
    console.log(`Database '${dbName}' created.`);

    // Check if user already exists
    if (db.getUser(adminUser) === null) {
        // Create the user with the specified role
        db.createUser({
            user: adminUser,
            pwd: adminPassword,
            roles: [{
                role: userRole,
                db: dbName
            }]
        });

        console.log(`Created user '${adminUser}' with role '${userRole}' on database '${dbName}'.`);
    } else {
        console.log(`User '${adminUser}' already exists on database '${dbName}'.`);
    }

    console.log("MongoDB initialization complete.");
}

// Run the async initialization function
initMongoDB();
