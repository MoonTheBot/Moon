const { ShardingManager } = require('discord.js');
const manager = new ShardingManager('./index.js');

manager.spawn();
manager.on('launch', shard => console.log(`Launched shard ${shard.id}`));
