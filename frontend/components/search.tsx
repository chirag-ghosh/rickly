import React from 'react';
import { NextComponentType } from "next";
import { useSearchContext } from '../hooks/useSearchContext';
import { Search as SearchIcon } from "react-feather";

const Search: NextComponentType = () => {

    const { query, setQuery, teams, players} = useSearchContext();

    return(
        <div className="search">
            <input
                type='text'
                placeholder='Search Teams and Players....'
                value={query}
                onChange={(event) => setQuery(event.target.value)}
            />
            <div className='icon'><SearchIcon /></div>
        </div>
    )
}

export default Search;