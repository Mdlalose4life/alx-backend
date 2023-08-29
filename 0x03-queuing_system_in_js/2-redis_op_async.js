import { redis } from 'redis';
import { print } from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`)
});

function setNewSchool(schoolName, value){
  client.set(schoolName, value, print);
}


const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName){
  const response = await client.get(schoolName).catch((err) => {
    if (err) {
      console.log(err);
      throw err;
    }
  });
  console.log(response)
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");