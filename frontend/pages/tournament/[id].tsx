import axios from "axios";
import { useRouter } from "next/router";
import { useEffect, useMemo, useState } from "react";
import Table from "../../components/table";
import { useSearchContext } from "../../hooks/useSearchContext";
import { Match } from "../../types";
import { BACKEND_URL } from "../../utils/constants";
import { getTournamentFromID } from "../../utils/helpers";
import { sampleMatches } from "../../utils/sampleData";

const Tournament = () => {

    const {tournamentList} = useSearchContext();
    const router = useRouter();
    const tournament = getTournamentFromID(router.query.id, tournamentList);

    const [matches, setMatches] = useState<Match[]>([]);

    useEffect(() => {

        setMatches(sampleMatches.filter((match) => {
            return match.tournament === tournament?.name
        }))
    }, []);

    const createSchedule = () => {

        axios.post(`${BACKEND_URL}/tournaments/unscheduled/${router.query.id}/`)
            .then((res) => {
                router.reload();
            })
            .catch((err) => console.log(err));
    }



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
            accessor: 'id',
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
                    <div>
                        <h3>Tournament matches not scheduled yet.</h3>
                        <button onClick={() => createSchedule()}>Create Schedule</button>
                    </div>
                )
            }
        </div>
    )
}

export default Tournament;