module.exports = async (client) => {
    client.user.setStaus("dnd");
    client.user.setActivity(`${client.config.defaultSettings.prefix}help | ${client.guilds.size} servers`);
};