import { Team } from "../types";
import { sampleTeams } from "./sampleData";

export const getTeamFromID = (id: string | string[] | undefined): Team | null => {

    if(id === undefined) return null;
    const teamList = sampleTeams;
    for(var i = 0; i < teamList.length; i++) {
        if(teamList[i].uuid === id) return teamList[i];
    }
    return null;
}