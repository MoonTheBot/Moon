const Discord = require("discord.js");
const { version } = require("discord.js");
const os = require("os");
const cpu = require("cpu-stat");
const moment = require("moment");
require("moment-duration-format");

exports.run = async (client, message, args, level, error) => {
    cpu.usagePercent(function (err, percent, seconds) {
        if (err) {
            return client.logger.error(`An unexpected error has occurred while fetching CPU usage: ${JSON.stringify(err)}`);
        }
    });

    const duration = moment.duration(client.uptime).format(" D [days] : H [hrs] : m [mins] : s [secs]");

    const embed = new Discord.RichEmbed()
    .setTitle("System Statistics")
    .addField("Bot Name", `${client.user.tag}`, true)
    .addField("Bot ID", `${client.user.id}`, true)
    .addField("Bot Developer", "Lizcrave", true)
    .addField("Guild Count", `${client.guilds.size}`, true)
    .addField("Channel Count", `${client.channels.size}`, true)
    .addField("User Count", `${client.users.size}`, true)
    .addField("Dependencies", `Node **- ${process.version}**\n\nDiscord.js **- v${version}**\n\nMAPI **- ${client.instance.version}**`, true)
    .addField("Version", `**v${client.instance.version}**`, true)
    .addField("CPU Usage", `${percent.toFixed(2)}%`, true)
    .addField("Mem Usage", `${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)} MB`, true)
    .addField("OS", `${os.platform().toProperCase()}`, true)
    .addField("CPUs", `1`, true)
    .addField("Commands", `${client.commands.length}`, true)
    .addField("Aliases", `${client.aliases.length}`, true)
    .addField("Messages Seen", `${client.channels.map(c => c.messages.size).reduce((c1, c2) => c1 + c2)}`, true)
    .addField("Uptime", `${duration}`)
    .addField("Links", "`[GitHub](https://github.com/Prylaris/Moon)`")
    .addField("Newest Changes", `\`\`\`diff
    + Added error messages to commands
    + Spiced up the stats command
    + Added more backend stuff to help with overall preformance
    - Removed needless code
    - Removed major and minor bugs
    \`\`\``)
    .setColor("#111111")
    return message.channel.send({embed});

    if (error) {
        return message.channel.send("An unexpected error has occurred, try again later.");
    }
};

exports.conf = {
    enabled: true,
    guildOnly: false,
    aliases: [],
    permLevel: "User"
};

exports.help = {
    name: "stats",
    category: "Information",
    description: "Gives some useful bot statistics.",
    usage: "stats"
};
