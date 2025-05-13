const gameDescription = document.getElementById("gameDescription");

document.getElementById("rocket").addEventListener("mouseover", () => {
  gameDescription.textContent = "Rocket League: A fast-paced football game played with rocket-powered cars.";
});

// Crete a mouseover event for the other games listed on the games web page, use the descriptions below
// "Minecraft: A creative sandbox game where you can build, mine, and explore."
// "Super Smash Bros: A fighting game featuring characters from various game universes."
// "FIFA: A realistic football simulation game with real-world teams and leagues."

// Resets the description when the mouse leaves the list
const listItems = document.querySelectorAll("li");
listItems.forEach(item => {
  item.addEventListener("mouseout", () => {
    gameDescription.textContent = "Hover over a game name to learn more about it.";
  });
});
