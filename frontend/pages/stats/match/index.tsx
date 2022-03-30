import axios from "axios";
import { useRouter } from "next/router";
import { useEffect, useMemo, useState } from "react";
import Table from "../../../components/table";
import { useSearchContext } from "../../../hooks/useSearchContext";
import { Match } from "../../../types";
import { BACKEND_URL } from "../../../utils/constants";
import { getTournamentFromID } from "../../../utils/helpers";

const Match = () => {

    const router = useRouter();
    const {tournamentList} = useSearchContext();

    const [matchList, setMatchList] = useState<Match[]>([]);

    useEffect(() => {
        axios.get(`${BACKEND_URL}/matches`)
            .then((response) => setMatchList(response.data))
            .catch((err) => console.log(err));
    }, []);

    const data = useMemo(() => [...matchList], [matchList])

    const columns = useMemo(() => [
        {
            Header: 'Date',
            accessor: 'date',
            Cell: ({ cell }: { cell: { value: any } }) => <div>{(new Date(cell.value)).toDateString()}</div>
        },
        {
            Header: 'Tournament',
            accessor: 'tournament',
            Cell: ({ cell }: { cell: { value: any } }) => <div>{getTournamentFromID(cell.value, tournamentList)?.name}</div>
        },
        {
            Header: 'Team A',
            accessor: 'team_names[0]',
        },
        {
            Header: 'Team B',
            accessor: 'team_names[1]',
        },
        {
            Header: 'Winner',
            accessor: 'winner',
            
        },
        {
            Header: 'Stats',
            accessor: 'id',
            Cell: ({ cell }: { cell: { value: any } }) => <button onClick={() => router.push(`stats/match/${cell.value}`)}>Open Stats</button>
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