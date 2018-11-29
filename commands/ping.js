const Discord = require("discord.js");

exports.run = async (client, message, args, level) => {
    const msg = await message.channel.send("Pinging...");
    const embed = new Discord.RichEmbed()
    .setTitle("🏓 Pong!")
    .addField("Message Latency", `\`${msg.createdTimestamp - message.createdTimestamp} ms\``)
    .addField("API Response Time", `\`${Math.round(client.ping)} ms\``)
    .addField("Other Pings", `\`${client.pings}\``)
    .setColor("FF001D")
    return message.channel.send({embed});
};

exports.conf = {
    enabled: true,
    guildOnly: false,
    aliases: [],
    permLevel: "User"
};

exports.help = {
    name: "ping",
    category: "Information",
    description: "Returns the latency of the bot.",
    usage: "ping"
};