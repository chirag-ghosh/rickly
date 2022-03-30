export type Team = {
    id: string,
    name: string,
    captain: string,
    wicketKeeper: string,
    coach: string,
    playersList: string[]
}

export type Player = {
    id: string,
    name: string,
    age: number,
    gender: 'male' | 'female' | 'others',
    team: string,
    role: 'batter' | 'bowler' | 'allrounder' | 'wicketkeeper',
    specifics: string,
    bathandedness: 'right' | 'left',
    ballhandedness: 'right' | 'left'
}

export type QuickCardProps = {
    title: string,
    imgSrc: string,
    link: string
}

export type Tournament = {
    id: string,
    name: string,
    match_num: number,
    scheduled: boolean,
    completed: boolean
}

export type Match = {
    id: string,
    tournament: string,
    teamA: string,
    teamB: string,
    date: string,
    winner?: string
}