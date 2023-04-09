const
  rpcGenerator = require("discordrpcgenerator"),

  // Add your client id in the index.js file And Set Your Stream Info
  IMAGE_NAME = "logo",
  LARGE_TEXT = "Minecraft | Chill",
  SMALL_TEXT = "Join Stream !",
  LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
 
module.exports = (client, CLIENT_ID) => rpcGenerator.getRpcImage(CLIENT_ID, IMAGE_NAME)
  .then(image => client.user.setPresence(
    new rpcGenerator.Rpc()
      .setName("twitch")
      .setUrl(LINK)
      .setType("STREAMING")
      .setApplicationId(CLIENT_ID)
      .setAssetsLargeImage(image.id)
      .setAssetsLargeText(SMALL_TEXT)
      .setDetails(LARGE_TEXT)
      .toDiscord()
  ));
