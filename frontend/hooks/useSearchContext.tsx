import React, { createContext, useContext, useEffect, useState } from "react";
import { Player, Team, Tournament } from "../types";
import { samplePlayers, sampleTeams } from "../utils/sampleData";
import fuzzysort from "fuzzysort";
import axios from "axios";
import { BACKEND_URL } from "../utils/constants";

type SearchContextType = {
    query: string;
    setQuery: (val: string) => void;
    teamList: Team[];
    setTeamList: (val: Team[]) => void;
    teams: Team[];
    setTeams: (val: Team[]) => void;
    playerList: Player[];
    setPlayerList: (val: Player[]) => void;
    players: Player[];
    setPlayers: (val: Player[]) => void;
    tournamentList: Tournament[];
    setTournamentList: (val: Tournament[]) => void;
    tournaments: Tournament[];
    setTournaments: (val: Tournament[]) => void;
};

const SearchContext = createContext<SearchContextType>(undefined!);
export const useSearchContext = () => useContext(SearchContext);

export const SearchProvider: React.FC = ({children}: any) => {

    const [query, setQuery] = useState<string>("");
    const [teams, setTeams] = useState<Team[]>([]);
    const [teamList, setTeamList] = useState<Team[]>([]);
    const [players, setPlayers] = useState<Player[]>([]);
    const [playerList, setPlayerList] = useState<Player[]>([]);
    const [tournaments, setTournaments] = useState<Tournament[]>([]);
    const [tournamentList, setTournamentList] = useState<Tournament[]>([]);

    useEffect(() => {

        axios.get(`${BACKEND_URL}/tournaments`)
            .then((response) => {
                setTournamentList(response.data);
            })
    }, []);

    useEffect(() => {

        if(query === "") {
            setTeams(teamList);
            setPlayers(playerList);
            setTournaments(tournamentList);
        }
        else {
            setTeams(fuzzysort.go(query, teamList, {key: 'name'}).map((item) => item.obj));
            setPlayers(fuzzysort.go(query, playerList, {key: 'name'}).map((item) => item.obj));
            setTournaments(fuzzysort.go(query, tournamentList, {key: 'name'}).map((item) => item.obj));
        }
    }, [query]);

    const value = {
        query,
        setQuery,
        teamList,
        setTeamList,
        teams,
        setTeams,
        playerList,
        setPlayerList,
        players,
        setPlayers,
        tournamentList,
        setTournamentList,
        tournaments,
        setTournaments
    };

    return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
}