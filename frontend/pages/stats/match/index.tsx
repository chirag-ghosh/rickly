import { useRouter } from "next/router";
import { useEffect, useMemo, useState } from "react";
import Table from "../../../components/table";
import { Match } from "../../../types";

const Match = () => {

    const router = useRouter();

    const [matchList, setMatchList] = useState<Match[]>([]);

    // useEffect(() => {
    //     setMatchList(sampleMatches);
    // }, []);

    const data = useMemo(() => [...matchList], [matchList])

    const columns = useMemo(() => [
        {
            Header: 'Date',
            accessor: 'date'
        },
        {
            Header: 'Tournament',
            accessor: 'tournament'
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
            accessor: 'id',
            Cell: ({ cell }: { cell: { value: any } }) => <button onClick={() => router.push(`/stats/match/${cell.value}`)}>Open Stats</button>
        }
    ], [matchList]);

    return(
        <div className="teams-page">
            <h1>List of all matches</h1>
            <Table data={data} columns={columns} />
        </div>
    )
}

export default Match;