export type Team = {
    name: string,
    captain: string,
    wicketKeeper: string,
    playersList: string[]
}

export type Player = {
    name: string,
    age: number,
    gender: 'male' | 'female' | 'others',
    team: string,
    category: 'batsman' | 'bowler' | 'allrounder'
}