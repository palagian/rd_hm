document.addEventListener("DOMContentLoaded", () => {
  var friendCount = Math.floor(Math.random() * 1000);
  document.getElementById("friend-count").textContent = friendCount;

  var isFriendButtonVisible = true;
  var isMessageButtonClicked = false;
  var isJobButtonClicked = false;

  function addFriend() {
    var addButton = document.getElementById("add-friend-btn");

    if (!isJobButtonClicked && isFriendButtonVisible) {
      addButton.textContent = "Pending confirmation";
      addButton.disabled = true;
      isFriendButtonVisible = false;
      var friendCountElement = document.getElementById("friend-count");
      friendCountElement.textContent = parseInt(friendCountElement.textContent) + 1;
    }
  }

  var messageButtonColors = ["red", "green", "black", "brown", "purple"];
  var colorIndex = 0;

  function changeButtonColor() {
    var messageButton = document.getElementById("send-message-btn");

    if (isMessageButtonClicked) {
      messageButton.style.backgroundColor = "";
    } else {
      colorIndex = (colorIndex + 1) % messageButtonColors.length;
      messageButton.style.backgroundColor = messageButtonColors[colorIndex];
    }

    isMessageButtonClicked = !isMessageButtonClicked;
  }

  function toggleJobButton() {
    var addButton = document.getElementById("add-friend-btn");
    var jobButton = document.getElementById("offer-job-btn");

    if (!isJobButtonClicked) {
      addButton.style.display = "none";
      isFriendButtonVisible = false;
    } else {
      addButton.style.display = "flex";
      isFriendButtonVisible = true;
    }

    isJobButtonClicked = !isJobButtonClicked;
  }

  function sendHW() {
    var tableBody = document.getElementById("hw-table-body");
    var newRow = document.createElement("tr");
    var homeworkCell = document.createElement("td");
    homeworkCell.textContent = "№26 «Базова робота з HTML/CSS»";
    var scoreCell = document.createElement("td");
    scoreCell.textContent = "7 / 7";
    newRow.appendChild(homeworkCell);
    newRow.appendChild(scoreCell);
    tableBody.appendChild(newRow);
  }

  var addButton = document.getElementById("add-friend-btn");
  addButton.addEventListener("click", addFriend);

  var messageButton = document.getElementById("send-message-btn");
  messageButton.addEventListener("click", changeButtonColor);

  var jobButton = document.getElementById("offer-job-btn");
  jobButton.addEventListener("click", toggleJobButton);

  var sendHWButton = document.getElementById("send-hw-btn");
  sendHWButton.addEventListener("click", sendHW);
});
