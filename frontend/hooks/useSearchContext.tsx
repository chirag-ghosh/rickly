import React, { createContext, useContext, useEffect, useState } from "react";
import { Player, Team } from "../types";
import { samplePlayers, sampleTeams } from "../utils/sampleData";
import fuzzysort from "fuzzysort";

type SearchContextType = {
    query: string;
    setQuery: (val: string) => void;
    teams: Team[];
    setTeams: (val: Team[]) => void;
    players: Player[];
    setPlayers: (val: Player[]) => void;
};

const SearchContext = createContext<SearchContextType>(undefined!);
export const useSearchContext = () => useContext(SearchContext);

export const SearchProvider: React.FC = ({children}: any) => {

    const [query, setQuery] = useState<string>("");
    const [teams, setTeams] = useState<Team[]>([]);
    const [players, setPlayers] = useState<Player[]>([]);

    useEffect(() => {

        if(query === "") {
            setTeams(sampleTeams);
            setPlayers(samplePlayers);
        }
        else {
            setTeams(fuzzysort.go(query, sampleTeams, {key: 'name'}).map((item) => item.obj));
            setPlayers(fuzzysort.go(query, samplePlayers, {key: 'name'}).map((item) => item.obj));
        }
    }, [query]);

    const value = {
        query,
        setQuery,
        teams,
        setTeams,
        players,
        setPlayers
    };

    return <SearchContext.Provider value={value}>{children}</SearchContext.Provider>;
}