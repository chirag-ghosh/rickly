export type Team = {
    uuid: string,
    name: string,
    captain: string,
    wicketKeeper: string,
    coach: string,
    playersList: string[]
}

export type Player = {
    uuid: string,
    name: string,
    age: number,
    gender: 'male' | 'female' | 'others',
    team: string,
    category: 'batsman' | 'bowler' | 'allrounder'
}

export type QuickCardProps = {
    title: string,
    imgSrc: string,
    link: string
}

export type Tournament = {
    uuid: string,
    name: string,
    matchCount: number,
    scheduled: boolean,
    completed: boolean
}

export type Match = {
    uuid: string,
    tournament: string,
    teamA: string,
    teamB: string,
    date: string,
    winner?: string
}