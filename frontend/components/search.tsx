import React from 'react';
import { NextComponentType } from "next";
import { useSearchContext } from '../hooks/useSearchContext';
import { Search as SearchIcon } from "react-feather";

const Search: NextComponentType = () => {

    const { query, setQuery, teams, players} = useSearchContext();

    const searchClickHandler = (type: 'team' | 'player', item: string) => {
        setQuery("");
        console.log(item);
        //move to corresponding section
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
                                <li key={index} onClick={() => searchClickHandler('team', team.name)}>{team.name}</li>
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
                                <li key={index} onClick={() => searchClickHandler('player', player.name)}>{player.name}</li>
                            )
                        })}
                        {players.length === 0 && (
                            <div>No results</div>
                        )}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default Search;