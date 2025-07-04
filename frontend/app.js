const socket = io("https://your-backend-service-name.onrender.com"); // Will work inside container network

socket.on("stock_update", (data) => {
  const stockDiv = document.createElement("div");
  stockDiv.className = "stock";
  stockDiv.innerText = `${data.symbol}: $${data.price} @ ${new Date(data.timestamp * 1000).toLocaleTimeString()}`;
  document.getElementById("stocks").prepend(stockDiv);
});
