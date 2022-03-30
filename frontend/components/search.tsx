import React from 'react';
import { NextComponentType } from "next";
import { useSearchContext } from '../hooks/useSearchContext';
import { Search as SearchIcon } from "react-feather";
import { useRouter } from 'next/router';

const Search: NextComponentType = () => {

    const { query, setQuery, teams, players, tournaments} = useSearchContext();

    const router = useRouter();

    const searchClickHandler = (type: 'team' | 'player' | 'tournament', id: string) => {
        setQuery("");
        if(type === 'team') router.push(`/team/${id}`);
        else if(type === 'player') router.push(`/player/${id}`);
        else router.push(`/tournament/${id}`);
    }

    return(
        <div className="search">
            <input
                type='text'
                placeholder='Search Teams and Players....'
                value={query}
                onChange={(event) => setQuery(event.target.value)}
            />
            <div className='icon'><SearchIcon /></div>
            {query !== "" && (
                <div className='dropdown'>
                    <div className='dropdown-label'>Teams</div>
                    <ul>
                        {teams.map((team, index) => {
                            return(
                                <li key={index} onClick={() => searchClickHandler('team', team.id)}>{team.name}</li>
                            )
                        })}
                        {teams.length === 0 && (
                            <div>No results</div>
                        )}
                    </ul>
                    <div className='dropdown-label'>Players</div>
                    <ul>
                        {players.map((player, index) => {
                            return(
                                <li key={index} onClick={() => searchClickHandler('player', player.id)}>{player.name}</li>
                            )
                        })}
                        {players.length === 0 && (
                            <div>No results</div>
                        )}
                    </ul>
                    <div className='dropdown-label'>Tournaments</div>
                    <ul>
                        {tournaments.map((tournament, index) => {
                            return(
                                <li key={index} onClick={() => searchClickHandler('tournament', tournament.id)}>{tournament.name}</li>
                            )
                        })}
                        {tournaments.length === 0 && (
                            <div>No results</div>
                        )}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default Search;