const { MongoClient } = require('mongodb');

const uri = 'mongodb://127.0.0.1:27017';
const client = new MongoClient(uri);

console.log('initializeDatabase...');

async function initializeDatabase() {
    try {
        console.log('client.connect...');
        await client.connect();
        const db = client.db('octofit_db');

        // Create collections and indexes
        try {
            console.log('Creating users collection...');
            await db.createCollection('users');
            console.log('Creating unique index on email field for users collection...');
            await db.collection('users').createIndex({ email: 1 }, { unique: true });
        } catch (error) {
            console.error('Error creating users collection or index:', error);
        }

        try {
            console.log('Creating teams collection...');
            await db.createCollection('teams');
        } catch (error) {
            console.error('Error creating teams collection:', error);
        }

        try {
            console.log('Creating activity collection...');
            await db.createCollection('activity');
        } catch (error) {
            console.error('Error creating activity collection:', error);
        }

        try {
            console.log('Creating leaderboard collection...');
            await db.createCollection('leaderboard');
        } catch (error) {
            console.error('Error creating leaderboard collection:', error);
        }

        try {
            console.log('Creating workouts collection...');
            await db.createCollection('workouts');
        } catch (error) {
            console.error('Error creating workouts collection:', error);
        }

        console.log('Database and collections initialized successfully.');
    } catch (error) {
        console.error('Error initializing database:', error);
    } finally {
        await client.close();
    }
}

initializeDatabase();
