import { useRouter } from "next/router"
import React from "react";
import Table from "../../components/table";
import { getTeamFromID } from "../../utils/helpers";
import { samplePlayers } from "../../utils/sampleData";

const Team = () => {

    const router = useRouter();
    const team = getTeamFromID(router.query.id);

    const data = React.useMemo(() => [...samplePlayers.filter((player) => player.team === team?.name)], []);
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
            Header: 'Gender',
            accessor: 'gender',
        },
        {
            Header: 'Category',
            accessor: 'category'
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
                        <div className="team-highlight blue">
                            <h2>Coach</h2>
                            <div>{team.coach}</div>
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