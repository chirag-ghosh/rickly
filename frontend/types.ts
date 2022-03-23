export type Team = {
    name: string,
    captain: Player,
    wicketKeeper: Player,
    playersList: Player[]
}

export type Player = {
    name: string,
    age: number,
    gender: 'male' | 'female' | 'others',
    team: Team,
    category: 'batsman' | 'bowler' | 'allrounder'
}