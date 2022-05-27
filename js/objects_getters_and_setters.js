const team = {
  _players: [
    { firstName: "Roger", lastName: "Castro", age: 21 },
    { firstName: "Bryan", lastName: "Agurcia", age: 22 },
    { firstName: "Raymond", lastName: "Caceres", age: 19 },
  ],
  _games: [
    { opponent: "Los Cholos FC", teamPoints: 3, opponentPoints: 2 },
    { opponent: "Malaga", teamPoints: 3, opponentPoints: 2 },
    { opponent: "Real Madrid", teamPoints: 3, opponentPoints: 2 },
  ],

  get players() {
    return this._players;
  },

  get games() {
    return this._games;
  },

  addPlayer(newFirstName, newLastName, newAge) {
    const player = {
      firstName: newFirstName,
      lastName: newLastName,
      age: newAge
    };
    this._players.push(player);
  },

  addGame(newOpponent, newTeamPoints, newOpponentPoints) {
    const game = {
      opponent: newOpponent,
      teamPoints: newTeamPoints,
      opponentPoints: newOpponentPoints
    }
    this._games.push(game);
  }
}

team.addPlayer("Bugs", "Bunny", 76);
console.log(team.players);

team.addGame("Titans", 100, 98);
console.log(team.games);

