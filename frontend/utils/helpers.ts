import { Player, Team, Tournament } from "../types";
import { samplePlayers, sampleTeams, sampleTournaments } from "./sampleData";

export const getTeamFromID = (id: string | string[] | undefined): Team | null => {

    if(id === undefined) return null;
    const teamList = sampleTeams;
    for(var i = 0; i < teamList.length; i++) {
        if(teamList[i].uuid === id) return teamList[i];
    }
    return null;
}

export const getPlayerFromID = (id: string | string[] | undefined): Player | null => {

    if(id === undefined) return null;
    const playerList = samplePlayers;
    for(var i = 0; i < playerList.length; i++) {
        if(playerList[i].uuid === id) return playerList[i];
    }
    return null;
}

export const getTournamentFromID = (id: string | string[] | undefined): Tournament | null => {

    if(id === undefined) return null;
    const tournamentList = sampleTournaments;
    for(var i = 0; i < tournamentList.length; i++) {
        if(tournamentList[i].uuid === id) return tournamentList[i];
    }
    return null;
}