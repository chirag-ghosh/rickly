import { useRouter } from "next/router";
import { useEffect, useMemo, useState } from "react";
import Table from "../../components/table";
import { Match } from "../../types";
import { getTournamentFromID } from "../../utils/helpers";
import { sampleMatches } from "../../utils/sampleData";

const Tournament = () => {

    const router = useRouter();
    const tournament = getTournamentFromID(router.query.id);

    const [matches, setMatches] = useState<Match[]>([]);

    useEffect(() => {

        setMatches(sampleMatches.filter((match) => {
            return match.tournament === tournament?.name
        }))
    }, []);

    const data = useMemo(() => [...matches], [matches])

    const columns = useMemo(() => [
        {
            Header: 'Date',
            accessor: 'date'
        },
        {
            Header: 'Team A',
            accessor: 'teamA',
        },
        {
            Header: 'Team B',
            accessor: 'teamB',
        },
        {
            Header: 'Winner',
            accessor: 'winner',
            Cell: ({ cell }: { cell: { value: any } }) => <div>{cell.value === undefined ? '-' : cell.value}</div>
        },
        {
            Header: 'Stats',
            accessor: 'uuid',
            Cell: ({ cell }: { cell: { value: any } }) => <button onClick={() => router.push(`stats/match/${cell.value}`)}>Open Stats</button>
        }
    ], []);

    return(
        <div className="tournament">
            <h1>{tournament?.name}</h1>
            {
                tournament?.scheduled ? (
                    <div className="tournament-matches">
                        <h3>Match Schedule</h3>
                        <Table data={data} columns={columns} />
                    </div>
                )
                : (
                    <h3>Tournament matches not scheduled yet.</h3>
                )
            }
        </div>
    )
}

export default Tournament;