import { Player, Team } from "../types";

export const samplePlayers: Player[] = [];
export const sampleTeams: Team[] = [];

samplePlayers.push({
    name: "Aritra Mitra",
    age: 96,
    gender: 'male',
    category: 'batsman',
    team: 'retards'
})
samplePlayers.push({
    name: "Devendra Palod",
    age: 69,
    gender: 'male',
    category: 'bowler',
    team: 'retards'
})
samplePlayers.push({
    name: "Anubhav Dhar",
    age: 11,
    gender: 'male',
    category: 'allrounder',
    team: 'AGB'
})

sampleTeams.push({
    name: "AGB",
    captain: 'Anubhav Dhar',
    wicketKeeper: 'Anubhav Dhar',
    playersList: ['Anubhav Dhar']
})
sampleTeams.push({
    name: "Retards",
    captain: 'Aritra Mitra',
    wicketKeeper: 'Devendra Palod',
    playersList: ['Aritra Mitra', 'Devendra Palod']
})