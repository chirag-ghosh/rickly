import axios from "axios";
import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../hooks/useSearchContext";
import { Tournament } from "../../types";
import { BACKEND_URL } from "../../utils/constants";
import { sampleTournaments } from "../../utils/sampleData";

const Tournament: NextPage = () => {

    const { tournamentList } = useSearchContext();

    const [newTournamentName, setNewTournamentName] = useState<string>('');
    const [mode, setMode] = useState<('unscheduled' | 'scheduled' | 'completed')>('unscheduled');
    const [tournaments, setTournaments] = useState<Tournament[]>([]);

    const router = useRouter();

    useEffect(() => {

        setTournaments(tournamentList.filter((tournament) => {
            if(mode === 'unscheduled')
                return !tournament.scheduled;
            else if(mode === 'scheduled')
                return (tournament.scheduled && !tournament.completed);
            else
                return tournament.completed;

        }));
    }, [mode, tournamentList]);

    const createNewTournament = (name: string) => {

        axios.post(`${BACKEND_URL}/tournaments/`, {
            name,
            "match_set": [],
            "team_set": []
        })
        .then((res) => {
            router.reload();
        })
        .catch((err) => console.log(err));
    }

    return(
        <div className="tournaments-page">
            <h1>Tournaments</h1>
            <div className="new-tournament">
                <h2>Create new Tournament <span>( All teams present will be played )</span></h2>
                <div className="input-bar">
                    <input type='text' placeholder="Enter tournament name" onChange={(event) => setNewTournamentName(event.target.value)}></input>
                    <button onClick={() => createNewTournament(newTournamentName)}>Create tournament</button>
                </div>
            </div>
            <div className="browse-tournaments">
                <h2>Browse tournaments</h2>
                <div className="button-group">
                    <button onClick={() => setMode('unscheduled')} className={`${mode === 'unscheduled' ? 'active' : ''}`}>Unscheduled</button>
                    <button onClick={() => setMode('scheduled')} className={`${mode === 'scheduled' ? 'active' : ''}`}>Scheduled</button>
                    <button onClick={() => setMode('completed')} className={`${mode === 'completed' ? 'active' : ''}`}>Completed</button>
                </div>
                <div className="tournament-list">
                    {
                        tournaments.map((tournament) => {
                            return(
                                <div onClick={() => router.push(`tournament/${tournament.id}`)}>{tournament.name}</div>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default Tournament;