const axios = require('axios');
const readline = require('readline');

const serverUrl = 'http://localhost:9339'; 

const sendPacketToServer = async (packet) => {
  try {
    const response = await axios.post(`${serverUrl}/process_packet`, { packet });
    console.log(response.data.message);
  } catch (error) {
    console.error('Error:', error.message);
  }
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const askForPacket = () => {
  rl.question('Enter a packet number (1-99): ', (userInput) => {
    const packet = parseInt(userInput);
    if (!isNaN(packet) && packet >= 1 && packet <= 99) {
      sendPacketToServer(packet);
    } else {
      console.log('Please enter a valid packet number between 1 and 99.');
    }
    askForPacket();
  });
};

askForPacket(); 
