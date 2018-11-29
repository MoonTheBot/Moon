module.exports = async (client) => {
    client.logger.log(`Logged in as ${client.user.username} and on ${client.guilds.size} guilds.`);
    client.user.setStatus("dnd");
    client.user.setActivity(`${client.config.defaultSettings.prefix}help | ${client.guilds.size} servers`);
};