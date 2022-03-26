import { Player, Team } from "../types";

export const samplePlayers: Player[] = [];
export const sampleTeams: Team[] = [];

samplePlayers.push({
    uuid: "e46478a3-80c8-48cf-b64b-71fe93b134d6",
    name: "Aritra Mitra",
    age: 96,
    gender: 'male',
    category: 'batsman',
    team: 'retards'
})
samplePlayers.push({
    uuid: "b144c2e1-1da5-4aa6-82b3-4c33980c01f6",
    name: "Devendra Palod",
    age: 69,
    gender: 'male',
    category: 'bowler',
    team: 'retards'
})
samplePlayers.push({
    uuid: "b932504b-553a-4204-9c6e-4fab05d9e5df",
    name: "Anubhav Dhar",
    age: 11,
    gender: 'male',
    category: 'allrounder',
    team: 'AGB'
})

sampleTeams.push({
    uuid: "db71f064-b158-4b35-b3cd-de15706ea2a6",
    name: "AGB",
    captain: 'Anubhav Dhar',
    wicketKeeper: 'Anubhav Dhar',
    coach: 'Shah Dhruv Rajendrabhai',
    playersList: ['Anubhav Dhar']
})
sampleTeams.push({
    uuid: "dfd5a36d-cfec-4e12-bd48-30b502c9572d",
    name: "Retards",
    captain: 'Aritra Mitra',
    wicketKeeper: 'Devendra Palod',
    coach: 'Subhu Halder',
    playersList: ['Aritra Mitra', 'Devendra Palod']
})