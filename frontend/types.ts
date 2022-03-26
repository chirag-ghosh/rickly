export type Team = {
    uuid: string,
    name: string,
    captain: string,
    wicketKeeper: string,
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