import { Match, Player, Team, Tournament } from "../types";

export const samplePlayers: Player[] = [];
export const sampleTeams: Team[] = [];

samplePlayers.push({
    id: "e46478a3-80c8-48cf-b64b-71fe93b134d6",
    name: "Aritra Mitra",
    age: 96,
    gender: 'male',
    category: 'batsman',
    team: 'Retards'
})
samplePlayers.push({
    id: "b144c2e1-1da5-4aa6-82b3-4c33980c01f6",
    name: "Devendra Palod",
    age: 69,
    gender: 'male',
    category: 'bowler',
    team: 'Retards'
})
samplePlayers.push({
    id: "b932504b-553a-4204-9c6e-4fab05d9e5df",
    name: "Anubhav Dhar",
    age: 11,
    gender: 'male',
    category: 'allrounder',
    team: 'AGB'
})

sampleTeams.push({
    id: "db71f064-b158-4b35-b3cd-de15706ea2a6",
    name: "AGB",
    captain: 'Anubhav Dhar',
    wicketKeeper: 'Anubhav Dhar',
    coach: 'Shah Dhruv Rajendrabhai',
    playersList: ['Anubhav Dhar']
})
sampleTeams.push({
    id: "dfd5a36d-cfec-4e12-bd48-30b502c9572d",
    name: "Retards",
    captain: 'Aritra Mitra',
    wicketKeeper: 'Devendra Palod',
    coach: 'Subhu Halder',
    playersList: ['Aritra Mitra', 'Devendra Palod']
})

export const sampleTournaments: Tournament[] = [
    {
        id: '23297962-b409-4c3a-974c-4dd7082de525',
        name: "AGB Premiere League",
        match_num: 4,
        scheduled: true,
        completed: false
    },
    {
        id: 'a3d1ff70-d74a-4dc9-a0d6-7283d9d292b5',
        name: "Vidyasagar Premiere League",
        match_num: 12,
        scheduled: true,
        completed: true
    },
    {
        id: '5a554346-2c7a-4224-b220-aa303e065376',
        name: "Indian Premiere League",
        match_num: 52,
        scheduled: false,
        completed: false
    }
];

export const sampleMatches: Match[] = [
    {
        id: '2978760b-5f42-4a81-9aa4-2b8418bbd7c6',
        tournament: 'AGB Premiere League',
        teamA: 'AGB',
        teamB: 'Retards',
        date: '2022-03-20'
    },
    {
        id: '784a5bb8-db51-4ea6-a43e-0bdcd8f0cdf9',
        tournament: 'AGB Premiere League',
        teamA: 'Retards',
        teamB: 'AGB',
        date: '2022-03-22'
    },
    {
        id: '4347bca5-e381-481f-8f65-636d3e83f824',
        tournament: 'Vidyasagar Premiere League',
        teamA: 'AGB',
        teamB: 'Retards',
        date: '2022-03-02',
        winner: 'AGB'
    },
    {
        id: 'dc089073-de2d-49cd-817d-e7377bd51082',
        tournament: 'Vidyasagar Premiere League',
        teamA: 'Retards',
        teamB: 'AGB',
        date: '2022-03-06',
        winner: 'Retards'
    }
]