import { Player, Team, Tournament } from "../types";

export const getTeamFromID = (id: string | string[] | undefined, teamList: Team[]): Team | null => {

    console.log(id, teamList)
    if(id === undefined) return null;
    for(var i = 0; i < teamList.length; i++) {
        console.log(teamList[i].id, id)
        if(teamList[i].id == id) return teamList[i];
    }
    return null;
}

export const getPlayerFromID = (id: string | string[] | undefined, playerList: Player[]): Player | null => {

    if(id === undefined) return null;
    for(var i = 0; i < playerList.length; i++) {
        if(playerList[i].id == id) return playerList[i];
    }
    return null;
}

export const getTournamentFromID = (id: string | string[] | undefined, tournamentList: Tournament[]): Tournament | null => {

    if(id === undefined) return null;
    for(var i = 0; i < tournamentList.length; i++) {
        if(tournamentList[i].id == id) return tournamentList[i];
    }
    return null;
}