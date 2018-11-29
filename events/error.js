module.exports = async (client, error) => {
    await client.logger.error(`An unexpected error has occurred: ${JSON.stringify(error)}`);
    await console.log("> Terminating session and rebooting.");
    await process.exit(1);
};