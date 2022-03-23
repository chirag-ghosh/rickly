import React, { createContext, useContext, useState } from "react";
import { Player, Team } from "../types";

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