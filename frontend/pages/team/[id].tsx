import { useRouter } from "next/router"
import React from "react";
import Table from "../../components/table";
import { useSearchContext } from "../../hooks/useSearchContext";
import { getTeamFromID } from "../../utils/helpers";
import { samplePlayers } from "../../utils/sampleData";

const Team = () => {

    const {teamList} = useSearchContext();
    const router = useRouter();
    const team = getTeamFromID(router.query.id, teamList);

    const {playerList} = useSearchContext();

    const data = React.useMemo(() => [...playerList.filter((player) => player.team === team?.name)], []);
    const columns = React.useMemo(() => [
        {
            Header: 'Name',
            accessor: 'name'
        },
        {
            Header: 'Age',
            accessor: 'age',
        },
        {
            Header: 'Category',
            accessor: 'role'
        },
        {
            Header: 'Batting Hand',
            accessor: 'bathandedness'
        },
        {
            Header: 'Bowling Hand',
            accessor: 'ballhandedness'
        }
    ], []);

    return(
        <div className="teams-page">{
            team === null ? (
                <h1>No valid team found</h1>
            )
            : (
                <div className="teams-page-container">
                    <h1>{team.name}</h1>
                    <div className="team-top-bar">
                        <div className="team-highlight red">
                            <h2>Captain</h2>
                            <div>{team.captain}</div>
                        </div>
                        <div className="team-highlight green">
                            <h2>Wicket Keeper</h2>
                            <div>{team.wicketKeeper}</div>
                        </div>
                    </div>
                    <div className="team-players">
                        <h2>Players</h2>
                        <Table data={data} columns={columns} />
                    </div>
                </div>
            )
        }</div>
    )
}

export default Team;