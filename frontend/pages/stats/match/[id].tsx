import axios from "axios";
import { useRouter } from "next/router";
import { useEffect, useMemo, useState } from "react";
import Table from "../../../components/table";
import { BACKEND_URL } from "../../../utils/constants";

const Match = () => {

    const router = useRouter();

    const [matchDetails, setMatchDetails] = useState<any>();
    const [innings1Data, setInnings1Data] = useState<any[]>([]);
    const [innings2Data, setInnings2Data] = useState<any[]>([]);

    useEffect(() => {

        axios.get(`${BACKEND_URL}/matches/${router.query.id}`)
            .then((response) => {
                const i1: any[] = [];
                for(var i = 0; i < response.data.scoreline_set[0].length; i+=2) {
                    const playerData = {
                        name: response.data.scoreline_set[0][i][0][0],
                        role: response.data.scoreline_set[0][i][0][1],
                        runs: response.data.scoreline_set[0][i+1][0],
                        balls: response.data.scoreline_set[0][i+1][1],
                        out: response.data.scoreline_set[0][i+1][2] ? response.data.scoreline_set[0][i+1][3] : "Not Out"
                    }
                    i1.push(playerData);
                }
                setInnings1Data(i1);

                const i2: any[] = [];
                for(var i = 0; i < response.data.scoreline_set[1].length; i+=2) {
                    const playerData = {
                        name: response.data.scoreline_set[1][i][0][0],
                        role: response.data.scoreline_set[1][i][0][1],
                        runs: response.data.scoreline_set[1][i+1][0],
                        balls: response.data.scoreline_set[1][i+1][1],
                        out: response.data.scoreline_set[1][i+1][2] ? response.data.scoreline_set[1][i+1][3] : "Not Out"
                    }
                    i2.push(playerData);
                }
                setInnings2Data(i2);
            })
            .catch((err) => console.log(err));
    }, []);

    const data1 = useMemo(() => [...innings1Data], [innings1Data]);
    const data2 = useMemo(() => [...innings2Data], [innings2Data]);

    const columns = useMemo(() => [
        {
            Header: 'Name',
            accessor: 'name',
        },
        {
            Header: 'Role',
            accessor: 'role',
        },
        {
            Header: 'Runs scored',
            accessor: 'runs',
        },
        {
            Header: 'Balls Faced',
            accessor: 'balls',
        },
        {
            Header: 'Out',
            accessor: 'out',
        },
    ], []);

    return(
        <div>
            <h1>Innings 1</h1>
            <Table data={data1} columns={columns} />
            <h2>Innings 2</h2>
            <Table data={data2} columns={columns} />
        </div>
    )
}

export default Match;