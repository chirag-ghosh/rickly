import { Player, Team, Tournament } from "../types";

export const samplePlayers: Player[] = [];
export const sampleTeams: Team[] = [];

samplePlayers.push({
    uuid: "e46478a3-80c8-48cf-b64b-71fe93b134d6",
    name: "Aritra Mitra",
    age: 96,
    gender: 'male',
    category: 'batsman',
    team: 'Retards'
})
samplePlayers.push({
    uuid: "b144c2e1-1da5-4aa6-82b3-4c33980c01f6",
    name: "Devendra Palod",
    age: 69,
    gender: 'male',
    category: 'bowler',
    team: 'Retards'
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

export const sampleTournaments: Tournament[] = [
    {
        uuid: '23297962-b409-4c3a-974c-4dd7082de525',
        name: "AGB Premiere League",
        matchCount: 4,
        scheduled: true,
        completed: false
    },
    {
        uuid: 'a3d1ff70-d74a-4dc9-a0d6-7283d9d292b5',
        name: "Vidyasagar Premiere League",
        matchCount: 12,
        scheduled: true,
        completed: true
    },
    {
        uuid: '5a554346-2c7a-4224-b220-aa303e065376',
        name: "Indian Premiere League",
        matchCount: 52,
        scheduled: false,
        completed: false
    }
];